class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* res = new ListNode;
        ListNode* current = res;
        int carry = 0;
        
        while (l1||l2)
        {
            int sum = carry;
            if (l1!=NULL)
            {
                sum += l1->val;
                l1 = l1->next;
            }
            
            if(l2!=NULL)
            {
                sum += l2->val;
                l2 = l2->next;
            }
            
            current->next = new ListNode(sum%10);
            current = current->next;
            carry = sum/10;
            
        }
        
        if (carry>=1)
        {
            current->next = new ListNode(carry);
        }
        
        return(res->next);
    }
};
