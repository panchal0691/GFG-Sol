class Solution{
  public:
    // your task is to complete this function
    int countPairs(struct Node* head1, struct Node* head2, int x)
    {
        vector<int>ans1, ans2;
        while(head1!=nullptr)
        {
            ans1.push_back(head1->data);
            head1=head1->next;
        }
        while(head2!=nullptr)
        {
            ans2.push_back(head2->data);
            head2=head2->next;
        }
        sort(ans1.begin(), ans1.end());
        sort(ans2.begin(), ans2.end());
        int low=0, high=ans2.size()-1, count=0;
        while (low<ans1.size() && high>=0)
        {
            if (ans1[low]+ans2[high]==x)
            {
                count++;
                low++;
                high--;
            }
            else if (ans1[low]+ans2[high]>x)
                high--;
            else low++;
        }
        return count;
    }
};
