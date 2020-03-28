#include<stdio.h>
#include "struct.h"

extern AVL *insert(AVL *root, int data);
extern void inorder(AVL *root);
extern void deleteTree(AVL **root);
extern AVL *deleteNode(AVL *node, const int data);
extern const int search(AVL *root, const int data);

int main(void) {
	AVL *root=NULL;
	int data,ch;

	while(1) {
		printf("\n_____________________________________________________");
		printf("\n1: Insert node\n2: Inorder\n3: Delete node\n4: Search node\n5: Exit");
		printf("\n______________________________________________________");
		printf("\nEnter your choice: ");
		scanf("%d",&ch);

		if(ch==5)
			break;

		switch(ch) {
			case 1:
				printf("\nEnter integer data for a node: ");
				scanf("%d",&data);

				root = insert(root,data);
				break;
			
			case 2:
				inorder(root);
				break;
			
			case 3:
				printf("\nEnter data to delete node: ");
				scanf("%d",&data);
				
				if(root)
					root = deleteNode(root,data);
				else
					printf("\n\t\t*** Tree is already empty..!! ***");
				break;

			case 4:
				printf("\nEnter searching element: ");
				scanf("%d",&data);

				if(search(root,data))
					printf("\n\t\t *** %d is present in a tree ***",data);
				else
					printf("\n\t\t *** %d is not present in a tree ***",data);
		}
	}
	deleteTree(&root);

	if(!root)
		printf("\n\t\t *** Tree is successfully deleted..! ***");
}
