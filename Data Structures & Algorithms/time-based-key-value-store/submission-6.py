class TimeMap:

    def __init__(self):
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.tmap.get(key) is not None:
            self.tmap[key].append([timestamp, value])
        else:
            self.tmap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        # if there's no such key or the list is empty
        if self.tmap.get(key) is None or len(self.tmap[key]) == 0:
            return ""        

        values = self.tmap[key]

        # if there's 1 item
        if len(values) == 1:
            timestamp_prev, val = values[0]
            return val if timestamp_prev <= timestamp else ""
        
        l, r= 0, len(values) - 1
        res = ""
        while l <= r:
            mid = l + (r-l) // 2
            pair = values[mid]
            timestamp_prev, val = pair
            
            if timestamp >= timestamp_prev:
                res = val
                l = mid + 1
            else:
                r = mid - 1
        
        return res

