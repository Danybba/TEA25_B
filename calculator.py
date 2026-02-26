"""
Input:
Zahl 1
Zahl 2
Rechenoperation: Add, Sub, Mul, Div

Output:
Ergebnis:

"""
ergebnis = 0
error = False

try:
    Zahl_1 = int(input("Bitte erste Zahl eingeben: "))
except ValueError:
    print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
    error = True

try:
    Zahl_2 = int(input("Bitte zweite Zahl eingeben: "))
except ValueError:
    print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
    error = True

if not error:   
    oppearation = input("Welche Rechenopperation möchten Sie durchführen? (add, sub, mul, div)")
    
    if oppearation == "add":
        ergebnis = Zahl_1 + Zahl_2
    elif oppearation == "sub":
         ergebnis = Zahl_1 - Zahl_2
    elif oppearation == "mul":
         ergebnis = Zahl_1 * Zahl_2
    elif oppearation == "div":
        try:
         ergebnis = Zahl_1 / Zahl_2
        except ZeroDivisionError:
            print("Fehler: Division durch Null ist nicht erlaubt.")
    else:
        print("Ungültige Rechenoperation.")

print(f"Das Ergebnis der Operation {oppearation} ist: {ergebnis}")