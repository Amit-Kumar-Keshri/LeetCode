class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = []
        j = 0
        for i in range(n):
            if ("".join(sorted(words[i])) != "".join(sorted(words[j]))) or i == n-1 :
                ans.append(words[j])
                j = i
            
        if "".join(sorted(words[n-1])) != "".join(sorted(words[n-2])):
            ans.append(words[n-1])

        return ans