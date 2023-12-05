def length_of_last_word(s):
    # Split the string into words
    words = s.split()

    # Check if there are any words in the string
    if not words:
        return 0

    # Return the length of the last word
    return len(words[-1])

# Example usage:
input_string = "Hello World"
result = length_of_last_word(input_string)
print(result)
