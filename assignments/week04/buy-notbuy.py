prices = []

print("Enter prices of 6 items:")
for i in range(1, 7):
    price = float(input(f"Item {i}: "))
    prices.append(price)

print()
budget = float(input("Enter total budget: "))
print()

total_spent = 0
bought_items = []

for i in range(len(prices)):
    price = prices[i]
    if total_spent + price <= budget:
        total_spent += price
        bought_items.append(int(price) if price.is_integer() else price)
        status = "buy"
    else:
        status = "cannot buy"
    
    formatted_price = int(price) if price.is_integer() else price
    formatted_total = int(total_spent) if total_spent.is_integer() else total_spent
    
    print(f"Item {i+1} = {formatted_price} -> {status}")
    print(f"Current total = {formatted_total}\n")

remaining_budget = budget - total_spent

formatted_spent = int(total_spent) if total_spent.is_integer() else total_spent
formatted_remaining = int(remaining_budget) if remaining_budget.is_integer() else remaining_budget

print(f"Bought items: {bought_items}")
print(f"Total spent: {formatted_spent}")
print(f"Remaining budget: {formatted_remaining}")