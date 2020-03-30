#include "struct.h"

extern void recolor(RBT **node) {
	if(*node) {
		if ((*node)->color == black)
			(*node)->color =red;
		else
			(*node)->color = black;
	}
}
