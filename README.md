# Discount Calculator 💰

A simple Python program that calculates the **final price of an item after applying a discount**.
If the discount is **20% or higher**, the discount is applied. Otherwise, the original price is returned.

## Example

```python
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

price = 20000
discount_percent = 30
final_price = calculate_discount(price, discount_percent)
print(f"Final price: {final_price} TSH")
```

### ✅ Output

```
Final price: 14000 TSH
```

## Usage

Clone the repo and run:

```bash
Discount.py
```

