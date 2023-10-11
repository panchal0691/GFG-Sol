unordered_map<Node *, int> height;

class Solution{
    public:
    //Function to check whether a binary tree is balanced or not.
    bool isBalanced(Node *root)
    {
        if(root == nullptr){
            height[root] = 0;
            return 1;
        }
        
        bool ok = isBalanced(root -> left) and isBalanced(root -> right);
        int left = height[root -> left];
        int right = height[root -> right];
        height.erase(root -> left);
        height.erase(root -> right);
        
        ok = ok and (abs(left - right) <= 1);
        height[root] = max(left, right) + 1;
        
        return ok;
    }
};
