class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=0
        best=""
        if not s: return 0
        if len(s)==1:return s
        for i in range(len(s)):
            for j in range(len(s)-1,i,-1):
                if j-i+1<=len(best):
                    break
                if s[j]==s[i]:
                    temp=s[i:j+1]
                    if temp[::-1]==temp and len(temp)>len(best):
                        best= temp
        if best:return best
        else: return s[0]
        