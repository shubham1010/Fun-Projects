#include "struct.h"

extern const int height(AVL *node);

extern const int getBalanceFactor(AVL *node) {
	if(!node)
		return 0;
	return (height(node->left))-height(node->right);
}
