from collections import deque


class Node(object):

    def __init__(self,val):
        self.val = val
        self.next = None

    def get_data (self):
        return self.val

    def set_data (self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next (self, next):
        self.next = next


class LinkedList (object):

    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count (self):
        return self.count

    def insert (self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        '''
        Find the first item with a given value
        '''
        node = self.head
        while True:
            if node is None:
                return None

            elif node.get_data() == val:
                return node

            else:
                node = node.get_next()

            
    def deleteAt(self, idx):
        if idx > self.get_count() - 1:
            return
        
        if idx == 0:
            self.head == self.head.get_next()

        else:
            node = self.head
            current_index = 0
            while current_index < idx - 1:
                node = self.head.get_next()
                current_index += 1

            prev_node = node
            prev_node.set_next(prev_node.get_next().get_next())

        self.count -= 1


    def dump_list(self):
        node = self.head

        while node is not None:
            print(f"Node: {node.get_data()}")
            node = node.get_next()


class Stack (object):

    def __init__(self):
        self.data = deque()

    def push (self, data):
        self.data.append(data)

    def pop (self):
        return self.data.pop()


class Queue (object):
    def __init__(self):
        self.data = deque()

    def push (self, data):
        self.data.append(data)

    def pop (self):
        return self.data.popleft()




if __name__ == "__main__":

    llist = LinkedList()
    llist.insert(38)
    llist.insert(49)
    llist.insert(13)
    llist.insert(15)

    llist.dump_list()

    print(f"Item count: {llist.get_count()}")
    print(f"Finding item {llist.find(13)}")
    print(f"Finding item {llist.find(78)}")

    llist.deleteAt(2)

    llist.dump_list()