class ListNode:

	def __init__(self, x):

		self.data = x
		self.next = None


class Solutionss:

    def __init__(self) -> None:
        pass
    # Function to prnodes in
    # a given linked list
    def printList(self,node):

        while (node != None):
            print(node.data,
                end = " ")
            node = node.next

    # The main function that
    # takes an array of lists
    # arr[0..last] and generates
    # the sorted output
    def mergeKLists(self,arr):
        last=2

        # Traverse form second
        # list to last
        for i in range(1, last + 1):
            while (True):
                # head of both the lists,
                # 0 and ith list.
                head_0 = arr[0]
                head_i = arr[i]

                # Break if list ended
                if (head_i == None):
                    break

                # Smaller than first
                # element
                if (head_0.data >=
                    head_i.data):
                    arr[i] = head_i.next
                    head_i.next = head_0
                    arr[0] = head_i
                else:
                    # Traverse the first list
                    while (head_0.next != None):
                        # Smaller than next
                        # element
                        if (head_0.next.data >=
                            head_i.data):
                            arr[i] = head_i.next
                            head_i.next = head_0.next
                            head_0.next = head_i
                            break
                        # go to next nod
                        head_0 = head_0.next
                        # if last node
                        if (head_0.next == None):
                            arr[i] = head_i.next
                            head_i.next = None
                            head_0.next = head_i
                            head_0.next.next = None
                            break
        return arr[0]

# Driver code


# Number of linked
# lists
k = 3

# Number of elements
# in each list
n = 4

# an array of pointers
# storing the head nodes
# of the linked lists
arr = [None for i in range(k)]

arr[0] = ListNode(1)
arr[0].next = ListNode(3)
arr[0].next.next = ListNode(5)
arr[0].next.next.next = ListNode(7)

arr[1] = ListNode(2)
arr[1].next = ListNode(4)
arr[1].next.next = ListNode(6)
arr[1].next.next.next = ListNode(8)

arr[2] = ListNode(0)
arr[2].next = ListNode(9)
arr[2].next.next = ListNode(10)
arr[2].next.next.next = ListNode(11)


sol=Solutionss()
# Merge all lists
head = sol.mergeKLists(arr)

sol.printList(head)
