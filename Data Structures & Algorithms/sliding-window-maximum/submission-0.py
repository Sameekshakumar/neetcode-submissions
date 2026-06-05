from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_window = []
        dq = deque()
        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]: #while last dq ele is smaller than our latest num
                dq.pop()
            dq.append(r)

            if dq and dq[0] < r-k+1: #removing the index that's no longer in the window
                dq.popleft()

            if r >= k-1: #after k-1 i will hv valid windows
                max_window.append(nums[dq[0]])
        return max_window
        