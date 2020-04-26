class Solution:
    # @param A : integer
    # @return a list of strings
    

    def fizzBuzz(self, N):
        temp=[]
            
        for i in range(1 ,N+1):
            val = i
            if ((i)%3==0):
                val="Fizz"
            if ((i)%5==0):
                val="Buzz"
            if ((i)%15==0):
                val="FizzBuzz"
                
            temp.append(val)
            
            
        return temp
    
            

