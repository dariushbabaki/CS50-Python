import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Enter your text: ")
    print(figlet.renderText(text))
    
elif sys.argv[1] =="-f" and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
    text = input("Enter your text: ")
    print(figlet.renderText(text))
else:
    sys.exit("Invalid usage")
