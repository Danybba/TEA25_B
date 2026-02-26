# entered_pin = 1234
# expected_pin = 1234

# print(entered_pin == expected_pin)

# print("orange" == "orange")

# print("orange" > "apple")
# print("orange" < "apple")

age = int(input("Please enter your age: "))

license = input("Do you have a driving license? (yes/no) ")

alcohol = input("Did you drink alcohol? (yes/no) ")

insurance = input("Do you have car insurance? (yes/no) ")

if (age >= 18) and (license == "yes") and (alcohol == "no") and (insurance == "yes"):
    print("You can drive")
else:
    print("You are not allowed to drive.")

if (age >= 18) or (license == "yes") or (alcohol == "no") or (insurance == "yes"):
    print("You can drive")

# hour = int(input("What is the current hour (0-23)? "))

# if hour < 12:
#     print("Good morning!")
# elif hour < 18:
#     print("Good afternoon!")
# elif hour < 22:
#     print("Good evening!")
# else:
#     print("Good night!")