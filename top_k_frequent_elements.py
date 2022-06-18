class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        keys = []
        counted = []
        idx = []

        for num in nums:
            if num not in keys:
                keys.append(num)
        for key in range(len(keys)):
            counted.append([nums.count(keys[key]), keys[key]])
        counted.sort(reverse=True)
        for i in range(0, k):
            idx.append(counted[i][1])

        return idx