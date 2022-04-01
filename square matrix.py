import numpy as np
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = np.square(nums)
        s.sort()
        return s
