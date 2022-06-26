

from itertools import combinations

nums = [-1,0,1,2,-1,-4]
# nums = ['A', 'B', 'C', 'D', 'E']

def threeSum(nums):
    idxlist = list(range(len(nums)))
    nums_dict = dict(zip(idxlist, nums))
    ret = combinations(nums, 3)
    for idx, num in map(lambda x: sum(list(x)) == 0, enumerate(list(ret))):
        print(idx, num)
        
threeSum(nums)
    

        
