# Beats 90% in runtime, beats 70% in memory.


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # create a set to remove all duplicates from the list
        num_set = set(nums)
        ans = 0

        for num in num_set:
            # if the number minus 1 is not in the set, then the number is not a
            # part of a consecutive sequence.

            # Create a temporary value to store the value to check for the
            # current value plus 1

            # If the value of the temp value plus 1 is in the set, then the number is a part of a consecutive sequence.

            # Update the temp value to loop

            if num - 1 not in num_set:
                print(
                    f"\n{'-----' * 12}\
                        \nCurrent number being checked: {num}\
                        \n\n\t{num} - 1 = {num-1}\n"
                )
                print(
                    f"{num-1} not in set. Setting index 0 to {num} and checking if the next number is {num+1}.\n"
                )

                curr = num

                while curr + 1 in num_set:
                    print(
                        f"{curr+1} found in set. Adding 1 to the current length count and searching for {curr+2}.\n"
                    )
                    curr += 1

                print(f"Loop has broken due to not finding {curr+1} in set.")

                tans = ans
                ans = max(ans, curr - num + 1)
                print("\nChecking length of subsequence . . . \n")
                print(
                    "\t(Last index - first index) + 1 (since index starts at zero)\
                    \n\t\t({curr} - {num}) + 1 = {ans}."
                )
                if (curr - num) + 1 > tans:
                    print(
                        f"\n{ans} is greater than the current value of answer: {tans}.\
                        \n\nanswer has been updated to reflect the count of the consecutive sequence found in the list so far."
                    )
                else:
                    print(
                        f"\nanswer not updated as the length of the sequence was not as large as the previous length, {ans}."
                    )
        print(
            f"\n\nThe longest consecutive sequence of numbers in the list is of length {ans}.\n"
        )
        return ans


# Test cases

test = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
test2 = [-3, -2, -1, 0, 1, 2, 3, 4]
test3 = [1, 2, 4, 5, 7, 9, 10, 11, 11, 12, 13, 14, 15, 16]

Solution().longestConsecutive(test3)
