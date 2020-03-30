#include "struct.h"
#include <stdlib.h>

extern void deleteTree(RBT **root) {
	if(*root) {
		deleteTree(&((*root)->left));
		deleteTree(&((*root)->right));

		free(*root);
	}
	*root=NULL;
}
