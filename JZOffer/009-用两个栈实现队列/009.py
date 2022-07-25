"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。\
(若队列中没有元素，deleteHead操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

提示：
1 <= values <= 10000
最多会对appendTail、deleteHead 进行10000次调用
"""

# 第一版本的代码  问题很大
class CQueue1(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.flag = 1  # 用这个定位使用那个栈来存储

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.stack1:
            self.stack1.append(value)
            self.flag = 1
        elif not self.stack2:
            self.stack2.append(value)
            self.flag = 2
        else:
            self.stack1.append(value) if self.flag == 1 else self.stack2.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if not self.stack1:
            return -1
        need_delete_num = self.stack1[-1]
        self.stack1.pop(-1)
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2[-1])

        return need_delete_num


"""
解题思路：
首先定义两个list作为栈，在入队列时，只要栈1空着，就往栈1寸，否则往栈2寸。
把栈1作为出队列的那个栈，栈1出完后，就把栈2从末尾开始移到栈1，移空为止。
然后每次的后续入栈继续往栈2入。就能实现入栈和出栈
"""
class CQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.stack1:
            self.stack1.append(value)
        else:
            self.stack2.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if not self.stack1:
            return -1
        need_delete_num = self.stack1[-1]
        self.stack1.pop(-1)
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2[-1])

        return need_delete_num


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
