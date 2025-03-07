user_input = input("Enter a string: ")

print("Characters at even index positions:")
for index in range(0, len(user_input), 2):
    print(user_input[index])