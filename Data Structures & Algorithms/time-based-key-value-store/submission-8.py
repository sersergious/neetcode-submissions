class TimeMap:

    def __init__(self):
        self.hM = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hM[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hM:
            return ""

        vals = self.hM[key]
        l, h = 0, len(vals) - 1
        res = ""
        
        while l <= h:
            mid = (l + h) // 2

            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                l = mid + 1
            else:
                h = mid - 1
        
        return res