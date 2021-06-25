# https://leetcode.com/problems/peak-index-in-a-mountain-array/
from typing import List


def solution(array: List[int]) -> int:
    low = 0
    hi = len(array) - 1
    mid = hi // 2

    if array[mid] < array[mid - 1]:
        return low + solution(array[low: mid + 1])
    elif array[mid] < array[mid + 1]:
        return mid + solution(array[mid: hi + 1])
    else:
        return mid
