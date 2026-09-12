def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False


    for letter in s:
        if not letter.isalnum():
            return False

    number_started = False

    for letter in s:
        if letter.isdigit():
            if not number_started:
                if letter == "0":
                    return False

            number_started = True

        elif number_started and letter.isalpha():
            return False

    return True

plate = input("Plate: ")

if is_valid(plate):
    print("Valid")
else:
    print("Invalid")