#!/usr/bin/env python3

def main() -> None:

    arch: str = input("File name: ").strip().lower()

    if arch.endswith(".gif"):
        print("image/gif")
    elif arch.endswith(".jpg") or arch.endswith(".jpeg"):
        print("image/jpeg")
    elif arch.endswith(".png"):
        print("image/png")
    elif arch.endswith(".pdf"):
        print("application/pdf")
    elif arch.endswith(".txt"):
        print("text/plain")
    elif arch.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
