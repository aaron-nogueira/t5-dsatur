class Stack:
    class _Node:
        def __init__(self, item=None, next_node=None):
            self.item = item
            self.next = next_node

    def __init__(self):
        self._first = None
        self._n = 0

    def is_empty(self):
        return self._first is None

    def size(self):
        return self._n

    def push(self, item):
        old_first = self._first
        self._first = self._Node(item, old_first)
        self._n += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        item = self._first.item
        self._first = self._first.next
        self._n -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._first.item

    def __str__(self):
        return " ".join(str(item) for item in self)

    def __iter__(self):
        return self._LinkedIterator(self._first)

    class _LinkedIterator:
        def __init__(self, first):
            self._current = first

        def __iter__(self):
            return self

        def __next__(self):
            if self._current is None:
                raise StopIteration
            item = self._current.item
            self._current = self._current.next
            return item

if __name__ == "__main__":
    import sys
    
    stack = Stack()
    input_data = sys.stdin.read().split()
    
    for item in input_data:
        if item != "-":
            stack.push(item)
        elif not stack.is_empty():
            print(stack.pop(), end=" ")
            
    print(f"({stack.size()} left on stack)")