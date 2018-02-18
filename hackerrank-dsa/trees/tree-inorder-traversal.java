//tree inorder traversal hackerrank github 
//rohan kumar 108krohan oddlypoetic.com

/* you only have to complete the function given below.  
Node is defined as  

class Node {
    int data;
    Node left;
    Node right;
}

*/

void inOrder(Node root) {
    if(root.left != null) {
        inOrder(root.left);
    }
    System.out.print(root.data + " ");
    if(root.right != null) {
        inOrder(root.right);
    }
}
