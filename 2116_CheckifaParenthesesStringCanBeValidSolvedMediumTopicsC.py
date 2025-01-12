class Solution(object):
    def canBeValid(self, s, locked):
    
        # If the length of s is odd, it cannot be valid
        if len(s) % 2 != 0:
            return False
        
        # Left to right pass
        open_count, close_count, flexible = 0, 0, 0
        for i in range(len(s)):
            if locked[i] == "1":  # Locked character
                if s[i] == '(':
                    open_count += 1
                else:
                    close_count += 1
            else:  # Unlocked character
                flexible += 1
            
            # Ensure at no point ')' exceeds '(' + flexible
            if close_count > open_count + flexible:
                return False
        
        # Right to left pass
        open_count, close_count, flexible = 0, 0, 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == "1":  # Locked character
                if s[i] == '(':
                    open_count += 1
                else:
                    close_count += 1
            else:  # Unlocked character
                flexible += 1
            
            # Ensure at no point '(' exceeds ')' + flexible
            if open_count > close_count + flexible:
                return False
        
        # If both passes succeed, the string can be valid
        return True
