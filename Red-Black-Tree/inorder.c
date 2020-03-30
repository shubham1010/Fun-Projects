#include "struct.h"

extern void formatedPrint(RBT *root);

extern void inorder(RBT *root) {
	if(root) {
		inorder(root->left);
		formatedPrint(root);
		inorder(root->right);
	}
}
