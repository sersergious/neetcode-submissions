class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        lowI, highI = 0, len(matrix)-1

        while lowI <= highI:
            
            midI = lowI + (highI - lowI) // 2
            
            low, high = 0, len(matrix[midI]) - 1

            if matrix[midI][0] > target:
                highI = midI - 1
                
            elif matrix[midI][-1] < target:
                lowI = midI + 1
                
            else: 
                while low <= high:
                    mid = low + (high - low) // 2

                    if matrix[midI][mid] == target:
                        return True
                    elif matrix[midI][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
                break

        return False