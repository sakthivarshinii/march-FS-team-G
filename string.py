def short_long_short(a: str, b: str) -> str:
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

# Example usage:
a = "Hi"
b = "There"
print(short_long_short(a, b)) 