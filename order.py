print(" Welcome to TEA Shop")

print("1. TEA - ₹10")
print("2. MILK - ₹15")
print("3. GREEN TEA - ₹15")

choice = int(input("Select your tea (1-3): "))

if choice == 1:
    item = "TEA"
    price = 10
elif choice == 2:
    item = "MILK"
    price = 15
elif choice == 3:
    item = "GREEN TEA"
    price = 15
else:
    print("Invalid choice!")
quantity = int(input("Enter quantity: "))
total = price * quantity
print("\n$ BILL $")
print("Item:", item)
print("Quantity:", quantity)
print("Total Amount: ₹", total)
print("Thank you for your order! ")