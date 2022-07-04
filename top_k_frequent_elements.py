from heapq import heapify, nlargest
import re


class Solution:
    def topKFrequent(nums, k):
        counted = []
        keys = set(nums)
        for idx, key in enumerate(keys):
            count = len(re.findall(str(key), str(nums)))
            counted.append([count, key])
        heapify(counted)
        topk = [n[1] for n in nlargest(k, counted)]
        return topk


nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5]
k = 2
print(Solution.topKFrequent(nums, k))
