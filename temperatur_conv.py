# Temperatur Umwandlung # 

# Celsius = (Fahrenheit - 32) * 5/9
# Celsius = Kelvin - 273.15
# Tiefste Temperatur = -273.15 Grad Celsius (0 Kelvin)

Celsius = 0 
Kelvin = 0
Fahrenheit = 0

temperatur_eingabe = input("Welche Temperatur möchten Sie umrechnen? (Celsius, Fahrenheit, Kelvin) ")
temperatur_wert = float(input("Geben Sie den Wert der Temperatur ein: "))

if (temperatur_eingabe == "Celsius" and temperatur_wert < -273.15) or (temperatur_eingabe == "Kelvin" and temperatur_wert < 0) or (temperatur_eingabe == "Fahrenheit" and temperatur_wert < -459.67):
    print("Ungültige Eingabe. Die Temperatur liegt unter dem absoluten Nullpunkt.")
    error = True
else:
    error = False

if error == False:
    temperatur_ziel = input("In welche Einheit möchten Sie die Temperatur umrechnen? (Celsius, Fahrenheit, Kelvin) ")
    if (temperatur_eingabe == "Celsius") and temperatur_ziel == "Kelvin":
        umrechnung = temperatur_wert + 273.15
    elif (temperatur_eingabe == "Celsius") and temperatur_ziel == "Fahrenheit":
        umrechnung = (temperatur_wert * 9/5) + 32
    elif (temperatur_eingabe == "Kelvin") and temperatur_ziel == "Celsius":
        umrechnung = temperatur_wert - 273.15
    elif (temperatur_eingabe == "Kelvin") and temperatur_ziel == "Fahrenheit":
        umrechnung = (temperatur_wert - 273.15) * 9/5 + 32
    elif (temperatur_eingabe == "Fahrenheit") and temperatur_ziel == "Celsius":
        umrechnung = (temperatur_wert - 32) * 5/9   
    elif (temperatur_eingabe == "Fahrenheit") and temperatur_ziel == "Kelvin":
        umrechnung = (temperatur_wert - 32) * 5/9 + 273.15
    else:
        print("Ungültige Eingabe. Bitte überprüfen Sie die Einheiten.")
        umrechnung = None
    
    if umrechnung is not None:
        print(f"{temperatur_wert} {temperatur_eingabe} sind umgerechnet {umrechnung} {temperatur_ziel}.")

elif error == True:
    print("Die Umrechnung konnte nicht durchgeführt werden, da die Eingabe ungültig war.")  