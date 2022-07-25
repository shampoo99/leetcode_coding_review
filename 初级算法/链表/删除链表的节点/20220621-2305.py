"""
请编写一个函数，用于 删除单链表中某个特定节点 。
在设计函数时需要注意，你无法访问链表的头节点head ，只能直接访问要被删除的节点 。
题目数据保证需要删除的节点 不是末尾节点 。

示例 1：

输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：指定链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9
示例 2：


输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：指定链表中值为1的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9

提示：

链表中节点的数目范围是 [2, 1000]
-1000 <= Node.val <= 1000
链表中每个节点的值都是 唯一 的
需要删除的节点 node 是 链表中的节点 ，且 不是末尾节点

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnarn7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 这题最恶心的在于， 你没法知道删除节点的前置节点，因为不知道头节点
        # 所以我们可以 用一个很妙的方法：把A-next的值赋给A，然后把A-next删了就行
        node.val = node.next.val
        node.next = node.next.next
