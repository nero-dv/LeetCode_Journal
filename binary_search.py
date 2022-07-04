class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binarySearch(nums, target, low, high):

            if high >= low:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    return mid

                elif nums[mid] > target:
                    return binarySearch(nums, target, low, mid - 1)

                else:
                    return binarySearch(nums, target, mid + 1, high)

            else:
                return

        result = binarySearch(nums, target, 0, len(nums) - 1)
        return result


nums = [3, 4, 5, 6, 7, 8, 9]
target = 2

print(Solution().search(nums, target))
