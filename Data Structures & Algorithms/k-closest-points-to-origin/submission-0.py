import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        combined = []
        ans = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = (x**2 + y**2)**(1/2)
            combined.append((-dist, x, y))
        
        heapq.heapify(combined)
        for j in range(len(combined)-k):
            heapq.heappop(combined)
        
        for k in range(len(combined)):
            ans.append([combined[k][1], combined[k][2]])
        
        return ans
