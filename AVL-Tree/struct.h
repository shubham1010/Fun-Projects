typedef struct AVL_Tree_Struct {
	int data ; // we are using integer as a data for a node
	struct AVL_Tree_Struct *left,*right;
	unsigned int height;
}AVL;
