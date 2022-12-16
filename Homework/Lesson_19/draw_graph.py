import networkx as nx
import matplotlib.pyplot as plot

with open('cities.csv') as file:
	cities = [line.rstrip().split(';') for line in file]

graph = nx.Graph()
for path in cities:
	graph.add_edge(path[0], path[1], weight=int(path[2]))

pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos)
plot.title('Cities')
plot.show()