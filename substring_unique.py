
def lengthOfLongestSubstring(s: str) -> int:
        substring = ""
        list_of_substrings = []
        for letter in s:
            if letter not in substring:
                substring += letter
            else:
                list_of_substrings.append(substring)
                substring = "" + letter
        list_of_length = [len(i) for i in list_of_substrings]
            
        return max(list_of_length)

print(lengthOfLongestSubstring("pwwkew"))