class Prefix:
    def run(self,arr):
        if not arr:
            return ""
        pre=[]
        i=0
        while True:
            keep_compairing = True
            for j in range(0,len(arr)-1):
                try:
                    if (arr[j][i]==arr[j+1][i]) and keep_compairing:
                        keep_compairing = True
                    else:
                        keep_compairing = False
                except IndexError:
                    keep_compairing = False
                    break
            if j == len(arr)-2 and keep_compairing:
                pre.append(arr[0][i]) 
            else:
                break
            i+=1
            
        mypre = ''.join(pre)
        return mypre
Prefix().run(["abcdefgh","abcefgh","abc"])

