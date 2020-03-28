#include "struct.h"

extern const int height(AVL *node);
extern const int max(const int a, const int b);

extern AVL *rightRotate(AVL *X) {
	AVL *Y = X->left;
	AVL *W = Y->right;

	Y->right = X;
	X->left = W;

	X->height = max(height(X->left),height(X->right)) + 1;
	Y->height = max(height(Y->left),height(Y->right)) + 1;

	return Y;
}
