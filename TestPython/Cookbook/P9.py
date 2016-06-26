# -*- coding: UTF-8 -*-

import heapq


# 实现优先级队列


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self._index = 0


def push(self, item, priority):
    heapq.heappush(self._queue, (-priority, self._index, item))
    self._index += 1


def pop(self):
    return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)
