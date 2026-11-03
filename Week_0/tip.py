#!/usr/bin/env python3

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

"""
Reviewing the available str methods, I found that
lstrip() and rstrip() allow me to remove symbols from
the specific side indicated in each function's instructions.
"""
def dollars_to_float(d):
    return float(d.lstrip("$"))

def percent_to_float(p):
    return float(p.rstrip("%")) / 100

main()
