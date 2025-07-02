2. Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1


CODE: (in Python)

Option 1: 
def is_palindrome(x):
        if x < 0:
            return False
        str_x = str(x)
        return str_x == str_x[::-1]
#test cases
print(is_palindrome(121))  # Output: True
print(is_palindrome(-121)) # Output: False  
print(is_palindrome(10))   # Output: False

Option 2:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        num = x
        
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        
        return rev == x

sol = Solution()
# Test cases
print(sol.isPalindrome(121))    # Output: True
print(sol.isPalindrome(-121))   # Output: False  
print(sol.isPalindrome(10))     # Output: False
 
