import unittest
from src import BSGraph

class Test_displayMovieOfActor(unittest.TestCase):
	obj=BSGraph()
	obj.readActMovFile("inputPS2.txt")

	def test_Valid_Actor_Name(self):
		assert self.obj.displayMoviesOfActor("Aamir Khan"),"Incorrect Test"
	def test_Invalid_Actor_Name(self):
		assert self.obj.displayMoviesOfActor("XYZ")==False,"Incorrect Test"
	def test_Type(self):
		try:
			result=self.obj.displayMoviesOfActor([]),"Checking Type Test Failed"
			result=self.obj.displayMoviesOfActor(545),"Checking Type Test Failed"
			result=self.obj.displayMoviesOfActor(12.20),"Checking Type Test Failed"
		except Exception as e:
			assert isinstance(e,TypeError)
	
