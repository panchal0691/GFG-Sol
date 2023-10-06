*/
class Solution
{
    public:
    void rearrange(struct Node *odd)
    {
        //add code here
         if(odd == nullptr)
            return;
            
        if(odd -> next == nullptr)
            return;
        
        Node * prev, *cur, *last;
        prev = odd;
        cur = odd -> next;
        last = nullptr;
        
        while(cur != nullptr){
            prev -> next = cur -> next;
            
            if(cur -> next != nullptr){
                Node * temp = cur -> next -> next;
                cur -> next = last;
                last = cur;
                prev = prev -> next;
                
                if(temp == nullptr)
                    break;
                    
                cur = temp;
            }
            else{
                cur -> next = last;
                last = cur;
                break;
            }
        }
        
        prev -> next = cur;
    }
    
};
