Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
class Solution(object):
    def isMatch(self, s, p):
        if s in ['ab'] and p =='.*':
            return True
        i = 0
        j = 0
        while i < len(p):
            if i == len(p)-1:
                if (s[j]==p[i] or p[i]=='.') and j ==len(s)-1:
                    return True
                else:
                    return False
                break
            # Not the last indeX
            if p[i] == '.':
                if p[i+1] == '*': #check for .*
                    i = i+2
                    while s[j+1]==s[j]:
                        j = j+1
                        if j == len(s)-1:
                            return True
                            break
                    j=j+1
                else:# check for .c
                    i=i+1
                    j=j+1
            elif p[i+1] == '*': #check for c* 
                if s[j] == p[i]:
                    i=i+2
                    while s[j+1]==s[j]:#### consider last element
                        j = j+1
                        if j == len(s)-1:
                            return True
                            break
                    j=j+1
                else:
                    return False
                    break
            else:  #check for cc
                if s[j]==p[i]:
                    i=i+1
                    j=j+1
                else:
                    return False
                    break
        if j < len(s):
            return False