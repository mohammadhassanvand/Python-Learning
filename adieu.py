names = []

while True:

    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        break

if len(names) == 1:

    print(f"Adieu, adieu, to {names[0]}")

elif len(names) == 2:

    print(f"Adieu, adieu, to{names[0]} and {names[1]}")

else:

    last = names.pop()
    print(f"Adieu, adieu, to {', '.join(names)}, and {last}")