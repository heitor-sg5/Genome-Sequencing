from collections import defaultdict

def build_de_bruijn_graph(kmers_str):
    kmers = kmers_str.strip().split()
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    nodes = set()

    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
        out_degree[prefix] += 1
        in_degree[suffix] += 1
        nodes.update([prefix, suffix])

    return graph, nodes, in_degree, out_degree

def is_1_in_1_out(node, in_degree, out_degree):
    return in_degree[node] == 1 and out_degree[node] == 1

def maximal_non_branching_paths(graph, nodes, in_degree, out_degree):
    paths = []
    visited = set()

    for node in nodes:
        if not is_1_in_1_out(node, in_degree, out_degree):
            if node in graph:
                for neighbour in graph[node]:
                    path = [node, neighbour]
                    visited.add((node, neighbour))
                    current = neighbour
                    while is_1_in_1_out(current, in_degree, out_degree):
                        next_node = graph[current][0]
                        path.append(next_node)
                        visited.add((current, next_node))
                        current = next_node
                    paths.append(path)

    for node in nodes:
        if is_1_in_1_out(node, in_degree, out_degree):
            if (node, graph[node][0]) not in visited:
                cycle = [node]
                current = graph[node][0]
                while current != node:
                    cycle.append(current)
                    current = graph[current][0]
                cycle.append(node)
                paths.append(cycle)

    return paths

def path_to_contig(path):
    contig = path[0]
    for node in path[1:]:
        contig += node[-1]
    return contig

def extract_contigs_from_kmers(kmers_str):
    graph, nodes, in_degree, out_degree = build_de_bruijn_graph(kmers_str)
    paths = maximal_non_branching_paths(graph, nodes, in_degree, out_degree)
    contigs = [path_to_contig(path) for path in paths]
    return contigs

with open('kmers_output.txt', 'r') as file:
    kmers_str = file.read().strip()

print(f"Maximal non-branching Eulerian paths: \n{extract_contigs_from_kmers(kmers_str)}")
