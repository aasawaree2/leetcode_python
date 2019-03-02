class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = current_node = ListNode(0)

        if not l1:
            return l2
        if not l2:
            return l1

        while l1 and l2:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next

        current_node.next = l1 or l2

        return head.next


def main():
    s = Solution()
    print(s.mergeTwoLists(ListNode(0), ListNode(1)))


if __name__ == '__main__':
    main()
