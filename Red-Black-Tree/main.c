#include<stdio.h>
#include "struct.h"

extern RBT *insert(RBT *root,const int data);
extern void inorder(RBT *root);
extern void deleteTree(RBT **root);

int main(void) {
	RBT *root=NULL;
	int ch, data;

	while(1) {
		printf("\n____________________________________________________");
		printf("\n1: Insert\n2: Inorder\n3: Delete Tree\n4: Exit");
		printf("\n____________________________________________________");
		printf("\nEnter your choice: ");
		scanf("%d",&ch);

		if(ch==4)
			break;

		switch(ch) {
			case 1:
				printf("\nEnter data for node: ");
				scanf("%d",&data);
				root = insert(root,data);
				break;
			
			case 2:
				inorder(root);
				break;
			
			case 3:
				deleteTree(&root);
				break;
			default:
				printf("\nPlease choose the valid options");
		}
	}
	deleteTree(&root);
}
