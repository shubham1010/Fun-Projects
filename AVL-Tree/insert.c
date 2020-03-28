#include "struct.h"

extern AVL *newNode(int data);
extern const int getBalanceFactor(AVL *node);
extern const int height(AVL *node);
extern const int max(const int a,const int b);
extern AVL *rightRotate(AVL *X);
extern AVL *leftRotate(AVL *Y);

extern AVL *insert(AVL *root, int data) {
	if(!root)
		return newNode(data);
	else if(data < root->data)
		root->left = insert(root->left,data);
	else if(data > root->data)
		root->right = insert(root->right,data);

	root->height = max(height(root->left),height(root->right)) + 1;

	int balance = getBalanceFactor(root);

	if(balance > 1 && data < root->left->data)
		return rightRotate(root);
	
	if(balance > 1 && data > root->left->data) {
		root->left = leftRotate(root->left);
		return rightRotate(root);
	}

	if(balance < -1 && data > root->right->data)
		return leftRotate(root);
	
	if(balance < -1 && data < root->right->data) {
		root->right = rightRotate(root->right);
		return leftRotate(root);
	}
	
	root->height = max(height(root->left),height(root->right)) + 1;

	return root;
}
