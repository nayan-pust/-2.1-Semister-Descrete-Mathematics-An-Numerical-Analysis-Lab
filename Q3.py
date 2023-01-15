#Problem No. 03
#Name of the Problem: Write a program for graph coloring by Welch- Powell’s algorithm.



def color_nodes(graph):
    color_map = {}
    for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
        neighbor = set(color_map.get(neigh) for neigh in graph[node])
        color_map[node] = next(color for color in range(len(graph)) if color not in neighbor)
    return color_map


graph = {'a': list('bcd'), 'b': list('ac'), 'c': list('abdef'), 'd': list('ace'), 'e': list('cdf'), 'f': list('ce')}
print(color_nodes(graph))




#Output: 
#{'c': 0, 'a': 1,'d': 2, 'e': 1, 'b': 2, 'f': 2}
