def calculator_discount(price, discount_percent):
    if discount_percent <0 or discount_percent > 100:
        return "Invalid discount"

    discount = price * discount_percent / 100
    final_price = price - discount

    return final_price

result = calculator_discount(1100, 15)
print(result)