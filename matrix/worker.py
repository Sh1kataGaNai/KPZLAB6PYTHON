from functools import reduce

class Worker:
	def execute(self):
		raise NotImplementedError

class MultiplicationColsWorker(Worker):
	def __init__(self, matrix):
		self.matrix = matrix

	def execute(self):
		self.results = []
		for col in zip(*self.matrix):
			self.results.append(reduce(lambda a, x: a * x, col))
		return self.results

