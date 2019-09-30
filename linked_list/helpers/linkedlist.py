class Node(object):
    """A class for Linked List Data Structure"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def append(self, data):
        node = Node(data)
        current = self

        while current.next is not None:
            current = current.next

        current.next = node

    def delete(self, head, data):
        current = head

        if current.data == data:
            return current.next

        while current.next is not None:

            if current.next.data == data:
                current.next = current.next.next
                return head

            current = current.next

        return head




        