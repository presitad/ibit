class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, N):
        
        #Num=" ".join(Num)
        if (N<0):
            return 0
        Num=str(N)
        if Num==Num[::-1]:
            return 1
        else :
            return 0
        
        
print(Solution().IsPalindrome(1111 ))

