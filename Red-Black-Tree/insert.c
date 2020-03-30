#include "struct.h"

unsigned int rCnt=1;

extern RBT *newNode(const int data);
extern RBT *leftRotate(RBT *root);
extern RBT *rightRotate(RBT *root);
extern Color givesParentSiblingColor(RBT *root, const int data);
extern void recolor(RBT **node);
extern void changeRoot(RBT **node);
extern unsigned int isRootOfTree(RBT *node);

extern RBT *insert(RBT *root, const int data) {
	if (!root)
		return newNode(data);
	else if (data < root->data)
		root->left = insert(root->left, data);
	else if (data > root->data)
		root->right = insert(root->right, data);

	if (rCnt == 2) { // if parent of newNode has red color
		rCnt = 1;
		if (givesParentSiblingColor(root, data) == black) { // rotation
			recolor(&root);
			if (root->left && data < root->left->data) {
				recolor(&(root->left));

				if (isRootOfTree(root)) {
					changeRoot(&root);
					changeRoot(&(root->left));
				}
				return rightRotate(root);
			}
		

			if (root->right && data > root->right->data) {
				recolor(&(root->right));

				if(isRootOfTree(root)) {
					changeRoot(&root);
					changeRoot(&(root->right));
				}

				return leftRotate(root);
			}

			if (root->left && data > root->left->data) {
				root->left = leftRotate(root->left);
				recolor(&(root->left));

				if(isRootOfTree(root)) {
					changeRoot(&root);
					changeRoot(&(root->left));
				}

				return rightRotate(root);
			}

			if (root->right && data < root->right->data) {
				root->right = rightRotate(root->right);
				recolor(&(root->right));
				if (isRootOfTree(root)) {
					changeRoot(&root);
					changeRoot(&(root->right));
				}

				return leftRotate(root);
			}
		}
		else { // recoloring

			recolor(&(root->left));
			recolor(&(root->right));

			if (!isRootOfTree(root))
				recolor(&root);

			return root;
		
		}
	}
	
	if (root->color == red)
		rCnt += 1;

	return root;
}
