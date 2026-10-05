continue_system = "yes"

while continue_system == "yes":
    
    order_amount = float(input("Enter order amount (TRY): "))
    available_stock = int(input("Enter available stock: "))
    requested_quantity = int(input("Enter requested quantity: "))
    is_member = input("Is the customer a member? (yes/no): ").strip().lower()

    if requested_quantity <= 0:
        print("Order Rejected: Invalid quantity. Must be greater than 0.")   
    elif requested_quantity > available_stock:
        print("Order Rejected: Insufficient stock.")
    else:
        if is_member == "yes" and order_amount >= 500:
            final_price = order_amount * 0.90
            print("Order Approved: 10% member discount applied.")
            print(f"Final Price: {final_price} TRY")
        else:
            final_price = order_amount
            print("Order Approved: Regular price.")
            print(f"Final Price: {final_price} TRY")
            
    continue_system = input("Do you want to process another order? (yes/no): ").strip().lower()

print("Exiting the system.")
