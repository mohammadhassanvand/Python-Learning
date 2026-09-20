import pyfiglet
import sys
import random

if len(sys.argv) == 1:
    font = random.choice(pyfiglet.FigletFont.getFonts())

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
        sys.exit("Invalid usage")
    font = sys.argv[2]

else:
    sys.exit("Invalid usage")

text = input("Input: ")

print(pyfiglet.figlet_format(text, font=font))