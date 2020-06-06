from _ast import List


class Solution:
    '在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。'
    '数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。'
    '请找出数组中任意一个重复的数字。'
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                v = nums[i]
                if nums[v] != v:
                    nums[i], nums[v] = nums[v], nums[i]
                else:
                    return nums[i]
        return -1

