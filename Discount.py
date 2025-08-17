def calculate_discount(price, discount_percent):
    """Calculates the final price after applying discount if >= 20%."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Given assumption
price = 20000
discount_percent = 30

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: {final_price:.2f} TSH")
else:
    print(f"No discount applied. Original price: {final_price:.2f} TSH")
