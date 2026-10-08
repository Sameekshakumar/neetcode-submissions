from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        queue = deque()
        heap = []
        for key, value in count.items():
            heap.append((-value, key))
        heapq.heapify(heap)

        time = 0
        while heap or queue:
            time += 1

            while queue and queue[0][0] == time:
                available_time, freq, task = queue.popleft()
                heapq.heappush(heap, (-freq, task))

            if heap:
                freq, task = heapq.heappop(heap)
                freq = -freq
                freq -= 1
                if freq:
                    queue.append((time+n+1, freq, task))
    
        return time


        