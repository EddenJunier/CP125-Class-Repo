def calculate_bill(meal_price):
    tax = meal_price * 0.06  # 6% SST
    service_charge = 2.00
    total = meal_price + tax + service_charge
    return total

total1 = calculate_bill(8.50)  # Nasi Lemak
print(f"Customer 1 total: RM{total1:.2f}")