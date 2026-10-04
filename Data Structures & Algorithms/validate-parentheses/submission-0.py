class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}
        stx = []

        for i in s:
            if i not in hashmap:
                stx.append(i)
            else:
                if not stx:
                    return False
                else:
                    popped = stx.pop()
                    if popped != hashmap[i]:
                        return False
        
        return not stx




        