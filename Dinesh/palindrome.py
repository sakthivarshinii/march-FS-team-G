import re

def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    filtered_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if the string is equal to its reverse
    return filtered_s == filtered_s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False
print(is_palindrome(" "))  # Output: True
