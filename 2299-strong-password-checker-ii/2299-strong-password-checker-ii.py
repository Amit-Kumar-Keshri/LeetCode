class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special_char = {"!","@","#","$","%","^","&","*","(",")","-","+"}
        l,u,s,n = 0,0,0,0
        if len(password)<8: 
            return False
        for i in range(len(password)):
            if i>0 and password[i-1]==password[i]: 
                return False
            if (password[i].islower()):
                l += 1
                
            if (password[i].isupper()):
                u += 1
                
            if password[i] in special_char:
                s += 1
            
            if password[i].isnumeric():
                n += 1
                
        if l!=0 and u!=0 and s!=0 and n!=0:
            return True
        
        return False
        
                