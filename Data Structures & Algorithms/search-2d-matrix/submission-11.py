class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time:
        # Reflection:

        lRow, hRow = 0, len(matrix) - 1

        while lRow <= hRow:
            midRow = (lRow + hRow) // 2

            if matrix[midRow][0] > target:
                hRow = midRow - 1
            elif matrix[midRow][-1] < target:
                lRow = midRow + 1
            else:
                l, h = 0, len(matrix[midRow]) - 1

                while l <= h:
                    mid = (l + h) // 2

                    if target == matrix[midRow][mid]:
                        return True
                    elif target < matrix[midRow][mid]:
                        h = mid - 1
                    else:
                        l = mid + 1
                break
        
        return False
