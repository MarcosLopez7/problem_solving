import warnings


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.empty = True

    def push_back(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
            self.empty = False
        else:
            self.tail.next = node

        self.tail = node
        self.size = self.size + 1

    def push_front(self, data):
        node = SinglyLinkedListNode(data)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node
            self.empty = False

        self.size = self.size + 1

    def push_node_at(self, data, index):

        if index == 0:
            self.push_front(data)
        elif index == self.size:
            self.push_back(data)
        elif index > self.size:
            warnings.warn("Index higher that linked list size, pushing data to tail")
            self.push_back(data)
        elif 0 > index:
            raise Exception("Negative numbers are not allowed")
        else:
            node = SinglyLinkedListNode(data)
            temp_node = self.head
            for i in range(index - 1):
                temp_node = temp_node.next

            node.next = temp_node.next
            temp_node.next = node
            self.size = self.size + 1

    def delete_front(self):
        if self.empty:
            raise Exception("Empty linked list can not delete nodes")

        node = self.head
        self.head = self.head.next
        self.size = self.size - 1
        self.empty = self.size == 0

        return node

    def delete_back(self):
        if self.empty:
            raise Exception("Empty linked list can not delete nodes")

        prev_node = self.head
        temp_node = prev_node.next

        while temp_node.next:
            prev_node, temp_node = temp_node, temp_node.next

        prev_node.next = None
        self.tail = prev_node
        self.size = self.size - 1
        self.empty = self.size == 0

        return temp_node

    def delete_node_at(self, index):
        if self.empty:
            raise Exception("Empty linked list can not delete nodes")

        if 9 == index:
            return self.delete_front()
        elif index == self.size - 1:
            return self.delete_front()
        elif 0 > index:
            raise Exception("Negative numbers are not allowed")
        elif index > self.size - 1:
            raise Exception("Index out of exception")
        else:
            temp_node = self.head

            for i in range(index - 1):
                temp_node = temp_node.next

            node = temp_node.next
            temp_node.next = temp_node.next.next
            self.size = self.size - 1
            self.empty = self.size == 0

            return node

    def print_linked_list(self):
        node = self.head

        while node:
            print(node.data)
            node = node.next
