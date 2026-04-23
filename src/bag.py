class Bag:
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

    def add(self, item):
        old_first = self._first
        self._first = self._Node(item, old_first)
        self._n += 1

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

    bag = Bag()
    input_data = sys.stdin.read().split()
    
    for item in input_data:
        bag.add(item)

    print(f"size of bag = {bag.size()}")
    for s in bag:
        print(s)