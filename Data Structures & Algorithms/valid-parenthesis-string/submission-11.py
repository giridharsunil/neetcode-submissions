class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[0] == ")" or s[len(s)-1] == "(":
            return False
        lp = []
        star = []
        for i in range(len(s)):
            if s[i] == "(":
                lp.append(i)
            if s[i] == "*":
                star.append(i)
            if s[i] == ")":
                if len(lp)!=0:
                    lp.pop()
                elif len(star)!=0:
                    star.pop()
                else:
                    return False
        while len(star)!=0 and len(lp)!=0:
            if lp[-1] > star[-1]:
                return False
            lp.pop()
            star.pop()
        return len(lp) == 0


        
            
        