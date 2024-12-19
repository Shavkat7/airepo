def invest(amount, rate, years):
    for i in range(1, years+1):
        print(f"year {i}: ${amount * (1 + rate)**i:.2f}")

amount1 = float(input("Enter initial amount:"))
rate1 = float(input("Enter percentage rate:"))
years1 = int(input("Enter number of years:"))
invest(amount1, rate1, years1)