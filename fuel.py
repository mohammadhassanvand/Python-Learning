while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if x < 0 or y <= 0 or x > y:
            continue

        percentage = x / y * 100

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{round(percentage)}%")

        break
    
    except ValueError:
        continue

    except ZeroDivisionError:
        continue    
