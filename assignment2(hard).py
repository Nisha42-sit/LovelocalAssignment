def shortest_palindrome(s):
    if s == s[::-1]:
        # Already a palindrome
        return s

    for i in range(len(s), 0, -1):
        if s[:i] == s[:i][::-1]:
            # Found the longest palindrome starting from the first character
            return s[i:][::-1] + s

# Example usage:
s = "abcd"
result = shortest_palindrome(s)
print(result)
