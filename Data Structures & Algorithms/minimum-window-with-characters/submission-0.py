class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for i in t:
            need[i] = need.get(i, 0) + 1
        need_count = len(need)
        window = {}
        l = 0
        have = 0
        result = float("inf")
        res_l, res_r = 0, 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1
            while have == need_count:
                if r-l+1 < result:
                    result = r-l+1
                    res_l = l
                    res_r = r
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        if result == float("inf"):
            return ""

        return s[res_l:res_r+1]

        