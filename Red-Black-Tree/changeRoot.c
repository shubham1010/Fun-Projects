#include "struct.h"

extern void changeRoot(RBT **node) {
	if (*node) {
		if ((*node)->isRoot)
			(*node)->isRoot = 0;
		else
			(*node)->isRoot = 1;
	}
}
