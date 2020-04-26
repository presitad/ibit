import pdb
n=10
primes = [1 for i in range(n)]
primes[0] = primes[1] =0
# pdb.set_trace()
for j in range(2,n):
    for i in range(1,int(n/j)+1):
        if i == 1: continue
        try:
            primes[i*j]=0
        except IndexError:
            break
result = [i for i in range(n) if primes[i]==1]
print(result)