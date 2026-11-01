#!/usr/bin/env python3

def convert(text):
    message = text.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    return(message)

def main():
    text = input("Leave a message:\n")
    text_output = convert(text)
    print(text_output)

main()
