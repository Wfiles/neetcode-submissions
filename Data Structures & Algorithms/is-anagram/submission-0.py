class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_char = {}

        for char in s :
            if char in seen_char : 
                seen_char[char] += 1
            else :
                seen_char[char] = 1
        
        for char in t :
            if char in seen_char : 
                seen_char[char] -= 1
                if seen_char[char] == 0 :
                    seen_char.pop(char)
            else :
                return False
        
        if not seen_char :
            return True
        else :
            return False
