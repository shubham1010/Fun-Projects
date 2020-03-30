typedef enum {red,black} Color;

typedef struct Struct_For_Red_Black_Tree {
	int data ; // assuming input data is going to be an integer
	unsigned int isRoot; // whether node is root node or not
	struct Struct_For_Red_Black_Tree *left, *right;
	Color color;
}RBT;
