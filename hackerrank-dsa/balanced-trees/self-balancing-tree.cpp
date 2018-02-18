#include <iostream>

#include <algorithm>

using namespace std;

int height (node * root) {
	int height = -1;
	if (root != NULL) {
		height = root->ht;
	}
	
	return height;
}

void update_height(node *root) {
	if (root != NULL) {
		root->ht = max(height(root->left), height(root->right)) + 1;
	}
}

int balance_factor(node * root) {
	int balance_factor = 0;
	
	if (root != NULL) {
		balance_factor = height(root->left) - height(root->right);
	}
	
	return balance_factor;
}

void fix_left(node * root) {
	//no_use.
}

node * rotate_left(node *root) {
	
	node *old_root = root;
	root = old_root->right;
	old_root->right = root->left;
	root->left = old_root;
	
	update_height(root->left);
	update_height(root->right);
	update_height(root);
	return root;
}

node * rotate_right(node * root) {
	
	node *old_root = root;
	root = old_root->left;
	old_root->left = root->right;
	root->right = old_root;
	
	update_height(root->left);
	update_height(root->right);
	update_height(root);
	return root;
}

node * rotate(node * root) {
	//rotate if unbalanced.
	if (balance_factor(root) < -1) {
		if (height(root->right->right) >= height(root->right->left)) {
			//right right condition
			return rotate_left(root);
		}
		else {
			//right left condition
			root->right = rotate_right(root->right);
			return rotate_left(root);
		}
	}
	else if (balance_factor(root) > 1) {
		if (height(root->left->left) >= height(root->left->right)) {
			//left left condition
			return rotate_right(root);
		}
		else {
			//left right condition
			root->left = rotate_left(root->left);
			return rotate_right(root);
		}
	}
	else {
		return root;
	}
}

node * insert (node * root, int val) {
	//insert new node.
	if (root != NULL) {
		if (val != root->val) {
			if (val < root->val) {
			root->left = insert(root->left, val);
			}
			else {
				root->right = insert(root->right, val);
			}
		
			update_height(root);
			return rotate(root);
		}
		else {
			return root;
		}
	}
	else {
		root = new node();
		root->right = NULL;
		root->left = NULL;
		root->val = val;
		return root;		
	}		
}



