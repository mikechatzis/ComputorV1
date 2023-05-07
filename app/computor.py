#!/usr/bin/env python3

import argparse
import math
import sys
import re

def parse_equation_string(eq_str : str):
    if not eq_str:
        raise argparse.ArgumentTypeError("Empty equation. Please enter a valid equation.")
    eq_str = eq_str.strip().replace(" ", "")                 # remove whitespace and spaces
    eq_sides = eq_str.split("=")                             # split the equation into two sides
    if len(eq_sides) != 2:                                   # check for multiple "="
        raise argparse.ArgumentTypeError("Invalid equation. Only one '=' is allowed.")
    
    left_terms = re.split(r'\s*(?=[+-])', eq_sides[0])           # split the left side at "+" and "-"
    left_terms = [term for term in left_terms if term.strip()]   # remove empty strings from left side

    right_terms = re.split(r'\s*(?=[+-])', eq_sides[1])          # split the right side at "+" and "-"
    right_terms = [term for term in right_terms if term.strip()] # remove empty strings from right side

    a, b, c = 0, 0, 0
    for term in left_terms:
        if term.endswith("*x^2"):                   # term is of the form ax^2
            a += float(term.replace("*x^2", ""))
        elif term.endswith("*x^1"):                 # term is of the form bx^1
            b += float(term.replace("*x^1", ""))
        elif term.endswith("*x^0"):                 # term is of the form cx^0
            c += float(term.replace("*x^0", ""))
        else:
            raise argparse.ArgumentTypeError(f"Invalid term {term}. Term must be of the form a*x^2, b*x^1 or c*x^0.")
    for term in right_terms:
        if term.endswith("*x^2"):                   # term is of the form ax^2
            a -= float(term.replace("*x^2", ""))
        elif term.endswith("*x^1"):                 # term is of the form bx^1
            b -= float(term.replace("*x^1", ""))
        elif term.endswith("*x^0"):                 # term is of the form cx^0
            c -= float(term.replace("*x^0", ""))
        else:
            raise argparse.ArgumentTypeError(f"Invalid term {term}. Term must be of the form a*x^2, b*x^1 or c*x^0.")

    return a, b, c

# print reduced form and polynomial degree
def print_data(a, b, c):
    Form = f"{a}*x^2 {b:+}*x^1 {c:+}*x^0 = 0"
    Form = Form.split(" ")
    pDegree = -1
    redForm = ""
    pos = 1
    for term in Form:
        if (pos == 1 and a == 0) or (pos == 2 and b == 0) or (pos == 3 and c == 0):
            pos += 1
            continue
        else:
            if ".0" in term:
                for (i, char) in enumerate(term):
                    if char == ".":
                        s = term[i:]
                        for (j, char) in enumerate(s):
                            if s[j] == "0":
                                continue
                            elif s[j].isdigit():
                                break
                            else:
                                term = term.replace(".0", "")
            redForm += term + " "
            pos += 1
    for term in redForm:
        if term == "^":
            pDegree += 1
    pDegree = pDegree if pDegree > 0 else 0
    print(f"Polynomial degree: {pDegree}")
    if redForm.find("+") == 0:
        redForm = redForm[1:]
    print(f"Reduced form: {redForm}")

def solve_polynomial(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("All real numbers solve the equation")
            else:
                print("This equation has no real number solution")
        else:
            x = -c / b
            print(f"The solution is x = {x}")
    else:
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            if x1.is_integer():
                x1 = int(x1)
            if x2.is_integer():
                x2 = int(x2)
            print(f"Discriminant is positive\nThe solutions are x1 = {x1} and x2 = {x2}")
        elif discriminant == 0:
            x = -b / (2*a)
            if x.is_integer():
                x = int(x)
            print(f"Discriminant is 0\nThe equation has exactly one solution: x = {x}")
        else:
            print("Discriminant is negative\nThis equation has no real number solution")

for arg in sys.argv[1:]:
    if arg == "-h" or arg == "--help":
        print("Usage: python computor.py 'ax^2 + bx^1 + cx^0 = dx^2 + ex^1 + fx^0'")
        sys.exit(0)
args = ""
for arg in sys.argv[1:]:
    args += arg

#program entry point
try:
    a, b, c = parse_equation_string(args)
    print_data(a, b, c)
    solve_polynomial(a, b, c)
except argparse.ArgumentTypeError as e:
    print(e, file=sys.stderr)
    sys.exit(1)
