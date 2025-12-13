class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Edge case for empty list
        if not strs:
            return ""
        
        # Find shortest word in the list
        shortest_length = len(strs[0]) # Set as length of first string
        for string in strs: # For every string in list named strs
            if len(string) < shortest_length:
                shortest_length = len(string)

        prefix = "" # Initialize prefix as empty string

        # Loop to for each character
        for j in range(shortest_length): # For every letter index up to shortest word length
            char = strs[0][j] # Get the character from the first string at index j

            # Loop for each string to compare characters
            for i in range(1, len(strs)): # For every string in the list from index 1 to end exclusive (not including last index ex. strs[3] iterates 1, 2)
                if strs[i][j] != char: # If character at index j doesn't match char
                    return prefix # Return the prefix found so far
                
            prefix += char # If all strings matched, add char to prefix

        return prefix # Return the full prefix if loop completes