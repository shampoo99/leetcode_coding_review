"""
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        return_list = []
        if nums == [] or length < 3:
            return []

        for i in range(length - 1):
            if nums[i] > 0:
                break
            l = i + 1
            r = length - 1
            if i>0 and nums[i] == nums[i - 1]: # 加个if i>0 来兜底 000的case
                continue
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    return_list.append([nums[i], nums[l], nums[r]])
                    # 这里原来用的break和continue 但是不合适，要继续往下找
                    # 同时避免重复
                    while (l < r and nums[l] == nums[l + 1]):
                        l = l + 1
                    while (l < l and nums[r] == nums[r - 1]):
                        r = r - 1
                    l = l + 1
                    r = r - 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return return_list

if __name__ == '__main__':
    tt = Solution()
    tt.threeSum([0,0,0])
