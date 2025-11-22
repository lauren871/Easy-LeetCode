class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x) #Convert x to a string
        i,j = 0, len(x_str) - 1 #Set i to beginning of string and j to end of string
        while i < j:
            if x_str[i] != x_str[j]: #Check if the mirrored ends don't match each other
                return False
            i += 1
            j -= 1 # Move both mirrored positions inward

        return True #If everything matches then it's a palindrome
