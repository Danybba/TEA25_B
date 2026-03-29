"""
Input:
1. Zahl: 137
2. Zahl: 5
Rechenoperation: (+) Addition (-) Subtraktion (*) Multiplikation (/) Division: /

Output:
Das Ergebnis der Rechenoperation ist: 27.4
"""

from functions import *

def calculate(num1, num2, operation):
    if operation == '+':
        return add_numbers(num1, num2)
    elif operation == '-':
        return subtract_numbers(num1, num2)
    elif operation == '*':
        return multiply_numbers(num1, num2)
    elif operation == '/':
        if num2 != 0:
            return divide_numbers(num1, num2)
        else:
            return "Fehler: Division durch Null ist nicht erlaubt."
    else:
        return "Fehler: Ungültige Rechenoperation."

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

result = calculate(number_1, number_2, operation)

print(f"Das Ergebnis der Rechenoperation ist: {result}")

