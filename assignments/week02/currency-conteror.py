EXCHANGE_RATE = 35.5

print("--- Currency Converter ---")
print("1: THB to USD")
print("2: USD to THB")

choice = input("Choose conversion direction (1 or 2): ")

if choice == "1":
    amount = float(input("Enter amount in THB: "))
    result = amount / EXCHANGE_RATE
    
    print("\n--- Result ---")
    print(f"Formula used: {amount:.2f} THB / {EXCHANGE_RATE} = {result:.2f} USD")
    print(f"Converted Amount: {result:.2f} USD")

elif choice == "2":
    amount = float(input("Enter amount in USD: "))
    result = amount * EXCHANGE_RATE
    
    print("\n--- Result ---")
    print(f"Formula used: {amount:.2f} USD * {EXCHANGE_RATE} = {result:.2f} THB")
    print(f"Converted Amount: {result:.2f} THB")

else:
    print("Invalid choice. Please run the program again.")