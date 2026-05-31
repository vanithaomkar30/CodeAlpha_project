stock_prices={"AAPL":180,"TSLA":250,"gOOGL":150,"MSFT":420}
total_investment=0
n=int(input("Enter the number of stocks: "))
portfolio={}
for i in range(n):
    stock_name=input("Enter the stock name:").upper()
    if stock_name in stock_prices:
        quantity=int(input("Enter quantity: "))
        portfolio[stock_name]=quantity
        investment=stock_prices[stock_name]*quantity
        total_investment+=investment
    else:
        print("stock not found")
    print("\n------Portfolio summary------")
    for stock,quantity in portfolio.items():
        print(f"{stock}: {quantity} shares x ${stock_prices[stock]}=${stock_prices[stock]*quantity}")
    print(f"total investment: ${total_investment:.2f}")
    #save result to text file
    with open("portfolio.txt","w")as file:
        file.write("stock portfolio summary\n")
        file.write("-------------------------\n")
        for stock,quantity in portfolio.items():
            file.write(f"{stock}: {quantity} shares x ${stock_prices[stock]}= ${stock_prices[stock]*quantity}\n")
        file.write(f"\nTotal Investment value =${total_investment}")
    print("portfolio saved to portfolio.txt")   