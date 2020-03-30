#include "struct.h"
#include <stdlib.h>

static int a=0;

extern RBT *newNode(const int data) {
	RBT *node =  (RBT *)malloc(sizeof(RBT));

	if(!node)
		exit(1); // terminate when memory is not allocate

	node->data = data;
	node->left = node->right = NULL;
	
	if(a==0) {
		node->color = black;
		node->isRoot = 1;		
	}
	else
		node->color = red;
	a+=1;
	return node;
}
