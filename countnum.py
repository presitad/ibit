class Solution:
    def binary(arr,N):
        
        low=0
        high=len(arr)-1
        mid=(low+high)/2
        count=0
        while (low<high):
            if (arr[low]>N>arr[high]):
                return 0
            if (arr[low]<N>arr[high]): 
                if (N==mid):
                    count+=1
                    return count
                if(N>mid):
                    for i in range(arr[mid+1],arr[high]):
                        if (N>are[mid+1]):
                            count+=1
                            mid+=1
                            return count
                        else:
                            break
                if (N<mid):
                    for i in range(arr[mid-1],arr[low]):
                        if (N>are[mid-1]):
                            count+=1
                            mid-=1
                            return count
                        else:
                            break
result=Solution().binary([1,2,2,2,3,4,5,6,7,8],2)
print(result)


