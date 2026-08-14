import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones
        for i in range(len(self.heap)):
            self.heap[i] = -1 * self.heap[i]
        heapq.heapify(self.heap) 

        while (len(self.heap)>1):
            ele1 = -(heapq.heappop(self.heap))  #higher num
            ele2 = -(heapq.heappop(self.heap))
            if ele1 == ele2:
                pass
            else:
                heapq.heappush(self.heap, -(ele1-ele2))
        
        if self.heap:
            return -self.heap[0]
        return 0