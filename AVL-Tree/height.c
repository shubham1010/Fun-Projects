#include "struct.h"

extern const int height(AVL *node) {
	if(!node)
		return -1;
	return (node->height);
}
