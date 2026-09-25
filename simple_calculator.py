def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "خطا: تقسیم بر صفر ممکن نیست"
        return num1 / num2
    elif operator == "**":
        return num1 ** num2
    elif operator == "%":
        return num1 % num2
    else:
        return "عملگر نامعتبر"

def main():
    print("=" * 40)
    print("       ماشین حساب ساده")
    print("=" * 40)
    print("عملگرهای مجاز: +  -  *  /  **  %")
    print("برای خروج بنویس: خروج\n")

    while True:
        expression = input("عبارت را وارد کن (مثال: 12 + 5): ").strip()

        if expression in ["خروج", "exit", "quit"]:
            break

        parts = expression.split()

        if len(parts) != 3:
            print("فرمت اشتباهه. مثال درست: 8 * 3\n")
            continue

        try:
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
        except ValueError:
            print("لطفاً عدد معتبر وارد کن.\n")
            continue

        result = calculate(num1, operator, num2)
        print(f"نتیجه: {result}\n")

    print("\n" + "=" * 40)
    print("خداحافظ!")
    print("=" * 40)

if __name__ == "__main__":
    main()
