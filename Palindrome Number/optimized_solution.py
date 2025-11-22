class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #Neg numbers aren't palindrome and numbers ending in 0 can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0): #0 can be a palindrome so exclude
            return False

        reversed_half = 0
        while x > reversed_half: #If x < reversed_half then we have past half point and should've compared if they matched
            reversed_half = reversed_half * 10 + (x % 10) #Moves current digits up a place value and takes last digit of x and adds it to reversed half

            x //= 10 #Divides x by 10 removing the last digit

        #When x and reversed_half are equal check if they match
        return x == reversed_half or x == reversed_half // 10 #For numbers with odd digits removes the last digit that was added to reversed_half since middle doesn't matter
