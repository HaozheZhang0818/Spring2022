"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""
# custom_queue.py

from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        try:
            return self._items.popleft()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        yield from self._items

    def __reversed__(self):
        yield from reversed(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"