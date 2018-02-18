//tree preorder traversal hackerrank github 
//rohan kumar 108krohan oddlypoetic.com
/*
class Node {
    int data;
    Node left;
    Node right;
}
*/

void preOrder(Node root) {
    System.out.print(root.data + " ");
    if(root.left != null) {
         preOrder(root.left);
    }
    if(root.right != null) {
         preOrder(root.right);
    }
}
