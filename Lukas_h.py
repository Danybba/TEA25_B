# Mini Taschenrechner
import math

print("=== Cool Calculator ===")
print("Tippe 'q' zum Beenden.\n")

while True:
    op = input("Operation (+, -, *, /, **, sqrt): ").strip().lower()

    if op == "q":
        print("Tschüss ")
        break

    if op == "sqrt":
        x = float(input("Zahl: "))
        if x < 0:
            print("Fehler: Wurzel aus negativer Zahl geht nicht.\n")
        else:
            print(f"Ergebnis: √{x} = {math.sqrt(x)}\n")
        continue

    if op not in ["+", "-", "*", "/", "**"]:
        print("Unbekannte Operation.\n")
        continue

    a = float(input("Erste Zahl: "))
    b = float(input("Zweite Zahl: "))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Fehler: Division durch 0.\n")
            continue
        result = a / b
    elif op == "**":
        result = a ** b

    print(f"Ergebnis: {a} {op} {b} = {result}\n")

