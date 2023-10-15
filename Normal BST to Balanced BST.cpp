Node*buildTree(vector<int>&v, int start, int end) {
        if(start > end) return NULL;
        int mid = (start + end) / 2;
        Node*root = new Node(v[mid]);
        root->left = buildTree(v,start,mid-1);
        root->right = buildTree(v,mid+1,end);
        return root;
    }
    void inorder(Node*root, vector<int>&v) {
        if(!root) return;
        inorder(root->left,v);
        v.push_back(root->data);
        inorder(root->right,v);
    }

class Solution{
    
    public:
    // Your are required to complete this function
    // function should return root of the modified BST
    Node* buildBalancedTree(Node* root)
    {
    	// Code here
    	 vector<int>v;
        inorder(root,v);
        root = buildTree(v,0,v.size()-1);
        return root;
    }
};
