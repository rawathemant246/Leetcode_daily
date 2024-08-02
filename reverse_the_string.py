def reverse_string(s):
    reversed_str = ""  # Start with an empty string
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character   first character will shift towards the right it will be prepend in the empty string
    return reversed_str



input_string = "hello"
reversed_string = reverse_string(input_string)
print("Original:", input_string)
print("Reversed:", reversed_string)




