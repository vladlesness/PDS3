from Trees import Tree

tree_gen = [48, 71, 57, 12, 67, 33, 16, 65, 15, 12, 62, 87, 98, 97, 50,
			28, 41, 17, 78, 4, 39, 84, 23, 24, 18, 39, 92, 13, 17, 96]

tree = Tree(50)
tree.insert_nodes(tree_gen)


def test_find_val_found():
	assert tree.findval(65) == '65 is found'


def test_find_val_not_found():
	assert tree.findval(5) == '5 Not Found'


def test_find_min_node():
	assert tree.find_min_node().id_node == 4


def test_find_max_node():
	assert tree.find_max_node().id_node == 98