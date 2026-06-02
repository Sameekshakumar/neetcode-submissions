class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        solution = set()

        for i in range(len(nums)):
            fixed = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = fixed + nums[l] + nums[r]
                if s == 0:
                    solution.add((fixed, nums[l], nums[r]))
                    l += 1
                    r -= 1

                elif s < 0:
                    l += 1

                else:
                    r -= 1

        return [list(x) for x in solution]