import string
import re
import os.path
from os import path

class BSGraph:
	ActMov=[]
	edges = [[],[]]

	def __init__(self):
		self.ActMov=[]
		self.edges=[]

	def readActMovFile(self,fname):
		try:
			if type(fname)!=str:
				raise TypeError()
			if path.exists(fname):
				with open(fname,"r") as f:
					while True:
						line=f.readline()
						line=re.split('/',line)

						if line==['']:
							break
						i=0
						if len(line)>1:
							for l in line:
								if len(l)>1:
									line[i]=l.strip()
								i+=1
							self.edges+=[[line[0]]]+[line[1:]]
							self.ActMov+=line
				
				# list containing actors and movies
				self.ActMov=list(set(self.ActMov))

				# integer matrix indicating edges between actors and movies
				# This matrix is created in a such a way that
				# the movie name will be always to it's even indexing and list of actors in it's odd indexing
				# type= [[movie id],[actorid1,actorid2...]]
				# the id's(integer) is nothing but the indices of the movie name or actor name from ActMov list.
				self.edges=list(map(lambda x:list(map(lambda y: self.ActMov.index(y),x)),self.edges))
				return True
				#self.edges=list(set(self.edges))
				#print("\nActMov:",self.ActMov)
				#print("\n\nEdges:",self.edges)
			else:
				raise FileNotFoundError("Input File is not exists")
		except TypeError:
			raise TypeError("Invalid Type, File name should be in string format..!!")

	def displayActMov(self):
		try:
			mlist=[]
			alist=[]
			mindex=list(filter(lambda x: self.edges.index(x)%2==0,self.edges))
			aindex=list(filter(lambda x: self.edges.index(x)%2!=0,self.edges))
			for i in mindex:
				mlist+=i
		
			for i in aindex:
				alist+=i
			alist=list(set(alist))

			mlist=list(set(mlist))
			alist=list(set(alist))
			totnoMov=len(mlist)
			totnoAct=len(alist)
			strMovCnt="Total Number of Movies: "+str(totnoMov)+'\n'
			strActCnt="Total Number of Actors: "+str(totnoAct)+'\n'
			with open("outputPS2.txt","w") as f:
				f.write("--------Function displayActMov--------\n")
				f.write(strMovCnt)
				f.write(strActCnt)
				f.write("List of Movies:\n")
				for i in mlist:
					f.write(self.ActMov[i])
					f.write("\n")

				f.write("List of Actors:\n")
				for i in alist:
					f.write(self.ActMov[i])
					f.write("\n")
				f.write("-----------------------------------------\n\n")
			print("\n***outputPS2.txt File is successfully created***\n\n")
			return True
		except TypeError:
			raise TypeError("Invalid Type")
		except ValueError:
			raise ValueError("Value is invalid")

	def displayMoviesOfActor(self,actor):
		try:
			if type(actor)!=str:
				raise TypeError()
			if actor=="":
				raise ValueError()
			aid=self.ActMov.index(actor)
			i=1
			l=len(self.edges)
			with open("outputPS2.txt","a") as f:
				f.write("\n--------Function displayMoviesOfActor-------- ")
				f.write("\nActor Name: ")
				f.write(self.ActMov[aid])
				f.write("\n")
				f.write("List of Movies:\n")
				while i<l:
					if aid in self.edges[i]:
						index=self.edges[i-1]
						f.write(self.ActMov[index[0]])
						f.write("\n")
					i+=2
				f.write("-----------------------------------------\n\n")
			print("\n***outputPS2.txt File is successfully appended***")
			print("***For displayMoviesOfActor function***\n\n")
			return True
		except TypeError:
			raise TypeError("Expected Type String,got {}".format(type(actor)))
		except ValueError:
			with open("outputPS2.txt","a") as f:
				f.write("\n--------Function displayMoviesOfActor-------- ")
				f.write("\nValueError: ")
				f.write("Actor name '")
				f.write(actor)
				f.write("' does not exist in the given records.")
				f.write("\n-----------------------------------------\n\n")
			return False


			#raise ValueError(actor," actor is not exist in given record.")

	def displayActorsOfMovie(self,movie):
		try:
			if type(movie)!=str:
				raise TypeError()
			if movie=="":
				raise ValueError()
			mid=self.ActMov.index(movie)
			i=0
			l=len(self.edges)
			actList=[]
			temp=[]
			while i<l:
				temp=self.edges[i]
				if temp[0]==mid:
					actList=self.edges[i+1]
				i+=2
			actList=list(set(actList))
			with open("outputPS2.txt","a") as f:
				f.write("\n--------Function displayActorsOfMovie --------")
				f.write("\nMovie Name: ")
				f.write(movie)
				f.write("\nList of Actors:")				
				for i in actList:
					f.write("\n")
					f.write(self.ActMov[i])

				f.write("\n-----------------------------------------\n\n")
			print("\n***File is successfully appended***")
			print("***For displayActorsOfMovie function***\n\n")
			return True
		except TypeError:
			raise TypeError("Expected Type String,got {}".format(type(movie)))
		except ValueError:
			with open("outputPS2.txt","a") as f:
				f.write("\n--------Function displayActorsOfMovie --------")
				f.write("\nValueError: ")
				f.write("Movie name '")
				f.write(movie)
				f.write("' does not exist in the given records.")
				f.write("\n-----------------------------------------\n\n")
			return False
			#raise ValueError(movie," movie is not exist in given record.")

	def findMovieRelation(self,movA,movB):
		try:
			if type(movA)!=str or type(movB)!=str:
				raise TypeError()
			if movA=="" or movB=="":
				raise ValueError()

			midA=self.ActMov.index(movA)
			midB=self.ActMov.index(movB)
			i=0
			l=len(self.edges)
			actListA=[]
			actListB=[]
			temp=[]
			while i<l:
				temp=self.edges[i]
				if temp[0]==midA:
					actListA=self.edges[i+1]
				if temp[0]==midB:
					actListB=self.edges[i+1]
				i+=2
			actListA=list(set(actListA))
			actListB=list(set(actListB))

			result=list(filter(lambda x:x in actListB,actListA))
			rl=len(result)
			commaCnt=0
			if result!=[]:
				with open("outputPS2.txt","a") as f:
					f.write("\n--------Function findMovieRelation -------- ")
					f.write("\nMovie A: ")
					f.write(movA)
					f.write("\nMovie B: ")
					f.write(movB)
					f.write("\nRelated: Yes, ")
					for i in result:
						f.write(self.ActMov[i])
						while commaCnt<rl-1:
							f.write(', ')
							commaCnt+=1
					f.write("\n-----------------------------------------\n\n")
			else:
				with open("outputPS2.txt","a") as f:
					f.write("\n--------Function findMovieRelation -------- ")
					f.write("\nMovie A: ")
					f.write(movA)
					f.write("\nMovie B: ")
					f.write(movB)
					f.write("\nNo relation found between above movies.")
					f.write("\n-----------------------------------------\n\n")

			return True
		except TypeError:
			raise TypeError("Movie name should be in string format.")

		except ValueError:
			with open("outputPS2.txt","a") as f:
				f.write("\n--------Function findMovieRelation -------- ")
				f.write("\nMovie A: ")
				f.write(movA)
				f.write("\nMovie B: ")
				f.write(movB)
				f.write("\nValueError: One of the above movie is not found in the given records.")
				f.write("\n-----------------------------------------\n\n")
			return False
		
		
	def getActorListByMovie(self,movie):
		try:
			if type(movie)!=str:
				raise TypeError()
			mid=self.ActMov.index(movie)
			i=0
			l=len(self.edges)
			temp=[]
			while i<l:
				temp=self.edges[i]
				if temp[0]==mid:
					break
				i+=2
			if i<l:
				listOfA_id=self.edges[i+1]
				result=[]
				for i in listOfA_id:
					result+=[self.ActMov[i]]
				return result
			else:
				return []
		except TypeError:
			raise TypeError("Invalid Type. Expected String type got {}".format(movie))
		except ValueError:
			return []
			
	def getMovieListByActor(self,actor):
		try:
			if type(actor)!=str:
				raise TypeError()
			aid=self.ActMov.index(actor)
			i=1
			l=len(self.edges)
			mlist=[]
			while i<l:
				if aid in self.edges[i]:
					mlist+=self.edges[i-1]
				i+=2
			mlist=list(set(mlist))
			result=[]
			for i in mlist:
				result+=[self.ActMov[i]]
			return result
		except TypeError:
			raise TypeError("Invalid Type. String type expected got {}",format(actor))
		except ValueError:
			return []
			

	# this function can give the relation if exists for Movies having more than 2 actors.
	def findMovieTransRelation(self,movA,movB):
		try:
			if type(movA)!=str or type(movB)!=str:
				raise TypeError()
			alistA=self.getActorListByMovie(movA)
			alistB=self.getActorListByMovie(movB)
			if alistA==[] or alistB==[]:
				raise ValueError()
			mlist=[]
			for i in alistA:
				mlist+=self.getMovieListByActor(i)
			for j in alistB:
				mlist+=self.getMovieListByActor(j)
			#print("mlist above:",mlist)
			mlist=list(filter(lambda x: mlist.count(x)==2,mlist))
			mlist=list(filter(lambda x: x!=movA and x!=movB,mlist))
			mlist=list(set(mlist))
			#print("mlist below:",mlist)
			if mlist!=[]:
				mlistcnt=0
				f=[]
				for i in mlist:
					f+=[self.getActorListByMovie(i)]
				#print("f=",f)
				ractor=[]
				with open("outputPS2.txt","a") as fp:
					fp.write("\n--------Function findMovieTransRelation --------")
					for i in f:
						ractor=list(filter(lambda x: x in alistA or x in alistB,i))
						print("ractor:",ractor)
						if len(ractor)!=2:
							fp.write("\nMovie A: ")
							fp.write(movA)
							fp.write("\nMovie B: ")
							fp.write(movB)
							fp.write("\nNo Trans Relation found..!!")
							fp.write("\n-----------------------------------------\n\n")
							fp.close()
							break


						if ractor[0] in alistA and ractor[1] in alistB: 
							fp.write("\nMovie A: ")
							fp.write(movA)
							fp.write("\nMovie B: ")
							fp.write(movB)
							fp.write("\nRelated: Yes, ")
							fp.write(movA+' > ')
							fp.write(ractor[0]+' > ')
							fp.write(mlist[mlistcnt]+' > ')
							fp.write(ractor[1]+' > ')
							fp.write(movB)
							fp.write("\n-----------------------------------------\n\n")
						elif  ractor[1] in alistA and ractor[0] in alistB :
							fp.write("\nMovie A: ")
							fp.write(movA)
							fp.write("\nMovie B: ")
							fp.write(movB)
							fp.write("\nRelated: Yes, ")
							fp.write(movA+' > ')
							fp.write(ractor[1]+' > ')
							fp.write(mlist[mlistcnt]+' > ')
							fp.write(ractor[0]+' > ')
							fp.write(movB)
							fp.write("\n-----------------------------------------\n\n")
						mlistcnt+=1
			else:
				with open("outputPS2.txt","a") as fp:
					fp.write("\n--------Function findMovieTransRelation --------")

					fp.write("\nMovie A: ")
					fp.write(movA)
					fp.write("\nMovie B: ")
					fp.write(movB)
					fp.write("\nNo Trans Relation found..!!")
					fp.write("\n-----------------------------------------\n\n")
			return True
		except TypeError:
			raise TypeError("Invalid Type, String type expected.")
		except ValueError:
			with open("outputPS2.txt","a") as fp:
				fp.write("\n--------Function findMovieTransRelation --------")
				fp.write("\nMovie A: ")
				fp.write(movA)
				fp.write("\nMovie B: ")
				fp.write(movB)
				fp.write("\nValueError: One of the above movie is not found in records.")
				fp.write("\n-----------------------------------------\n\n")
			return False

	def readPromptsPS2(self,fname):
		try:
			if type(fname)!=str:
				raise TypeError()
			if path.exists(fname):	
				with open(fname,"r") as f:
					while True:
						line=f.readline()
						if line=="":
							break
						if ":" not in line:
							raise ValueError()
						line=line.split(':')
						i=0
						l=len(line)
						while i<l:
							line[i]=line[i].strip()
							i+=1
						
						if line[0]=="searchActor":
							self.displayMoviesOfActor(line[1])
						elif line[0]=="searchMovie":
							self.displayActorsOfMovie(line[1])
						elif line[0]=="RMovies":
							self.findMovieRelation(line[1],line[2])
						elif line[0]=="TMovies":
							self.findMovieTransRelation(line[1],line[2])
					return True
			else:
				raise FileNotFoundError("File does not exist in the current directory")
		except TypeError:
			raise TypeError("Invalid Type, String type expected, got {} type",type(fname))
		except ValueError:
			raise ValueError("Some lines of promptsPS2.txt file is not get seperated by colon(:)")

		
if __name__=='__main__':	
	fname=input("Enter the input file name: ")
	obj = BSGraph()
	print(obj.readActMovFile(fname))
	obj.displayActMov()
	obj.readPromptsPS2("promptsPS2.txt")
