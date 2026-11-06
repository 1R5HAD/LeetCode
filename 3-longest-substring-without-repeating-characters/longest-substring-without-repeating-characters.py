class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        if len(s)==1:return 1
        for i in range(len(s)):
            seen={s[i]}
            leng=1
            for j in range(i+1,len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    leng+=1
                else:
                    break
            length=max(length,leng)
        return length