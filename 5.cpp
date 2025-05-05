#include <iostream>
using namespace std;
struct Node {
int data;
Node* left;
Node* right;
bool rightThread;
Node(int val) {
data = val;
left = right = nullptr;
rightThread = false;
}
};
Node* insert(Node* root, int key) {
if (!root) return new Node(key);
Node* curr = root;
while (curr) {
if (key < curr->data) {
if (!curr->left) {
curr->left = new Node(key);
return root;
}
curr = curr->left;
} else {
if (!curr->right) {
curr->right = new Node(key);
return root;
}
curr = curr->right;
}
}
return root;
}
// Function to convert binary tree to threaded binary tree
void convertToThreadedBinaryTree(Node* root) {
if (!root) return;Node* prev = nullptr;
Node* curr = root;
while (curr) {
if (!curr->left) {
if (prev) {
prev->right = curr;
prev->rightThread = true;
}
prev = curr;
curr = curr->right;
} else {
Node* pre = curr->left;
while (pre->right && pre->right != curr) {
pre = pre->right;
}
if (!pre->right) {
pre->right = curr;
pre->rightThread = false;
curr = curr->left;
} else {
pre->right = nullptr;
pre->rightThread = true;
if (prev) {
prev->right = curr;
prev->rightThread = true;
}
prev = curr;
curr = curr->right;
}
}
}
}
// Inorder traversal of threaded binary tree
void inorder(Node* root) {
Node* curr = root;
while (curr) {
while (curr->left) {
curr = curr->left;
}
cout << curr->data << " ";while (curr->rightThread) {
curr = curr->right;
cout << curr->data << " ";
}
curr = curr->right;
}
cout << endl;
}
int main() {
Node* root = nullptr;
root = insert(root, 45);
root = insert(root, 20);
root = insert(root, 65);
root = insert(root, 15);
root = insert(root, 35);
root = insert(root, 50);
root = insert(root, 85);
convertToThreadedBinaryTree(root);
cout << "Inorder Traversal of Threaded Binary Tree: ";
inorder(root);
return 0;
}
