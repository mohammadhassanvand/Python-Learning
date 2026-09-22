
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 15

class Monster:
    def __init__(self):
        self.hp = random.randint(50, 120)
        self.attack = random.randint(8, 20)

def battle(player, monster):
    print("\nA wild monster appeared!")

    while player.hp > 0 and monster.hp > 0:
        print(f"\n{player.name} HP: {player.hp}")
        print(f"Monster HP: {monster.hp}")

        action = input("Attack or Run? ").lower()

        if action == "attack":
            damage = random.randint(5, player.attack)
            monster.hp -= damage
            print(f"You dealt {damage} damage!")

            if monster.hp > 0:
                damage = random.randint(3, monster.attack)
                player.hp -= damage
                print(f"Monster dealt {damage} damage!")

        elif action == "run":
            print("You escaped!")
            return

    if player.hp > 0:
        print("\nVictory!")
    else:
        print("\nGame Over!")

name = input("Enter your hero name: ")
player = Player(name)
monster = Monster()

battle(player, monster)
