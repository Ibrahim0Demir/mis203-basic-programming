while True:
    starting_balance = float(input("Enter your starting balance: "))
    if starting_balance < 0:
        print("Starting balance cannot be negative. Please try again.")
        continue
    break

while True:
    monthly_deposit = float(input("Enter your monthly deposit: "))
    if monthly_deposit <= 0:
        print("Monthly deposit must be a positive number. Please try again.")
        continue
    break

while True:
    interest_rate = float(input("Enter the monthly interest rate (as a percentage): "))
    if interest_rate < 0:
        print("Interest rate cannot be negative. Please try again.")
        continue
    break

while True:
    savings_goal = float(input("Enter your savings goal: "))
    if savings_goal <= 0:
        print("Savings goal must be a positive number. Please try again.")
        continue
    break

total_earned = 0
goal_reached = False
months_used = 0

if starting_balance >= savings_goal:
    goal_reached = True
    print("Congratulations! You have already reached your savings goal.")
else:
    for month in range(1, 61):
        interest_earned = starting_balance * (interest_rate / 100)
        total_earned += interest_earned
        starting_balance += interest_earned + monthly_deposit
        months_used = month

        print(f"Month {month}: interest earned: ${interest_earned:.2f}, balance: ${starting_balance:.2f}")

        if starting_balance >= savings_goal:
            goal_reached = True
            break

if goal_reached and months_used == 0:
    print("Goal reached: Yes, already at the start.")
elif goal_reached:
    print(f"Goal reached: Yes, in {months_used} month(s).")
else:
    print(f"Goal reached: No, after {months_used} months.")
print(f"Final balance: ${starting_balance:.2f}")
print(f"Total interest earned: ${total_earned:.2f}")
  