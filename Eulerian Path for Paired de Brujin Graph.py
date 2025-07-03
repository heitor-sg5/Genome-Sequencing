from collections import defaultdict, deque
import re

def parse_paired_reads(input_str):
    pairs = re.findall(r"\((\w+),(\w+)\)", input_str)
    return [(a, b) for a, b in pairs]

def build_paired_de_bruijn_graph(pairs):
    graph = defaultdict(deque)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for prefix, suffix in pairs:
        from_node = (prefix[:-1], suffix[:-1])
        to_node = (prefix[1:], suffix[1:])
        graph[from_node].append(to_node)
        out_degree[from_node] += 1
        in_degree[to_node] += 1

    return graph, in_degree, out_degree

def find_start_node(graph, in_degree, out_degree):
    for node in graph:
        if out_degree[node] - in_degree[node] == 1:
            return node
    return next(iter(graph))

def find_eulerian_path(graph, in_degree, out_degree):
    graph_copy = {node: deque(neighbour) for node, neighbour in graph.items()}
    path = []
    stack = []

    start = find_start_node(graph, in_degree, out_degree)
    stack.append(start)

    while stack:
        u = stack[-1]
        if u in graph_copy and graph_copy[u]:
            v = graph_copy[u].popleft()
            stack.append(v)
        else:
            path.append(stack.pop())
    path.reverse()
    return path

def reconstruct_genome_from_paired_path(path, k, d):
    prefix_string = path[0][0]
    suffix_string = path[0][1]

    for i in range(1, len(path)):
        prefix_string += path[i][0][-1]
        suffix_string += path[i][1][-1]

    for i in range(k + d, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - k - d]:
            return "No valid genome can be reconstructed"
    
    return prefix_string + suffix_string[-(k + d):]

def paired_de_bruijn_assembly(input_str, k, d):
    pairs = parse_paired_reads(input_str)
    graph, in_degree, out_degree = build_paired_de_bruijn_graph(pairs)
    path = find_eulerian_path(graph, in_degree, out_degree)
    genome = reconstruct_genome_from_paired_path(path, k, d)
    return genome

with open('read_pairs_output.txt', 'r') as file:
    paired_reads_str = file.read().strip()

k = 50
d = 100

graph, in_degree, out_degree = build_paired_de_bruijn_graph(parse_paired_reads(paired_reads_str))
path = find_eulerian_path(graph, in_degree, out_degree)

if path:
    genome = reconstruct_genome_from_paired_path(path, k, d)
    print("Genome:", genome)
else:
    print("No Eulerian path found")

