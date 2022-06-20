# class Solution(object):
from calendar import c
from operator import indexOf


def topKFrequent(array, k):
    """
    :type array: List[int]
    :type k: int
    :rtype: List[int]
    """
    keys = []
    counted = []
    idx = []
    
    keys = list(set(array))
    for key in range(len(keys)):
        counted.append([array.count(keys[key]), keys[key]])
    
    for i in range(len(array)):
        idx.append(max(counted)[1])
        counted.remove(max(counted))
    print(idx)
    
    
    return idx

array = [1,1,1,2,2,2,2,2,3,3]
k = 3

topKFrequent(array, k)