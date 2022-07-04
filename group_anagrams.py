strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagrams(strs):

    # left = 0
    # right = 1
    # list_len = len(strs)
    # while left < list_len:
    #     if sorted(strs[left]) == sorted(strs[right]):
    #         pass

    sorted_strs = []
    relist = {}
    left = 0
    right = 1

    # Sorting the words in the list and then appending the sorted word and the index of the original word to a new list.
    for idx, word in enumerate(strs):
        srtword = ""
        for x in sorted(word):
            srtword += x
        sorted_strs.append((srtword, idx))

    # This is creating a dictionary with the sorted word as the key and an empty list as the value.
    for key in sorted_strs:
        if key not in relist:
            relist[key[0]] = []

    # This is comparing the first word in the list to the second word in the list.
    while left < len(sorted_strs):
        first = sorted_strs[left][0]
        word_idx = sorted_strs[left][1]
        second = sorted_strs[left][0]

        if first == second:
            relist[first].append(strs[word_idx])
            right += 1
        left += 1

    # Creating a list of the values in the dictionary.
    ga = [x for x in relist.values()]

    return ga
