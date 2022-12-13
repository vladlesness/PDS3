import networkx as nx
import matplotlib.pyplot as plot

city_list = [['Mannheim', 'Frankfurt', 85], ['Mannheim', 'Karlsruhe', 80], ['Erfurt', 'Wurzburg', 186],
			['Munchen', 'Numberg', 167], ['Munchen', 'Augsburg', 84], ['Munchen', 'Kassel', 502],
			['Numberg', 'Stuttgart', 183], ['Numberg', 'Wurzburg', 103], ['Numberg', 'Munchen', 167],
			['Stuttgart', 'Numberg', 183], ['Augsburg', 'Munchen', 84], ['Augsburg', 'Karlsruhe', 250],
			['Kassel', 'Munchen', 502], ['Kassel', 'Frankfurt', 173], ['Frankfurt', 'Mannheim', 85],
			['Frankfurt', 'Wurzburg', 217], ['Frankfurt', 'Kassel', 173], ['Wurzburg', 'Numberg', 103],
			['Wurzburg', 'Erfurt', 186], ['Wurzburg', 'Frankfurt', 217], ['Karlsruhe', 'Mannheim', 80],
			['Karlsruhe', 'Augsburg', 250]]

graph = nx.Graph()
for path in city_list:
	graph.add_edge(path[0], path[1], weight=path[2])

pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos)
plot.title("Cities")
plot.show()

print(nx.shortest_path(graph, 'Mannheim', 'Kassel', weight='weight'),
	  nx.shortest_path_length(graph, 'Mannheim', 'Kassel', weight='weight'))
print(nx.shortest_path(graph, 'Munchen', 'Erfurt', weight='weight'),
	  nx.shortest_path_length(graph, 'Munchen', 'Erfurt', weight='weight'))
print(nx.shortest_path(graph, 'Stuttgart', 'Karlsruhe', weight='weight'),
	  nx.shortest_path_length(graph, 'Stuttgart', 'Karlsruhe', weight='weight'))