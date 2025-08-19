# COMPLETED

# 2609. Find the Longest Balanced Substring of a Binary String

#  You are given a binary string s consisting only of zeroes and ones.

# A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

# Return the length of the longest balanced substring of s.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "01000111"
# Output: 6
# Explanation: The longest balanced substring is "000111", which has length 6.
# Example 2:

# Input: s = "00111"
# Output: 4
# Explanation: The longest balanced substring is "0011", which has length 4. 
# Example 3:

# Input: s = "111"
# Output: 0
# Explanation: There is no balanced substring except the empty substring, so the answer is 0.
 

# Constraints:

# 1 <= s.length <= 50
# '0' <= s[i] <= '1'

# 01000111

def findTheLongestBalancedSubstring(s):
    i = 0
    max_z = 0
    while True:
        index_0 = s.find('0', i)
        index_1 = s.find('1', index_0)
        if index_0 == -1 or index_1 == -1:
            break
        substr = s[index_0:index_1 + (index_1-index_0)]
        if substr.count('0') == substr.count('1') and len(substr) > max_z:
            max_z = len(substr)
        i = index_0 + 1

    return max_z
        
        
print(findTheLongestBalancedSubstring('01000111'))
print(findTheLongestBalancedSubstring('00111'))
print(findTheLongestBalancedSubstring('111'))