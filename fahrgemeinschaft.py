credits_available = int(input("Haben Sie Credits zu verfügung? (Geben Sie den Betrag ein)")) 
ride_type = input("Möchten Sie Ihre Fahrt Upgraden? (comfort/plus) ")

ride_price = 0
final_price = 0 

if ride_type == "plus": 
    ride_price = 20.5
elif ride_type == "comfort":
    ride_price = 37.9
else:
    ride_price = 18.7

if credits_available > 0:
    final_price = ride_price - credits_available
    print(f"Der Fahrpreis nach Abzug der Credits beträgt: {final_price} Euro.")