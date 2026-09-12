name = input("camelCase: ")

result =""


for letter in name:
    if letter.isupper():
        result += "_" + letter.lower()
    else:
        result += letter

print(result)