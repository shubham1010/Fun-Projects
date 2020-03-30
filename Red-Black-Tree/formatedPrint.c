#include "struct.h"
#include <stdio.h>

extern void formatedPrint(RBT *root) {
	printf("\n\t\t *** %d with its color",root->data);

	if(root->color==0)
		printf(" red ");
	else
		printf(" black ");
	
	printf("isParent = %d ***", root->isRoot);
}
