import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1

    levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }

    return levels.get(score, "Very Weak")

def main():
    print("=" * 40)
    print("Password Generator & Strength Checker")
    print("=" * 40)

    while True:
        print("\n1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            length = int(input("Password length: "))
            password = generate_password(length)
            print("\nGenerated Password:", password)

        elif choice == "2":
            password = input("Enter password: ")
            print("Strength:", password_strength(password))

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
