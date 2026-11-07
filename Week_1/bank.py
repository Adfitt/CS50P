#!/usr/bin/env python3

def main() -> None:

    message: str = input("Greeting: ").lower().lstrip()
    if message.startswith("hello"):
        print("$0")
    elif message.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
