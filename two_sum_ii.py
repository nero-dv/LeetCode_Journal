class Solution:
    def twoSum(numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            summed = numbers[left] + numbers[right]

            if summed > target:
                right -= 1
            elif summed < target:
                left += 1
            else:
                return [left + 1, right + 1]


numbers = [0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 11, 15]
target = 9

print(Solution.twoSum(numbers, target))
