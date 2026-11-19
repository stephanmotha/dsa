class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        "abcddeffgx"

        seen = set()
        l = 0
        r = 0
        ans = 0
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(s[r])
            r += 1
            ans = max(ans, len(seen))

        return ans



    
        