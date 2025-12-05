class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def get_value(char):
            if char == 'I': return 1
            elif char == 'V': return 5
            elif char == 'X': return 10
            elif char == 'L': return 50
            elif char == 'C': return 100
            elif char == 'D': return 500
            elif char == 'M': return 1000
        
        i = 0
        num = 0
        while i < len(s): #If s = I, 0 < 1 so loop will run. 1 !< 1 so loop will stop
            #Check if only 1 numeral left and regular case
            if i == len(s) - 1 or get_value(s[i]) >= get_value(s[i+1]):
                num += get_value(s[i])
                i += 1
            else:
                num += get_value(s[i + 1]) - get_value(s[i])
                i += 2
        
        return num
