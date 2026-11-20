class DoublyLinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoublyLinkedList(tokens[0])
        curr = head

        for i in range(1, len(tokens)):  # O(n) space comp and time
            curr.next = DoublyLinkedList(tokens[i], prev=curr)
            curr = curr.next

        while head is not None: # O(n) time comp
            if head.val in "+-*/":
                l = int(head.prev.prev.val)
                r = int(head.prev.val)
                if head.val == "+":
                    temp = l+r
                elif head.val == "-":
                    temp = l-r
                elif head.val == "*":
                    temp = l*r
                elif head.val == "/":
                    temp = int(l/r)

                head.val = str(temp)
                if head.prev.prev.prev is not None:
                    head.prev = head.prev.prev.prev

                if head.prev is not None:
                    head.prev.next = head
                    

            
            ans = int(head.val)

            head = head.next

        return ans

                      