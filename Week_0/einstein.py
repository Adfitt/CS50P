#!/usr/bin/env python3

def main():
    mass = int(input("Type a size of a mass: "))
    c = 300000000 ** 2
    energy = mass * c
    print(f"E: {energy:,}")

main()
