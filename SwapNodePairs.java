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


// Given a linked list, swap every two adjacent nodes and return its head.
    
    
public class Solution {
    public ListNode swapPairs(ListNode head) {
      if(head==null) return null; 
      if(head.next==null) return head; 
      ListNode p=null; 
      ListNode c=head; 
      ListNode NodeLooper=head.next; 
      while(NodeLooper!=null && NodeLooper!=c)
      {
        c.next=NodeLooper.next; 
        NodeLooper.next=c; 
        if(p==null)
        {
          p=NodeLooper; 
          head=p; 
          p=p.next; 
        }else
        {
          p.next=NodeLooper; 
          p=p.next.next; 
        }
        c=c.next;
        if(c==null) break; 
        NodeLooper=NodeLooper.next.next.next; 
         
      }
      return head; 
    }
}
