def greet_user(name):
    print(f"Hello {name}!")


# greet_user("User")
# greet_user("Anna")
# greet_user("Emil")


def double_number(num):
    result = num * 2
    return result

def triple_number(num):
    result = num * 3
    return result

def add_numbers(num1, num2):
    result = num1 + num2
    return result

def subtract_numbers(num1, num2):
    result = num1 - num2
    return result

def multiply_numbers(num1, num2):
    result = num1 * num2
    return result   

def divide_numbers(num1, num2):
    if num2 != 0:
        result = num1 / num2
        return result
    else:
        return "Error: Division by zero is not allowed."
    

# var = double_number(5)
# print(var)

# print(double_number(5))

# print(add_numbers(3, 4))


def add_bonus(salary):
    global start_value 
    start_value = 200   
    bonus = 100
    print(salary + bonus + start_value)

add_bonus(5000)

print(start_value)