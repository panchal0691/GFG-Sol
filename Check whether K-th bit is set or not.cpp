
class Solution
{
    public:
    // Function to check if Kth bit is set or not.
    bool checkKthBit(int n, int k)
    {
        // Your code here
        return (n >> k) & 1;
        // It can be a one liner logic!! Think of it!!
    }
};
