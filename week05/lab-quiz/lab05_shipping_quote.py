def calculate_subtotal(unit_price, quantity):
    return round(unit_price * quantity, 2)

def get_discount_rate(subtotal):
    if subtotal >= 500:
        return 0.10
    return 0.0

def calculate_shipping_fee(weight_kg):
    if weight_kg <= 2.0:
        return 30.0
    return round(30.0 + (weight_kg - 2.0) * 10.0, 2)

def calculate_final_total(subtotal, discount_rate, shipping_fee):
    discount_amount = subtotal * discount_rate
    return round((subtotal - discount_amount) + shipping_fee, 2)

assert calculate_subtotal(50, 4) == 200
assert get_discount_rate(499.99) == 0.0 
assert get_discount_rate(500.0) == 0.10  
assert calculate_shipping_fee(2.0) == 30.0

def process_order(order_name, unit_price, quantity, weight_kg):
    subtotal = calculate_subtotal(unit_price, quantity)
    rate = get_discount_rate(subtotal)
    shipping = calculate_shipping_fee(weight_kg)
    final_total = calculate_final_total(subtotal, rate, shipping)

    print(f"--- {order_name} ---")
    print(f"Subtotal: {subtotal:.2f} TL")
    print(f"Discount Rate: %{rate * 100:.0f}")
    print(f"Shipping Fee: {shipping:.2f} TL")
    print(f"Final Total: {final_total:.2f} TL\n")


process_order("Order 1", unit_price=150.0, quantity=4, weight_kg=3.5)

process_order("Order 2", unit_price=40.0, quantity=2, weight_kg=1.0)