import math
import json
numbers = []
def save_history(expression):
    try:
        with open("history.json", "r") as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []

    history.append(expression)

    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)
def menu():
    choice = input("""
🌸✨ Cute Calculator ✨🌸
0️⃣  history📜
1️⃣  Sum ➕
2️⃣  Minus ➖
3️⃣  Times ✖️
4️⃣  Division ➗
5️⃣  Floor Division 📐
6️⃣  Power ⚡
7️⃣  Square Root 🌱
8️⃣  Clear History 🗑️
Type 'done' when you finish 💕
Your choice: 
""")

    return choice
def add():
    total = 0

    while True:
       num = input("🌸 give me a number: ")

       if num == 'done':
            break
       num = int(num)
       numbers.append(num)
       total = total + num
    expression = " + ".join(map(str, numbers))

    save_history(f"{expression} = {total}")

    return total
def minus():
    total = int(input("🌸 give me first number: "))
    numbers = [total]

    while True:
        num = input("🌸 give me next number: ")

        if num == 'done':
            break

        num = int(num)
        numbers.append(num)
        total -= num

    expression = " - ".join(map(str, numbers))
    save_history(f"{expression} = {total}")

    return total

def times():
    
    while True:
        num = input("🌸 Give me a number: ")

        if num == "done":
            break

        numbers.append(int(num))

    total = 1

    for num in numbers:
        total *= num

    expression = " × ".join(map(str, numbers))
    save_history(f"{expression} = {total}")
    return total
def division(): 
    total = int(input("🌸 give me first number: ")) 
    numbers.append(total) 
 
    while True: 
        num = input("🌸 give me a number: ") 
 
        if num == 'done': 
            break 
 
        numbers.append(int(num)) 
 
    try:
        for num in numbers[1:]: 
            total = total / num
    except ZeroDivisionError:
        print("❌ Cannot divide by zero! 🎀")
        return

    expression = " ÷ ".join(map(str, numbers)) 
    save_history(f"{expression} = {total}") 
 
    return total    
def floor_division(): 
    total = int(input("🌸 give me first number: ")) 
    numbers.append(total) 
 
    while True: 
        num = input("🌸 give me a number: ") 
 
        if num == 'done': 
            break 
 
        numbers.append(int(num)) 
 
    try:
        for num in numbers[1:]: 
            total = total // num
    except ZeroDivisionError:
        print("❌ Cannot divide by zero! 🎀")
        return

    expression = " // ".join(map(str, numbers)) 
    save_history(f"{expression} = {total}") 
 
    return total
def clear_history():
    with open("history.json", "w") as file:
        json.dump([], file)

    print("🗑️ History cleared! 🎀")

def power():
    base = int(input("🌸 give me the base: "))
    exponent = int(input("🌸 give me the exponent: "))

    result = base ** exponent

    save_history(f"{base} ** {exponent} = {result}")

    return result
def square_root():
    num = float(input("🌸 Give me a number: "))

    result = math.sqrt(num)

    save_history(f"√{num} = {result}")

    return result
def show_history():
    try:
        with open("history.json", "r") as file:
            history = json.load(file)

        print("📜 Calculation History 🎀")

        for item in history:
            print(item)

    except FileNotFoundError:
        print("📭 No history yet!")  
   
   
   
   
while True:
    answer=menu()
    if answer == '0':
        show_history()
    elif answer == "1":
        result=add()
        print(f"✨ Your answer is {result} 🎀")
    elif answer == "2":
        result=minus()
        print(f"✨ Your answer is {result} 🎀")
    elif answer == "3":
        result=times()
        print(f"✨ Your answer is {result} 🎀")
    elif answer == "4":
        result=division()
        print(f"✨ Your answer is {result} 🎀")
    elif answer=='5':
        result=floor_division()
        print(f"✨ Your answer is {result} 🎀")
    elif answer=='6':
        result=power()
        print(f"✨ Your answer is {result} 🎀")  
    elif answer=='7':
        result=square_root()
        print(f"✨ Your answer is {result} 🎀") 
    elif answer=='8':
         clear_history()            
         
    else:
      print("Please choose a valid option 🎀")        
