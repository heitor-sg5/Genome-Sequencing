
def build_overlap_graph_matrix(kmers_str):
    kmers = kmers_str.split()
    n = len(kmers)
    graph = [[0]*n for _ in range(n)]
    
    for i, a in enumerate(kmers):
        suffix = a[1:]
        for j, b in enumerate(kmers):
            prefix = b[:-1]
            if suffix == prefix:
                graph[i][j] = 1
                
    return kmers, graph

def find_hamiltonian_path_matrix(kmers, graph):
    n = len(kmers)
    path = []

    def depth_first_search(current, visited):
        path.append(current)
        if len(path) == n:
            return True
        for neighbour in range(n):
            if graph[current][neighbour] == 1 and neighbour not in visited:
                visited.add(neighbour)
                if depth_first_search(neighbour, visited):
                    return True
                visited.remove(neighbour)
        path.pop()
        return False

    for start in range(n):
        visited = set([start])
        path.clear()
        if depth_first_search(start, visited):
            return path
    return None

def reconstruct_genome_from_path(kmers, path):
    if not path:
        return ""
    genome = kmers[path[0]]
    for index in path[1:]:
        genome += kmers[index][-1] 
    return genome

with open('kmers_output.txt', 'r') as file:
    kmers_str = file.read().strip()

kmers, graph = build_overlap_graph_matrix(kmers_str)
path = find_hamiltonian_path_matrix(kmers, graph)

if path:
    genome = reconstruct_genome_from_path(kmers, path)
    print("Genome:", genome)
else:
    print("No Hamiltonian path found")
