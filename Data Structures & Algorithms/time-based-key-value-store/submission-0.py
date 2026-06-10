class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)  # key → [(timestamp, value), ...    ]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.store:
            return result
        l = 0
        r = len(self.store[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.store[key][mid][0] <= timestamp:
                result = self.store[key][mid][1]  
                l = mid + 1
            else:
                r = mid - 1
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)