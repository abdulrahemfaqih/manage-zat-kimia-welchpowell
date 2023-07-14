graph1 = {}
used_colors = {}


def get_vertex(graph):
    return list(graph.keys())


def get_edges(graph):
    edges = []
    for v in graph:
        for e in graph[v]:
            if {v, e} not in edges:
                edges.append({v, e})
    return edges

def get_degree(edges, vertex):
    degree = 0
    for edge in edges:
        if vertex in edge:
            degree += 1
    return degree


vertex = get_vertex(graph1)

def bubble_sort_by_degree(vertices, edges):
    n = len(vertices)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if get_degree(edges, vertices[j]) < get_degree(edges, vertices[j + 1]):
                vertices[j], vertices[j + 1] = vertices[j + 1], vertices[j]
    return vertices
