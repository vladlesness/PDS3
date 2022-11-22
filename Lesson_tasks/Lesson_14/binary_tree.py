from binarytree import *
from random import randint


nodes = [randint(20, 30), randint(5, 10), randint(30, 40), randint(0, 5), randint(10, 15), None, randint(40, 50),
         None, None, randint(5, 10), randint(15, 20), None, None, randint(50, 60), None]
# Building the binary tree
binary_tree = build()
print('Binary tree from list :\n', binary_tree)
print('Tree Properties:\n', binary_tree.properties)