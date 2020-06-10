from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self._max_heap = []
        self._min_heap = []
        self._is_even = True
        
    def addNum(self, num: int) -> None:
        if len(self._max_heap) == 0:
            heappush(self._max_heap, -num)
            self._is_even = not self._is_even
            return
        
        max_heap_top = self._max_heap[0]

        if num <= -max_heap_top:
            heappush(self._max_heap, -num)
            if len(self._max_heap) - len(self._min_heap) == 2:
                max_heap_top = heappop(self._max_heap)
                heappush(self._min_heap, -max_heap_top)
        else:
            heappush(self._min_heap, num)
            if len(self._min_heap) - len(self._max_heap) == 1:
                min_heap_top = heappop(self._min_heap)
                heappush(self._max_heap, -min_heap_top)

        self._is_even = not self._is_even
            

    def findMedian(self) -> float:
        if len(self._max_heap) == 0:
            return 0

        if self._is_even is True:
            return (-self._max_heap[0] + self._min_heap[0]) / 2
        else:
            return -self._max_heap[0]


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3) 
    assert mf.findMedian() == 2