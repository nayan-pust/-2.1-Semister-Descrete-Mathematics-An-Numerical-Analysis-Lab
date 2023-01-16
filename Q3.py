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

Procedure: Firstly, I created a user define functions called color_nodes for calculating graph 
coloring by Welch-Powell’s algorithm and should be used ‘def’ for definition keyword before 
function name for created this. This function contained one parameter ‘graph’.
After that, I created an empty list and assigned with a variable named color_map under the 
function. Again, I created a ‘for’ loop for consider nodes in descending degree (most neighbors 
into least neighbors) using sorted function that’s received three parameters such as iterable 
objects(list), lambda function, reverse method. Here iterable object is graph, ‘lambda’ is an 
anonymous function that calculated length of graph using len() function. Inside this ‘for’ loop I 
used a comprehension list for calculated neighbor colors and assigned the appropriate result with 
a variable named neighbor_colors as a set. Then I also used a next function. Inside the next function 
I created a comprehension list which contained an ‘if’ statement that checked the condition “color 
not in neighbor_colors” and assigned the appropriate result with a variable named color_map. 
Finally, I returned the result of color_map.
After that, I created a dictionary for stored the adjacent list and assigned this dictionary with a 
variable named graph. Dictionary are used stored the value with key of pair
