"""
快速排序
"""


def quicksort(nums):
    high = len(nums) - 1
    low = 0

    recursion_sort(nums, low, high)
    print(nums)


def recursion_sort(nums, low, high):
    begin = low
    end = high
    basic = nums[low]
    # 这里我一开始想的是交换，但是交换一是不好定位置，而是值会变化，所以应该用坑的概念，不用管哨兵，最后哪里剩了就把它丢进哪儿
    if begin < end:
        while low < high:
            while low < high and nums[high] > basic:
                high -= 1

            if low < high:
                nums[low] = nums[high]
                low += 1

            while low < high and nums[low] < basic:
                low += 1

            if low < high:
                nums[high] = nums[low]
                high -= 1

        nums[low] = basic
        recursion_sort(nums, begin, low - 1)
        recursion_sort(nums, low + 1, end)


if __name__ == '__main__':
    nums = [51, 5, 2, 49, 59, 28, 4]
    quicksort(nums)
