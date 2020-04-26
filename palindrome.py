class Palindrome:
    def sentencePalindrome(s): 
        l, h = 0, len(s) - 1
        s = s.lower() 
        while (l <= h): 
            l += 1
            if (not(s[l] >= 'a' and s[l] <= 'z')): 
                pass
                elif (not(s[h] >= 'a' and s[h] <= 'z')):
                    h -= 1
                    elif (s[l] == s[h]): 
                        l += 1
                        h -= 1
            else: 
                return False
        return True
print(Palindrome().sentencePalindrome("abab baba"))
       
        
        
        
            
            
           
        
        
        
            
           
        
    
    s