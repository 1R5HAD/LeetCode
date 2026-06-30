class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Initialize the last seen indices of 'a', 'b', and 'c' to -1
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        total_substrings = 0
        
        for i, char in enumerate(s):
            # Update the last seen position of the current character
            last_seen[char] = i
            
            # Find the start index of the smallest valid window ending at i
            min_idx = min(last_seen['a'], last_seen['b'], last_seen['c'])
            
            # If all three characters have been seen at least once
            if min_idx != -1:
                # Add all valid substrings ending at the current index i
                total_substrings += min_idx + 1
                
        return total_substrings