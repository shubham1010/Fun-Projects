#include "struct.h"
#include<stdlib.h>

extern void deleteTree(AVL **root) {
	if(!(*root))
		return;
	
	deleteTree(&((*root)->left));
	deleteTree(&((*root)->right));
	free(*root);
	*root=NULL;
}
