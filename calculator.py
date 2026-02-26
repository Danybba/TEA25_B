"""
Input:
1. Zahl: 137
2. Zahl: 5
Rechenoperation: (+) Addition (-) Subtraktion (*) Multiplikation (/) Division: /

Output:
Das Ergebnis der Rechenoperation ist: 27.4
"""
error = False
number_1 = input("Gib die erste Zahl ein: ")

try:
    number_1 = float(number_1)
except ValueError:
    print("Fehler: Bitte gib eine gültige Zahl ein.")
    error = True

try:
    number_2 = float(input("Gib die zweite Zahl ein: "))    
except ValueError:
    print("Fehler: Bitte gib eine gültige Zahl ein.")
    error = True

if not error:
    operation = input("Gib die Rechenoperation ein (+, -, *, /): ")

    if operation == "+":    
        result = number_1 + number_2
    elif operation == "-":
        result = number_1 - number_2
    elif operation == "*":
        result = number_1 * number_2
    elif operation == "/":
        try:
            result = number_1 / number_2
        except ZeroDivisionError:
            result = "Fehler: Division durch Null ist nicht erlaubt."
    else:
        result = "Fehler: Ungültige Rechenoperation."

if not error:
    print(f"Das Ergebnis der Rechenoperation ist: {result}")

