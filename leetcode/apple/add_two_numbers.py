# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#  

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#  

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # My Solution
        resultCurrent = ListNode((l1.val + l2.val) % 10)
        resultHead = resultCurrent
        carry = (l1.val + l2.val) // 10
        while True:
            if (l1 is None) and (l2 is None):
                if carry == 1:
                    resultCurrent.next = ListNode(1)
                return resultHead
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if l1 and l2:
                resultCurrent.next = ListNode((l1.val + l2.val + carry) % 10)
                carry = (l1.val + l2.val + carry) // 10
                resultCurrent = resultCurrent.next
            elif l1 is None and l2:
                resultCurrent.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                resultCurrent = resultCurrent.next
                # continue to l2
            elif l1 and l2 is None:
                resultCurrent.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                resultCurrent = resultCurrent.next
                # continue to l1
        return resultHead

        # Proposed Solution
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        resultCurrent = ListNode()
        resultHead = resultCurrent
        while (l1 is not None) or (l2 is not None):
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            val = (x + y + carry) % 10
            # resultCurrent.val = val % 10
            carry = ((x + y + carry) // 10)
            resultCurrent.next = ListNode(val)
            resultCurrent = resultCurrent.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry == 1:
            resultCurrent.next = ListNode(1)
        return resultHead.next