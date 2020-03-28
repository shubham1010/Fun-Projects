CC=gcc
TARGET=main
DEPS=struct.h
CFLAG=-Wall
OBJ= main.o newNode.o inorder.o deleteTree.o insert.o rightRotate.o leftRotate.o getBalanceFactor.o height.o max.o deleteNode.o getInorderPredecessor.o search.o

%.o: %.c
	$(CC) $(CFLAG) -c -o $@ $<

main: $(OBJ)
	$(CC) $(CFLAG) -o $@ $^

clean: $(OBJ)
	rm $(OBJ)

install:
	sudo apt-get install make -y && sudo apt install build-essential -y
