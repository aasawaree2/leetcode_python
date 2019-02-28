class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry_forward = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            summation = x + y + carry_forward
            carry_forward = int(summation / 10)
            curr.next = ListNode(summation % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if carry_forward:
                curr.next = ListNode(carry_forward)
        return dummy.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry_forward = 0
        while l1 or l2 or carry_forward:
            if l1:
                carry_forward += l1.val
                l1 = l1.next
            if l2:
                carry_forward += l2.val
                l2 = l2.next
            curr.next = ListNode(carry_forward % 10)
            carry_forward = carry_forward // 10
            curr = curr.next
        return dummy.next


def main():
    l1 = ListNode(1)
    l2 = ListNode(2)
    s = Solution()
    r = s.addTwoNumbers1(l1, l2)
    print(r.val)
    r = s.addTwoNumbers2(l1, l2)
    print(r.val)


if __name__ == '__main__':
    main()
