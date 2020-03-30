#include "struct.h"

unsigned int isRootOfTree(RBT *node) {
	if (node)
		return (node->isRoot);
	return 0;
}
