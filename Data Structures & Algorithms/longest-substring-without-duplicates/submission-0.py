class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_seen = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in chars_seen:
                chars_seen.remove(s[l])
                l += 1
            chars_seen.add(s[r])
            longest = max(longest, r - l + 1)
        return longest