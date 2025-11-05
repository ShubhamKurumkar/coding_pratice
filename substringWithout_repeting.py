''' Given a string s, find the length of the longest substring 
without duplicate characters.

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3. Note that "bca"
// and "cab" are also correct answers.'''

class Solution:
    def substringWithoutRepeting(self,s):
        s1=""
        for i,j in enumerate(s):
            if j not in s1[0:i+1]:
                s1=s1+j
        return len(s1)
s = Solution()
print(s.substringWithoutRepeting("abcabcbb") )