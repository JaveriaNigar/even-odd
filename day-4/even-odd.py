num = int(input("Enter a number: "))  

if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

num = int(input("Enter a number: ")) 

if num % 2 == 0:  
    print(f"{num} is an Even number.")  
else:  
    print(f"{num} is an Odd number.")  

while True:  
    user_input = input("Enter a number (or type 'exit' to quit): ")  
    
    if user_input.lower() == "exit":  
        print("Exiting the program. Goodbye! 👋")
        break
    
    try:  
        num = int(user_input)  

        if num % 2 == 0:  
            print(f"🔢 {num} is an Even number.")  
        else:  
            print(f"🔢 {num} is an Odd number.")  
    
    except ValueError: 
        print("❌ Invalid input! Please enter a valid number.")
