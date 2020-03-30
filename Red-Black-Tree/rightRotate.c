#include "struct.h"


extern RBT *rightRotate(RBT *X) {
	RBT *Y = X->left;
	RBT *W = Y->right;

	Y->right = X;
	X->left = W;

	return Y;
}
