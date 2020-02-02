import unittest
from src import BSGraph

class Test_readActMovFile(unittest.TestCase):
	obj=BSGraph()
	def test_readingInputFile(self):
		assert self.obj.readActMovFile("inputPS2.txt"),"Reading Input Test Failed"
	def test_TypeError(self):
		try:
			assert self.obj.readActMovFile(1244),"Checking Integer Type Test Failed"
			assert self.obj.readActMovFile(134.3),"Checking Floating Type Test Failed"
			assert self.obj.readActMovFile([]),"Checking List Type Test Failed"
		except Exception as e:
			assert isinstance(e,TypeError)
	def test_FileNotFound(self):
		try:
			assert self.obj.readActMovFile("unknownfile"),"Checking File-Not-Found Test Failed"
		except Exception as e:
			assert isinstance(e,FileNotFoundError)
