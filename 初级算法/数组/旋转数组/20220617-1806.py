"""
给你一个数组，将数组中的元素向右轮转 k个位置，其中k是非负数。


示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

进阶：

尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
你可以使用空间复杂度为O(1)原地算法解决这个问题吗？

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2skh7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# 解法1：多放一个k的空间来做
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        i = 0
        new_list = []
        while i < k:
            new_list.append(nums[length-k+i])
            i += 1
        for index in range(length-k):
            new_list.append(nums[index])

        for i in range(length):
            nums[i] = new_list[i]


class Solution_1(object):
    def rotate(self, nums, k):
        length = len(nums)
        new_list = []
        i = 0
        while i < length:
            new_list.append(nums[i])
            i += 1

        # 这个操作很重要！！
        # 然后在把临时数组的值重新放到原数组，并且往右移动k位
        i = 0
        while i < length:
            nums[(i + k) % length] = new_list[i]
            i += 1


class Solution_2(object):
    # 两重反转
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]