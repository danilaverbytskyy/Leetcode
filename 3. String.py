class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=""
        mx=0
        for c in s:
            if longest.find(c)==-1:
                longest += c
                mx = max(mx, len(longest))
                print(longest)
            else:
                longest=longest[longest.find(c)+1:]
        return mx


print(Solution.lengthOfLongestSubstring(Solution(), "aabaab!bb"))