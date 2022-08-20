class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        zeroes = ones = ans = 0
        for c in s:
            if c == "1":
                if zeroes:
                    ans = max(ans+1,zeroes)
                ones+=1
            else:
                zeroes+=1
        return ans