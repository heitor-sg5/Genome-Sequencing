from collections import defaultdict, deque

def build_de_bruijn_graph(kmers_str):
    kmers = kmers_str.split()
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
        out_degree[prefix] += 1
        in_degree[suffix] += 1
        
    nodes = set(list(in_degree.keys()) + list(out_degree.keys()))
    return graph, nodes, in_degree, out_degree

def find_start_node(nodes, in_degree, out_degree):
    for node in nodes:
        outdeg = out_degree.get(node, 0)
        indeg = in_degree.get(node, 0)
        if outdeg - indeg == 1:
            return node
    for node in nodes:
        if out_degree.get(node, 0) > 0:
            return node
    return None

def find_eulerian_path(graph, nodes, in_degree, out_degree):
    start_node = find_start_node(nodes, in_degree, out_degree)
    if start_node is None:
        return None
    
    stack = [start_node]
    path = []
    local_graph = {u: deque(v) for u,v in graph.items()}
    
    while stack:
        u = stack[-1]
        if u in local_graph and local_graph[u]:
            v = local_graph[u].popleft()
            stack.append(v)
        else:
            path.append(stack.pop())
    return path[::-1] 

def reconstruct_genome_from_path(path):
    genome = path[0]
    for node in path[1:]:
        genome += node[-1]
    return genome

with open('kmers_output.txt', 'r') as file:
    kmers_str = file.read().strip()

graph, nodes, in_degree, out_degree = build_de_bruijn_graph(kmers_str)
path = find_eulerian_path(graph, nodes, in_degree, out_degree)

if path:
    genome = reconstruct_genome_from_path(path)
    print("Genome:", genome)
else:
    print("No Eulerian path found")
