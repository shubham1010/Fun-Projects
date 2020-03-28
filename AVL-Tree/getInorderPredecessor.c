#include "struct.h"

extern const int getInorderPredecessor(AVL *root) {
	while (root && root->right) 
		root = root->right;
	
	return root->data;
}
