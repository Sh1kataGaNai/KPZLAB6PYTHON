class MatrixAbstract:
	worker = None
	reader = None

	def set_worker(self, worker):
		self.worker = worker

	def execute_worker(self):
		if self.worker == None:
			raise NameError('Worker does not initialized')
		else:
			return self.worker.execute()

	def set_reader(self, reader):
		self.reader = reader

	def read_matrix(self ,reader):
		self.matrix = reader.read()
		self.size = reader.size()
		

	def matrix_size(self):
		return self.size

	def get_matrix(self):
		return self.matrix



class StandartMatrix(MatrixAbstract):
	def __init__(self, reader):
		self.read_matrix(reader)

class SquareMatrix(MatrixAbstract):
	def __init__(self, reader):
		self.read_matrix(reader)
		if self.size[0] != self.size[1]:
			raise NameError('Rows and cols must be equals for square matrix')
		else:
			pass


		


