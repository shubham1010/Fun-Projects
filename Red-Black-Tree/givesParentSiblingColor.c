#include "struct.h"
extern Color givesParentSiblingColor(RBT *root, const int data) {
	if (data > root->data)
		return ((root->left)?root->left->color:black);
	else
		return ((root->right)?root->right->color:black);
		
}
