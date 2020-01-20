#! /usr/bin/python3
import sys
import pyfiglet

try:
    if sys.argv[1] == "-h":
        print("help")
    else:
        print(f"'{sys.argv[1]}' argument not recognized.\n Try '-h' for help")
except:
    pass

def mainw():
    print("working.")

def start_logo():
    font = pyfiglet.Figlet(font="slant")
    print(font.renderText('FireShield'))


if __name__ == "__main__":
    mainw()
    start_logo()