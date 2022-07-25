"""
给你一个整数数组 prices ，其中prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润。

示例 1：

输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
    随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     总利润为 4 + 3 = 7 。
示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
    总利润为 4 。
示例3：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0 。


提示：

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2zsx1/
来源：力扣（LeetCode）

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        # 以下为贪心算法
        for index in range(len(prices)-1):
            if prices[index+1] - prices[index] > 0:
                total += prices[index+1] - prices[index]
        return total


# 以下为贪心算法代码优化：使用列表推导式
class Solution_1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = sum([(prices[index + 1] - prices[index]) for index in range(len(prices)-1) if prices[index + 1] - prices[index]>0])
        return total


#以下为动态规划
class Solution_2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices)<2:
            return 0
        hold = -prices[0]
        no_hold = 0
        for i in range(len(prices)):
            hold = max(hold,no_hold-prices[i])
            no_hold = max(no_hold,hold+prices)
        return no_hold

"""
一些思路之：这鸟题目要用到动态规划，完了，不太会
现在会了，链接中有一个很详细的解法，欢迎学习
还可以用贪心算法！！牛啊！ 贪心的话，只要算最低点和最高点就行，把每段涨幅都加起来，跌的不算就行
"""