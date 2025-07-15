class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=""
        rez=0
        zap=0
        for i in a[::-1]:
            rez=0
            for k in b[::-1]:
                rez=int(i)+int(k)+zap
                zap=0
                if rez==0:
                    c+="0"
                elif rez==1:
                    c+="1"
                elif rez==2:
                    c+="0"
                    zap+=1
                elif rez==3:
                    c+=1
                    zap+=1
        return c



print(Solution.addBinary(Solution(), a = "11", b = "1"))