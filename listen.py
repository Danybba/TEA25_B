# age_1 = 27
# age_2 = 30
# age_3 = 25

# print(age_1)
# print(age_2)
# print(age_3)

# task_1 = "Go to the gym"
# task_2 = "Buy groceries"
# task_3 = "Call mom"

# print(task_1)
# print(task_2)
# print(task_3)

age = [27, 30, 25]

age[2] = 26
age.append(28)
age.insert(1, 66)
age.pop()
age.remove(66)
age.sort()
age.reverse()
age.clear()
age.extend([29, 31, 24])

print(len(age))

for ages in age:
    print(ages)

todo = ["Go to the gym", "Buy groceries", "Call mom"]

print(todo)

student = {
    "name": "Anna",
    "age": 17,
    "city": "Berlin",
    "hobbies": ["Lesen", "Schwimmen", "Zeichnen"]
}

print(student)
print(student["name"])
print(student.get("city"))

student["age"] = 18
student["grade"] = "A"
student["school"] = "Goethe Gymnasium"

print("Schluessel:", student.keys())
print("Werte:", student.values())

student.pop("city")

for key, value in student.items():
    print(key, ":", value)

