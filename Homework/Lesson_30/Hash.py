from hashlib import md5
from sys import stderr


class HashTable:
	def __init__(self, size: int, dict_=None):
		self.__hashtable = dict()
		for i in range(size):
			self.__hashtable[f'hash_{i}'] = None
		if dict_:
			for i in dict_:
				self.add(dict_[i])

		self.size = len(self.__hashtable)
		self.__removed_hash = list()

	def add(self, val: str):
		val_hash = md5(bytes(val, 'UTF-8')).hexdigest()
		if val_hash in self.__hashtable:
			if isinstance(self.__hashtable[val_hash], str):
				self.__hashtable[val_hash] = [self.__hashtable[val_hash], val]
			elif isinstance(self.__hashtable[val_hash], list):
				self.__hashtable[val_hash].append(val)
		else:
			for i in self.__hashtable:
				if self.__hashtable[i] is None:
					del self.__hashtable[i]
					self.__removed_hash.append(i)
					self.__hashtable[val_hash] = val
					break
			else:
				print('HashTab is full, cannot add more hashes!', file=stderr)

	def remove(self, val: str):
		if isinstance(self.__hashtable[md5(bytes(val, 'UTF-8')).hexdigest()], str):
			del self.__hashtable[md5(bytes(val, 'UTF-8')).hexdigest()]
			self.__hashtable[self.__removed_hash.pop()] = None
		else:
			self.__hashtable[md5(bytes(val, 'UTF-8')).hexdigest()].remove(val)
			self.__hashtable[self.__removed_hash.pop()] = None

	def find(self, val):
		if md5(bytes(val, 'UTF-8')).hexdigest() in self.__hashtable:
			if self.__hashtable[md5(bytes(val, 'UTF-8')).hexdigest()] == val:
				return True
			elif isinstance(self.__hashtable[md5(bytes(val, 'UTF-8')).hexdigest()], list) and val in self.__hashtable[md5(bytes(val, 'UTF-8')).hexdigest()]:
				return True
		else:
			return False

	def __getitem__(self, item):
		return self.__hashtable[item]

	def print_hash_table(self):
		for k, v in self.__hashtable.items():
			if v is not None:
				print(k, ': ', v, sep='')
