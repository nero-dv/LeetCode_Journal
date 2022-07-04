from copy import copy


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        s_set = ""

        def fake_set(k: str) -> str:
            for letter in s:
                if letter not in s_set:
                    s_set += letter

        # if s_set in s:
        #     res.append(len(s_set))
        # global count
        # count = 0
        # def subcheck(s, ss):
        #     if ss and ss in s:
        #         # print(f'Check {count}: \n')
        #         res.append(len(ss))
        #         ss = ss[1::]
        #         return subcheck(s, ss)
        #     elif ss not in s:
        #         ss = ss[1::]
        #         print(f'{ss}\nstop')
        #         return subcheck(s, ss)

        ss = [s for s in s_set]
        for x in range(len(s_set) * 2):
            if ss and ss in s:
                res.append(len(ss))
                ss = ss[1::]
            elif ss not in s:
                ss = ss[1::]
            elif not ss:
                ss = [s for s in s_set[::-1]]

        print(f"check 1:\n{subcheck(s, s_set)}\n")

        print(f"check 2:\n{subcheck(s, s_set[::-1])}\n")

        ans = max(res)

        return ans


s = "abcabcbb"

Solution().lengthOfLongestSubstring(s)
