import random

def main():
    print("=" * 40)
    print("      بازی حدس عدد")
    print("=" * 40)
    print("من یک عدد بین ۱ تا ۱۰۰ انتخاب کردم.")
    print("سعی کن حدس بزنی!\n")

    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"شانس باقی‌مانده: {remaining}")

        try:
            guess = int(input("حدس شما: "))
        except ValueError:
            print("لطفاً فقط عدد وارد کن.\n")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("عدد باید بین ۱ تا ۱۰۰ باشد.\n")
            continue

        if guess == secret:
            print(f"\nآفرین! درست حدس زدی.")
            print(f"عدد {secret} بود و در {attempts} تلاش پیدا کردی.")
            break
        elif guess < secret:
            print("عدد بزرگ‌تره!\n")
        else:
            print("عدد کوچک‌تره!\n")
    else:
        print(f"\nشانس‌هات تموم شد!")
        print(f"عدد درست {secret} بود.")

    print("\n" + "=" * 40)
    print("بازی تموم شد. ممنون که بازی کردی!")
    print("=" * 40)

if __name__ == "__main__":
    main()
