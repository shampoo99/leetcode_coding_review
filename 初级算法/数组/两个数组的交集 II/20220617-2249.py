"""
给你两个整数数组nums1 和 nums2 ，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

提示：

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果nums的大小nums2 小，哪种方法更优？
如果nums的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2y0c2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 解法1：先做出来再说，先排序，再处理，双指针
        len_1 = len(nums1)
        len_2 = len(nums2)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        index_1, index_2 = 0, 0
        output_list = []
        while index_1 < len_1 and index_2 < len_2:
            if nums1[index_1] == nums2[index_2]:
                output_list.append(nums1[index_1])
                index_2 += 1
                index_1 += 1
            elif nums1[index_1] > nums2[index_2]:
                index_2 += 1
            else:
                index_1 += 1
        print(output_list)
        return output_list

class Solution_1(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 用字典的方式做，时空复杂度其实都不如上面的
        dict_1 = {}
        output_list = []
        for num1 in nums1:
            if num1 not in dict_1:
                dict_1[num1] = 1
            else:
                dict_1[num1] += 1

        for num2 in nums2:
            if num2 in dict_1:
                if dict_1[num2]:
                    output_list.append(num2)
                    dict_1[num2] -= 1
        return output_list


if __name__ == '__main__':
    tt = Solution_1()
    sum1 = [1,1,2,2]
    sum2 = [2,2]
    tt.intersect(sum1,sum2)