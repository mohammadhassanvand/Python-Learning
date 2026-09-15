months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "Agust": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    date = input("Date: ")

    try:
        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        else:
            month, day, year = date.split()

            day = int(day.rstrip(","))
            year = int(year)
            month = months[month]

    except (ValueError, KeyError):
        continue

    if month < 1 or month >12:
        continue

    if day < 1 or day > 31:
        continue

    print(f"{year:04}-{month:02}-{day:02}")
    break