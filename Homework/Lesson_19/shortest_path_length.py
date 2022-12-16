from networkx import shortest_path, shortest_path_length, Graph


def shortest_path_and_length(g, start_node, target_node):
	w = 'weight'
	return f'Path: {shortest_path(g, start_node, target_node, weight=w)}',\
		   f'Length: {shortest_path_length(g, start_node, target_node, weight=w)}'


with open('cities.csv') as file:
	cities = [line.rstrip().split(';') for line in file]

graph = Graph()
for path in cities:
	graph.add_edge(path[0], path[1], weight=int(path[2]))

print(shortest_path_and_length(graph, 'Netishyn', 'Ternopil'))
print(shortest_path_and_length(graph, 'Rozdilna', 'Siversk'))