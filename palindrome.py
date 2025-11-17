# Given an integer x, return true if x is a palindrome, and false otherwise.

 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=str(x)
        rev=""
        for i in r:
            if i.isdigit():
                rev=rev+i
        rev=rev[::-1]
        rev =int(rev)
        return rev == x