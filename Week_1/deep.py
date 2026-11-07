#!/usr/bin/env python3

def main() -> None:
    message: str = input("What is the Answer to the Great Question of Life, "
                         "the Universe, and Everything? ").lower().strip()
    if message == "42" or message == "forty-two" or message == "forty two":
        print("yes")
    else:
        print("no")


main()
