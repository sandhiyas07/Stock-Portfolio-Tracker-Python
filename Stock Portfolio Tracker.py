stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150
}

stock = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock in stocks:
    total = stocks[stock] * quantity
    print("Total Investment Value: $", total)

    with open("portfolio.txt", "w") as file:
        file.write(f"Stock: {stock}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Value: ${total}\n")

    print("Saved to portfolio.txt")
else:
    print("Stock not found")