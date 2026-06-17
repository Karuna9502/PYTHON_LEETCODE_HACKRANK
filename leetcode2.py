'''Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        return even + odd
