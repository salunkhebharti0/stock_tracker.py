# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300
}

portfolio = {}
total_investment = 0

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity for {stock}: "))
        investment = stock_prices[stock] * quantity
        portfolio[stock] = {
            'quantity': quantity,
            'investment': investment
        }
        total_investment += investment
    else:
        print("Stock not found in the price list.")

# Display the portfolio and total
print("\nYour Portfolio Summary:")
for stock, data in portfolio.items():
    print(f"{stock}: {data['quantity']} shares | Investment = ${data['investment']}")

print(f"\nTotal Investment: ${total_investment}")

# Save to file?
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as f:
        f.write("Your Portfolio Summary:\n")
        for stock, data in portfolio.items():
            f.write(f"{stock}: {data['quantity']} shares | Investment = ${data['investment']}\n")
        f.write(f"\nTotal Investment: ${total_investment}")
    print("Saved to portfolio_summary.txt")