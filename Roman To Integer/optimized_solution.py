class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0
        prev_value = 0

        for char in s:
            current_value = values[char]
            total += current_value # Add the current numeral's value

            # If previous was smaller, it should not have been added
            # Subtract twice to remove and subtract how we were supposed to

            if current_value > prev_value:
                total -= 2 * prev_value

            prev_value = current_value

        return total

