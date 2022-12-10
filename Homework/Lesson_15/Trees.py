class Tree:
	def __init__(self, id_node):
		self.id_node = id_node
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.id_node)

	# Insert method to create nodes
	def insert(self, id_node):
		if self.id_node:
			if id_node < self.id_node:
				if self.left is None:
					self.left = Tree(id_node)
				else:
					self.left.insert(id_node)
			elif id_node > self.id_node:
				if self.right is None:
					self.right = Tree(id_node)
				else:
					self.right.insert(id_node)
		else:
			self.id_node = id_node

	# findval method to compare the id_node with nodes
	def findval(self, find_val):
		if find_val < self.id_node:
			if self.left is None:
				return str(find_val) + " Not Found"
			return self.left.findval(find_val)
		elif find_val > self.id_node:
			if self.right is None:
				return str(find_val) + " Not Found"
			return self.right.findval(find_val)
		else:
			return str(self.id_node) + ' is found'

	# Print the tree
	def print_tree(self):
		if self.left:
			self.left.print_tree()
		print(self.id_node),
		if self.right:
			self.right.print_tree()

	# Create nodes from an iterable using the insert method
	def insert_nodes(self, iterable):
		for val in iterable:
			self.insert(val)

	# Find the min value element
	def find_min_node(self):
		if self.left:
			return self.left.find_min_node()
		return self

	# Find the max value element
	def find_max_node(self):
		if self.right:
			return self.right.find_max_node()
		return self

	# Remove a node
	def remove_node(self):
		if self.left and self.right:
			right_min_node = self.right.find_min_node()
			self.id_node = right_min_node.id_node
			if right_min_node.right is None:
				right_min_node.__remove_leaf()
			else:  # If right_min_node.right
				right_min_node.__remove_right_child_node()
		elif self.left and self.right is None:
			self.__remove_left_child_node()
		elif self.left is None and self.right:
			self.__remove_right_child_node()
		else:  # If self.left is None and self.right is None
			self.__remove_leaf()

	# Remove a leaf
	def __remove_leaf(self):
		del self.left
		del self.right
		self.id_node = None

	# Remove a node with only the right child
	def __remove_right_child_node(self):
		self.id_node = self.right.id_node
		self.left = self.right.left
		self.right = self.right.right

	# Remove a node with only the left child
	def __remove_left_child_node(self):
		self.id_node = self.left.id_node
		self.left = self.left.left
		self.right = self.left.right
