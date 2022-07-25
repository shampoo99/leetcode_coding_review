"""
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

示例 1：

输入：nums = [1,2,3,1]
输出：true
示例 2：

输入：nums = [1,2,3,4]
输出：false
示例3：

输入：nums = [1,1,1,3,3,4,3,2,4,2]
输出：true

提示：
1 <= nums.length <= 105
-109 <= nums[i] <= 109

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x248f5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        nums = sorted(nums)
        for index, num in enumerate(nums):
            if index < length-1:
                if num == nums[index+1]:
                    return True
        return False