CC=gcc
CFLAG=-Wall
OBJ= main.o inorder.o newNode.o insert.o formatedPrint.o deleteTree.o changeRoot.o givesParentSiblingColor.o isRootOfTree.o leftRotate.o recolor.o rightRotate.o whichColor.o

%.o: %.c
	$(CC) $(CFLAG) -c -o $@ $<

main: $(OBJ)
	$(CC) $(CFLAG) -o $@ $^

clean:
	rm $(OBJ)
