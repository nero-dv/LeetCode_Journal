# We create a set from the list of numbers, and if the length of the set is not equal to the length of
# the list, then we know that there are duplicates


class Solution(object):
    def containsDuplicate(self, nums):
        hash_table = {item for item in nums}
        if len(hash_table) != len(nums):
            return True
        return False
