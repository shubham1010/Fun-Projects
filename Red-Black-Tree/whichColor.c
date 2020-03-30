#include "struct.h"

extern Color whichColor(RBT *node) {
	if (!node)
		return black;
	return node->color;
}
