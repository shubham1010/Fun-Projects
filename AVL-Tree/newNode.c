#include<stdlib.h>
#include "struct.h"

extern AVL *newNode(int data) {
	AVL *node = (AVL *)malloc(sizeof(AVL));
	node->data = data;
	node->left = NULL;
	node->right = NULL;

	return node;
}
