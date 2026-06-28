class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        low = 0
        high = len(numbers)-1

        while low <= high:
            
            if numbers[low] + numbers[high] > target:
                high -= 1
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                res.append(min(low, high)+1)
                res.append(max(low, high)+1)
                break
                    
        return res
        
        