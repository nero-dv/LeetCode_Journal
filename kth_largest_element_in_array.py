from collections import deque

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    d = deque()
    checklist = [num for num in nums]

    for index in range(0, k):
        largest = max(checklist)
        d.appendleft(largest)
        checklist.remove(largest)

    element = list(d)

    return element[-k]

nums = [3,2,1,5,6,4]
k = 2

print(findKthLargest(nums, k))