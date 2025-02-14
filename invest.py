invest = 365 // 10
profit = 1000
for i in range(invest):
    print(f"====Iteration {i + 1}====")
    print(f"{profit} + {profit}", end="")
    profit +=profit
    print(f" = {profit}")
    print()
print(f"Total Profit is: {profit}")