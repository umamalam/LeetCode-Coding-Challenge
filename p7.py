Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1


class Solution(object):
    def reverse(self, x):
        if x>=0:
            b =list(str(x))
            b.reverse()
            c=''
            c = c.join(b)
            if int(c)<2**31:
                return int(c)
            else: return 0
        else:
            x = -1*x
            b =list(str(x))
            b.reverse()
            c=''
            c = c.join(b)
            if int(c)<2**31:
                return -1*int(c)
            else:
                return 0

     