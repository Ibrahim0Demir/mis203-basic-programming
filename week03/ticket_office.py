total_ticket=0
total_revenue=0
free_ticket_counter=0
while True:
    customer_name=input("Enter customer name(or q to quit): ").strip()
    if customer_name.lower()== "q":
        break

    customer_age=int(input("Enter customer age: "))
    if 0>customer_age or customer_age>120:
        print("Please enter a valid age")
        continue

    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ("weekday", "weekend"):
        print("Invalid day.")
        continue
    student_check=input("Student(yes/no): ").strip().lower()
    if student_check not in ("yes", "no"):
        print("Please answer yes or no.")
        continue

    ticket_price=200 if day == "weekday" else 250
    if customer_age<6:
        discount=1.0
        discount_category="Free"
    elif customer_age>=65:
        discount=0.5
        discount_category="Senior"
    elif 6<=customer_age<=12:
        discount=0.4
        discount_category="Child"
    elif student_check=="yes" and customer_age<=25:
        discount=0.3
        discount_category="Student"
    else:
        discount=0.0
        discount_category="Standard"

    ticket_price=ticket_price*(1.0-discount)
    print(f"{customer_name}:{ticket_price:.2f} TRY ({discount_category})")

    total_ticket +=1
    total_revenue=total_revenue+ticket_price
    average_price=total_revenue/total_ticket
    if discount_category=="Free":
        free_ticket_counter +=1
if total_ticket==0:
    print("No tickets sold.")
else:
    print(f"Tickets sold: {total_ticket}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {average_price:.2f} TRY")
    print(f"Free tickets: {free_ticket_counter}")
