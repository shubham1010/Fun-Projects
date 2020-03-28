#include "struct.h"

extern const int height(AVL *node);
extern const int max(const int a, const int b);

extern AVL *leftRotate(AVL *Y) {
	AVL *X = Y->right;
	AVL *W = X->left;

	X->left = Y;
	Y->right = W;

	Y->height = max(height(Y->left),height(Y->right)) + 1;
	X->height = max(height(X->left),height(X->right)) + 1;


	return X;
}
