import random
import string

print("--- Password Generator ---")
while True:
    password = input("Do you want to create a password? (yes or q to quit): ").strip().lower()
    if password == "q":
        print("Exiting program")
        break
        
    password_length = int(input("Enter password length (minimum 6): "))
    if password_length < 6:
        print("Password is too short. It must be at least 6 characters.")
        continue
        
    upper_case = input("Include uppercase letters? (yes/no): ").strip().lower()

    if upper_case not in ["yes", "no"]:
        print("Invalid choice. Please answer yes or no.")
        continue
        
    number = input("Include numbers? (yes/no): ").strip().lower()
    if number not in ["yes", "no"]:
        print("Invalid choice. Please answer yes or no.")
        continue
        
    symbols = input("Include symbols? (yes/no): ").strip().lower()
    if symbols not in ["yes", "no"]:
        print("Invalid choice. Please answer yes or no.")
        continue
        
    pool = string.ascii_lowercase
    if upper_case == "yes":
        pool = pool + string.ascii_uppercase
    if number == "yes":
        pool = pool + string.digits
    if symbols == "yes":
        pool = pool + string.punctuation
        
    generated_password = ""
    
    while len(generated_password) < password_length:
        generated_password = generated_password + random.choice(pool)
        
    print(f"\nYour password is: {generated_password}\n")

