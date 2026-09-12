numbers = []

for _ in range(5):
    number = int(input("Nuumbers: "))
    numbers.append(number)

result = None

for number in numbers:
    if result is None or number > result:
        result = number

print(result)