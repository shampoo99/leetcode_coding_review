"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−231, 231− 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0

提示：

-231 <= x <= 231 - 1

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnx13t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 我的思路一开始是先把符号取下来，然后把数字放到一个数组，再给他拼回来，然后乘一下，也是受上一个反转list的代码影响，
        # 这里没有限制空间复杂度，所以可以直接做
        # 但是有一个溢出的判断需要斟酌
        flag = 0 if x >= 0 else 1
        x = abs(x)
        y = 0
        while (x > 0):
            y = y * 10 + x % 10
            x = x // 10

        if y > 2 ** 31 - 1:
            return 0

        if flag:
            y = 0 - y

        return y