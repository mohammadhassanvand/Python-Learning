text = input("Input: ")
result = ""

for letter in text:
    if letter not in "aeiouAEIOU":
        result += letter


print(result)