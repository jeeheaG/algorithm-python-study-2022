#Runner 기법 - 연결리스트의 특징을 살려 풀이

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
        
        slow = fast = head
        
        #역순 연결리스트 만들기
        rev = None
        # fast와 fast.next 모두 존재할(None이 아닐) 때 실행
        while fast and fast.next :
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            #위 코드는 rev=slow, rev.next=rev, slow=slow.next순으로 실행됨
            #rev는 새로운 원소가 '앞부분'에 추가됨.
        
        #[연결리스트 길이가 홀수일 때 중앙에 위치한 값 처리]
        #fast는 두 칸 씩 가므로
        #반복문을 모두 돈 후인데 fast가 None이 아닐 때 = 연결리스트 원소 개수가 홀수일 때임!
        #연결리스트 길이가 홀수일 경우 slow는 중앙의 값을 건너뛴 뒤에 rev와 비교를 시작해야 한다.
        #중앙의 값을 건너뛰기 위해 slow.next를 한 번 더 실행함!
        if fast : 
            slow = slow.next
        
        
        #역순리스트 rev와 중앙 직후부터 시작하는 slow비교로 팰린드롬 판단
        #rev가 None이 아니고 비교 결과가 동일할 때 계속 실행
        while rev and rev.val == slow.val :
            rev, slow = rev.next, slow.next
        
        #rev를 끝까지 돌았다면 None이 되었을 것이므로 True반환
        #끝까지 돌지 않았다면 rev.val == slow.val 이 성립하지 않은 구간이 있으므로 False반환
        return not rev