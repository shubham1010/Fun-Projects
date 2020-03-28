#include "struct.h"

extern const int search(AVL *root, const int data) {
	if(!root)
		return 0;
	else if (data < root->data)
		return (1 && search(root->left,data));
	else if (data > root->data)
		return (1 && search(root->right,data));
	else
		return 1;
}
