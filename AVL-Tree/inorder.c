#include "struct.h"
#include<stdio.h>

extern void inorder(AVL *root) {
	if(root) {
		inorder(root->left);
		printf("\n%d having height %d",root->data,root->height);
		inorder(root->right);
	}
	
}
