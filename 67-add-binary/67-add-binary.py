class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        ans = ""

        if(len(a)<len(b)):
            a=a.zfill(len(b))
        elif(len(b)<len(a)):
            b=b.zfill(len(a))

        for i in range(len(a)-1,-1,-1):
                if a[i] == "1" and b[i] =="1":
                    if carry is "0":
                        ans+="0"
                        carry = "1"
                    else:
                        ans+="1"


                elif (a[i] == "1" and b[i] == "0") or  (a[i] == "0" and b[i] == "1"):
                    if(carry is "0"):
                        ans+="1"
                    else:
                        ans+="0"


                else:
                    if(carry is "0"):
                        ans+="0"
                    else:
                        ans+="1"
                        carry = "0"
        if carry == "1":
            ans += "1"

        return ans[::-1]