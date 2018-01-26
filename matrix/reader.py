import pickle

class Reader:
	def read(self):
		raise NotImplementedError
	def size(self):
		raise NotImplementedError

class ReaderPickle(Reader):
	def __init__(self, filename):
		self.filename = filename

	def read(self):
		with open(self.filename, 'rb') as src:
			self.matrix = pickle.load(src)
			return self.matrix
	def size(self):
		return tuple([len(self.matrix), len(self.matrix[0])])

		


			






