import random

def roll_dice(sides=6, count=1):
    results = [random.randint(1, sides) for _ in range(count)]
    return results

def main():
    print("=" * 40)
    print("         تاس‌انداز")
    print("=" * 40)

    while True:
        try:
            sides = input("\nتاس چند وجهی؟ (پیش‌فرض ۶): ").strip()
            sides = int(sides) if sides else 6
            if sides < 2:
                print("تاس باید حداقل ۲ وجه داشته باشد.")
                continue

            count = input("چند تا تاس بندازم؟ (پیش‌فرض ۱): ").strip()
            count = int(count) if count else 1
            if count < 1:
                print("حداقل باید ۱ تاس بندازی.")
                continue
            if count > 20:
                print("حداکثر ۲۰ تاس می‌تونی بندازی.")
                continue

            results = roll_dice(sides, count)

            print(f"\nنتیجه تاس‌ها ({count} تا تاس {sides} وجهی):")
            print(" → ".join(str(r) for r in results))

            if count > 1:
                total = sum(results)
                print(f"جمع کل: {total}")

        except ValueError:
            print("لطفاً فقط عدد وارد کن.")
            continue

        again = input("\nدوباره تاس بندازم؟ (بله/خیر): ").strip().lower()
        if again not in ["بله", "آره", "yes", "y"]:
            break

    print("\n" + "=" * 40)
    print("خداحافظ!")
    print("=" * 40)

if __name__ == "__main__":
    main()
