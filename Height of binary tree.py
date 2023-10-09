class Solution{
    public:
    int findHeight(Node * node){
        if(node == nullptr)
            return 0;
            
        int left = findHeight(node -> left);
        int right = findHeight(node -> right);
        
        return max(left, right) + 1;
    }
    
    //Function to find the height of a binary tree.
    int height(struct Node* node){
        // code here 
        return findHeight(node);
    }
};
