# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:

# Input: head = [1], n = 1
# Output: []
    
# Example 2:

# Input: head = [1,2], n = 1
# Output: [1]
    
    

class Solution:
    def removeNthFromEnd(self, head, n):
        deer_pointer = tortoise_pointer = head
        for _ in range(n):
            deer_pointer = deer_pointer.next
        if not deer_pointer:
            return head.next
        
        while deer_pointer.next:
            deer_pointer = deer_pointer.next
            tortoise_pointer = tortoise_pointer.next
            
        tortoise_pointer.next = tortoise_pointer.next.next
        return head
