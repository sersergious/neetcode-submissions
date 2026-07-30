class TimeMap:

    def __init__(self):
        self.hM = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hM[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hM:
            return ""
        
        values = self.hM[key]
        l, h = 0, len(values) - 1
        res = ""
        while l <= h:
            mid = (l + h) // 2
            timestamp_prev, val = values[mid] 
            if timestamp >= timestamp_prev :
                res = val
                l = mid + 1
            else:
                h = mid - 1 
        
        return res