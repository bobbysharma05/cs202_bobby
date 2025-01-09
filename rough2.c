#include<stdio.h>
#include<stdlib.h>

typedef struct BST {
    int data;
    struct BST *left;
    struct BST *right;
}BST;

int numberOfNodes(BST *root) {
    if(root == NULL) {
        return 0;
    }
    return (1 + numberOfNodes(root -> left) + numberOfNodes(root -> right));
}

int sumOfContentOfNodes(BST *root) {
    if(root == NULL) {
        return 0;
    }
    return (root -> data + sumOfContentOfNodes(root -> left) + sumOfContentOfNodes(root -> right));
}

int depthOfHeight(BST *root) {
    if(root == NULL) {
        return 0;
    }
    int left = depthOfHeight(root -> left);
    int right = depthOfHeight(root -> right);
    return (left > right ? left : right) + 1;
}

