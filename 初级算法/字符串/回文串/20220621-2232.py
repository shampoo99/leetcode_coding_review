"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。


示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
示例 2:

输入: "race a car"
输出: false
解释："raceacar" 不是回文串

提示：

1 <= s.length <= 2 * 105
字符串 s 由 ASCII 字符组成
相关标签

Python



作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xne8id/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 这里有两个问题，一个是需要处理掉字符串中的其他非字母和数字字符，二是需要把大小写做转换
        # python中有两个函数，一个是lower和upper，可以批量处理字符，二是isalpha和isdigit 可以判断是不是数字和字母
        new_str = s.lower()
        res = ([x for x in new_str if x.isalpha() or x.isdigit()])
        leng = len(res)
        for i in range(leng // 2):
            if res[i] != res[leng - 1 - i]:
                return False
        return True