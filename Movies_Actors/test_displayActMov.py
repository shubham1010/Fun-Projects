import unittest
from src import BSGraph

class Test_displayActMov(unittest.TestCase):
	obj=BSGraph()
	def test_TypeError(self):
		try:
			self.obj.readActMovFile("inputPS2.txt")
			if self.obj.ActMov!=[] and self.obj.edges!=[]:
				assert self.obj.displayActMov(),"Type Test Failed"
			else:
				raise ValueError()
		except Exception as e:
			assert isinstance(e,ValueError)
		except Exception as e:
			assert isinstance(e,TypeError)
	def test_ValueError(self):
		assert self.obj.displayActMov(),"Value Test Failed"
