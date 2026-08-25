class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #create a hashmap(same as dict)
        same_char = {}

        for i in range(len(s)):
            same_char[s[i]] = same_char.get(s[i], 0) + 1
            same_char[t[i]] = same_char.get(t[i], 0) - 1

        for k in same_char.values():
            if k != 0:
                return False

        return True

        