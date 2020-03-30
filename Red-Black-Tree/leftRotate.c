#include "struct.h"


extern RBT *leftRotate(RBT *Y) {
	RBT *X = Y->right;
	RBT *W = X->left;

	X->left = Y;
	Y->right = W;

	return X;
}
