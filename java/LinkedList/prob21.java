/*21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution 
{
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) 
    {
        if(list1==null)
            return list2;
        if(list2==null)
            return list1;
        ListNode head;
        ListNode temp;
        if(list1.val<list2.val)
        {
            temp=head=new ListNode(list1.val);
            list1=list1.next;
        }
        else
        {
            temp=head=new ListNode(list2.val);
            list2=list2.next;
        }
        while(list1!=null && list2!=null)
        {
            if(list1.val<list2.val)
            {
                temp.next=new ListNode(list1.val);
                list1=list1.next;
            }
            else
            {
                temp.next=new ListNode(list2.val);
                list2=list2.next;
            }
            temp=temp.next;
        }
        while(list1!=null)
        {
            temp.next=new ListNode(list1.val);
            list1=list1.next;
            temp=temp.next;
        }
        while(list2!=null)
        {
            temp.next=new ListNode(list2.val);
            list2=list2.next;
            temp=temp.next;
        }
        return head;
    }
}
