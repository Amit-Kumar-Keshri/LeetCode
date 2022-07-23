class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = sentence.split(" ")
        m = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                if ans[i][0] in m:
                    ans[i] = ans[i]+"ma"
                    ans[i] = ans[i]+"a"*(i+1)
                    break
                else:
                    t = ans[i][0]
                    r = ans[i][1:]
                    r = r+t+"ma"
                    ans[i] = r+"a"*(i+1)
                    break
        return " ".join(ans)