import random

def get_user_choice():
    while True:
        choice = input("\nانتخاب شما (سنگ / کاغذ / قیچی): ").strip()
        if choice in ["سنگ", "کاغذ", "قیچی"]:
            return choice
        print("لطفا فقط یکی از این سه تا رو بنویس: سنگ، کاغذ یا قیچی")

def get_computer_choice():
    return random.choice(["سنگ", "کاغذ", "قیچی"])

def determine_winner(user, computer):
    if user == computer:
        return "مساوی"
    
    wins = {
        "سنگ": "قیچی",
        "کاغذ": "سنگ",
        "قیچی": "کاغذ"
    }
    
    if wins[user] == computer:
        return "شما"
    else:
        return "کامپیوتر"

def main():
    print("=" * 40)
    print("      بازی سنگ کاغذ قیچی")
    print("=" * 40)
    
    user_score = 0
    computer_score = 0
    round_num = 1
    
    while True:
        print(f"\n--- راند {round_num} ---")
        print(f"امتیاز شما: {user_score} | امتیاز کامپیوتر: {computer_score}")
        
        user = get_user_choice()
        computer = get_computer_choice()
        
        print(f"\nشما: {user}")
        print(f"کامپیوتر: {computer}")
        
        winner = determine_winner(user, computer)
        
        if winner == "مساوی":
            print("نتیجه: مساوی شد!")
        elif winner == "شما":
            print("نتیجه: شما برنده شدید!")
            user_score += 1
        else:
            print("نتیجه: کامپیوتر برنده شد!")
            computer_score += 1
        
        again = input("\nمی‌خوای دوباره بازی کنی؟ (بله/خیر): ").strip().lower()
        if again not in ["بله", "آره", "yes", "y"]:
            break
        
        round_num += 1
    
    print("\n" + "=" * 40)
    print("بازی تموم شد!")
    print(f"امتیاز نهایی → شما: {user_score} | کامپیوتر: {computer_score}")
    
    if user_score > computer_score:
        print("تبریک! شما برنده کلی شدید")
    elif computer_score > user_score:
        print("کامپیوتر این بار قوی‌تر بود")
    else:
        print("بازی مساوی تموم شد")
    print("=" * 40)

if __name__ == "__main__":
    main()
