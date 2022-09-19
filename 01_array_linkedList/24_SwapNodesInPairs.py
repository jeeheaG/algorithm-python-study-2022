#연결리스트 문제이므로 리트코드에서 풀이하고 코드를 아래에 복붙만 해둠


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        node = head
        
        while node and node.next :
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next # 두 칸 씩 건너뛰기
            
        return head
