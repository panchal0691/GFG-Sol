bool same(Node * x, Node * y) {
    if((x == nullptr) ^ (y == nullptr))
        return 0;
    if((x == nullptr) and (y == nullptr))
        return 1;
        
    if(x -> data != y -> data)
        return 0;
        
    return same(x -> left, y -> left) and same(x -> right, y -> right);
}
class Solution {
  public:
    /*This function returns true if the tree contains 
    a duplicate subtree of size 2 or more else returns false*/
    int dupSub(Node *root) {
        vector<Node *> nodes;
        
        queue<Node *> q;
        q.push(root);
        
        while(!q.empty()){
            Node * cur = q.front();
            q.pop();
            
            bool leaf = 1;
            
            if(cur -> left != nullptr){
                q.push(cur -> left);
                leaf = 0;
            }
            if(cur -> right != nullptr){
                q.push(cur -> right);
                leaf = 0;
            }
            
            if(!leaf)
                nodes.push_back(cur);
        }
         
        for(int i = 0; i < nodes.size(); i++){
            for(int j = i + 1; j < nodes.size(); j++){
                if(same(nodes[i], nodes[j]))
                    return 1;
            }
        }
        
        return 0;
    }
};
