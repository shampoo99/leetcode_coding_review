"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]

提示：

1 <= digits.length <= 100
0 <= digits[i] <= 9
相关标签

Python



作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2cv1c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 两次反转，整体的空间复杂度比较高
        digits.reverse()
        length = len(digits)
        for index, num in enumerate(digits):
            if (num + 1) % 10 == 0:
                digits[index] = 0
                if index + 1 == length:
                    digits.append(1)
                    break
            else:
                digits[index] += 1
                break
        digits.reverse()
        print(digits)
        return digits


class Solution_1(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #如果不是9，则加1返回，如果是9先置为0
        for site in range(len(digits)-1, -1, -1):
            if digits[site] != 9:
                digits[site] += 1
                return digits
            else:
                digits[site] = 0
        # 以下是数组全为9的情况
        digits.insert(0,1)
        return digits



if __name__ == '__main__':
    tt = Solution()
    digits = [9]
    tt.plusOne(digits)
