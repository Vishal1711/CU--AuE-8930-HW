class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next

        for k in sorted(nodes):
            point.next = ListNode(k)
            point = point.next
        return head.next

lists = [[1,4,5],[1,3,4],[2,6]]

ob1 = Solution()
print(ob1.mergeKLists(lists))
