# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []


# Definition for singly-linked list.
from typing import List
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
def mergeTwoLists(l1, l2):
    # define the two memory addresses pointing to node to be created
    nodeHead = nodeTrackerCurrent = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            nodeTrackerCurrent.next = l1
            l1 = l1.next
        else:
            nodeTrackerCurrent.next = l2
            l2 = l2.next

        nodeTrackerCurrent = nodeTrackerCurrent.next

    if l1: nodeTrackerCurrent.next = l1
    if l2: nodeTrackerCurrent.next = l2
    return (nodeHead.next)


class Solution:
    def build_queue(self, lists):
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        return q

    def mergeKLists2(self, lists):
        head = ListNode()
        current = head
        q = self.build_queue(lists)

        while not q.empty():
            val, list_node = q.get()
            current.next = ListNode(val)
            current = current.next
            next_node = list_node.next
            if next_node:
                q.put((next_node.val, next_node))

        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        if k == 0:
            return None

        step = 1
        while step < k:
            for i in range(0, k - step, step * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + step])
            step *= 2
        return lists[0]
