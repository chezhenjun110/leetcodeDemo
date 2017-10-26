# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        size=len(s)-1
        Max=1
        i=0
        j=i+1
        while i<size and j<size:
            if s[j]!=s[i]:
                j+=1
            else:
                current=j-i
                if current>Max:
                    Max=current
                i=j
                j+=1
        return Max

a = "pwwkew"
s=Solution()
print(s.lengthOfLongestSubstring(a))

