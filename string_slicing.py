def reverse_string_slicing(s):
    """Reverse a string using slicing."""
    return s[::-1]

def reverse_string_loop(s):
    """Reverse a string using a manual loop."""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str