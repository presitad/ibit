class Binary:
    def run(self, N):
        import pdb;pdb.set_trace()
        result = []
        while N>0:
            i = int(N%2)
            N=int(N/2)
            result.append(i)
        # return result[::-1]
        return [a for a in reversed(result)]
         
print(Binary().run(20))
