class Verifypri:
    def run (self):
        N=int (input("enter number "))
        if N>1:
            for i in range (2,N):
                if (N%i==0):
                    return 0
            return 1

Verifypri().run()
# print(result)
