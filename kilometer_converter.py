'Dieses Programm kann Meilen in Kilomenter umrechnen. '
'Es fragt den Nutzer nach der Anzahl der Meilen '
'und gibt die entsprechende Anzahl an Kilometern aus. '
'1 Meile entspricht 1.60934 Kilometern.'''

FACTOR_MILES_TO_KM = 1.60934

miles = int(input("Gib die Anzahl der Meilen ein: "))
kilometers = miles * FACTOR_MILES_TO_KM
print(f"{miles} Meilen entsprechen {kilometers} Kilometern.")