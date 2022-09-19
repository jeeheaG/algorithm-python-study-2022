#deque


# [1,2,3,2,1]
#이걸 첫 노드head로 시작하는 연결리스트로 주는데 나는 어떻게 줄 지 모르겠어서 
#실제 풀이와 테스트는 리트코드에서 하고 아래에 그 코드를 옮겨 적어만 두겠다

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        #input값이 비어있는 리스트일 경우 처리
        if not head :
            return True
        
        node = head
        
        #노드를 따라 탐색하며 리스트로 변환
        nodeList = []
        while node is not None :
            nodeList.append(node.val)
            node = node.next
        
        #배열의 앞쪽 값과 뒤쪽 값 비교
        # nodeList.pop(0) 부분이 속도가 느리다. 이는 deque를 사용해 개선할 수 있다.
        if nodeList.pop(0) != nodeList.pop() :
            return False
        
        return True

