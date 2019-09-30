class Solution(object):
    """Write code to remove duplicates from an unsorted linked list."""

    def removeduplicate(self, head):
        d = {}

        current = head
        previous = None

        while current is not None:
            if current.data in d:
                previous.next = current.next
            else:
                d[current.data] = 1
                previous = current
            
            current = current.next
            
        return head

            