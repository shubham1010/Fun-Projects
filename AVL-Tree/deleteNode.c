#include "struct.h"
#include<stdlib.h>

extern const int height(AVL *node);
extern const int getBalanceFactor(AVL *node);
extern AVL *rightRotate(AVL *X);
extern AVL *leftRotate(AVL *Y);
extern const int getInorderPredecessor(AVL *node);
extern const int max(const int a, const int b);

extern AVL *deleteNode(AVL *root, const int data) {
	if (!root)
		return root;
	else if (data < root->data) 
		root->left = deleteNode(root->left,data);
	else if (data > root->data) 
		root->right = deleteNode(root->right,data);
	else {
		if(!root->left || !root->right) {
			AVL *temp = root->left ? root->left : root->right;
			if (!temp) { // doesn't has child
				temp = root;
				root = NULL;
			}
			else	// has only one child
				*root = *temp;
			free(temp);
		}
		else { // has 2 childs
			const int inPreData = getInorderPredecessor(root->left);

			root->data = inPreData;

			root->left = deleteNode(root->left,inPreData);
		}

	}
	
	if(root==NULL)
		return root;

	root->height = max(height(root->left),height(root->right)) + 1;

	int balance = getBalanceFactor(root);

	if (balance < -1 && getBalanceFactor(root->right) <= 0)
		return leftRotate(root);
	
	if (balance < -1 && getBalanceFactor(root->right) > 0 ) {
		root->right = rightRotate(root->right);
		return leftRotate(root);
	}

	if (balance > 1 && getBalanceFactor(root->left) >= 0)
		return rightRotate(root);

	if (balance > 1 && getBalanceFactor(root->left) <0) {
		root->left = leftRotate(root->left);
		return rightRotate(root);
	}

	return root;
}
