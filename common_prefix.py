from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    word = strs[0]
    len_list = len(strs)
    while len(word)>0:
        counting = 0
        for i in strs:
            # print("i:", i, "conting:", counting, "word: ", word)
            if i.startswith(word):
                counting += 1
            if counting == len_list:
                return word
        word = word[:-1]
        # print("word: ", word)
    return word


print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","dog","dogdy"]))
print(longestCommonPrefix(["aa","ab"]))
