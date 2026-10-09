# Take price of 3 products as input (eg -> 99.5, 23.75, 16.15)
# • print the total Bill amount
# • print the average price


price1 = float(input("enter price product of 1: "))
price2 = float(input("enter price product of 2: "))
price3 = float(input("enter price product of 3: "))

total = price1 + price2 + price3
avg = total/3

print('total' ,total)
print('avg' ,avg)

