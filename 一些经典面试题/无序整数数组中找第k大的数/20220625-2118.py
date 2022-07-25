"""
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
提示：

0 <= len(arr) <= 100000
0 <= k <= min(100000, len(arr))

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/smallest-k-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
快排中的每次递归，将待排数据分做两组，其中一组的数据的任何一个数都比另一组中的任何一个大，然后再对两组分别做类似的操作；
在本问题中，假设 N 个数存储在数组 S 中，我们从数组 S 中随机找出一个元素 X，把数组分为两部分 Sa 和 Sb。Sa 中的元素大于等于 X，Sb 中元素小于 X。
这时，有两种可能性：
1. Sa中元素的个数小于K，Sa中所有的数和Sb中最大的K-|Sa|个元素（|Sa|指Sa中元素的个数）就是数组S中最大的K个数。
2. Sa中元素的个数大于或等于K，则需要返回Sa中最大的K个元素。
"""


class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        begin = 0
        end = len(arr) - 1
        self.k = k
        print(self.quick_sort_k(arr, begin, end))

    def quick_sort_k(self, arr, begin, end):

        while begin < end:
            low = begin
            high = end
            key = arr[low]
            while low < high:
                while low < high and arr[high] > key:
                    high -= 1
                if arr[high] < key:
                    arr[low] = arr[high]
                    low += 1

                while low < high and arr[low] < key:
                    low += 1
                if arr[low] > key:
                    arr[high] = arr[low]
                    high -= 1

            arr[low] = key
            if begin - 1 == self.k:
                return arr[0:self.k - 1]

            self.quick_sort_k(arr, begin, low - 1) if low > self.k else self.quick_sort_k(arr, low + 1, end)

if __name__ == '__main__':
    tt = Solution()
    arr = [1, 3, 5, 7, 2, 4, 6, 8]
    k = 4
    tt.smallestK(arr, k)