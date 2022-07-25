"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意，必须在不复制数组的情况下原地对数组进行操作。

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]

提示:

1 <= nums.length <= 104
-231<= nums[i] <= 231- 1


进阶：你能尽量减少完成的操作次数吗？

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2ba4i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 思路之，直接遍历，把所有0元素删了，最后再补回来，起飞
        for index, num in enumerate(nums):
            if num == 0:
                nums.remove(num)
                nums.append(0)

if __name__ == '__main__':
    tt = Solution()
