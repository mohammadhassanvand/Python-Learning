import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("=== Password Generator ===")

    while True:
        try:
            length = int(input("Password length: "))
            if length < 4:
                print("Length must be at least 4.")
                continue

            password = generate_password(length)
            print(f"\nGenerated Password:\n{password}")
            break

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
