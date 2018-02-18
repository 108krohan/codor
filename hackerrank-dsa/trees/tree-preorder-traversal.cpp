//tree preorder traversal hackerrank github 
//rohan kumar 108krohan oddlypoetic.com


/* you only have to complete the function given below.  
Node is defined as  

struct node
{
    int data;
    node* left;
    node* right;
};

*/
#include <iostream>
using namespace std;

void preOrder(node *root) {
    if (root != NULL) {
        cout << root->data << " ";
        preOrder(root->left);
        preOrder(root->right);
    }
}
