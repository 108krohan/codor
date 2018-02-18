//height of binary tree hackerrank github
//rohan kumar 108krohan 
/*
class Node 
	int data;
    	Node left;
    	Node right;
*/
static int height(Node root) {

	if(root == null) {
		return -1;
        }
	return 1 + Math.max(height(root.left), height(root.right));
}
