# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # function to convert linked list to list for addition
    def toList(self, linked):
        convt = []
        while linked is not None:
            convt.append(linked.val)
            linked = linked.next
        return convt
    # function to add list of integers

    def addLists(self, num1, num2):
        sol = []
        for i in range(len(num1)):
            sol.append(num1[i]+num2[i])
        for i in range(len(sol)-1):
            if sol[i] >= 10:
                sol[i] = sol[i] - 10
                sol[i+1] = sol[i+1] + 1
        if sol[(len(sol)-1)] >= 10:
            sol[(len(sol)-1)] = sol[(len(sol)-1)] - 10
            sol = sol+[1]
        return sol
    # function to change list of integers back to linked list

    def cvtBack(self, lst):
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = self.toList(l1)
        second = self.toList(l2)
        # matching length
        diff = len(first) - len(second)
        if diff < 0:
            diff = -1 * diff
            first = first + [0]*diff
        else:
            second = second + [0]*diff
        result = self.addLists(first, second)
        answer = self.cvtBack(result)
        return (answer)
