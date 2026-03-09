# source: https://www.youtube.com/watch?v=FrvBwdAU2dQ

# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

#.(number)f = round to that many decimal places (fixed point)
print(f"Price 1 is ${price1:.2f}")
print(f"Price 1 is ${price2:.2f}")
print(f"Price 1 is ${price3:.2f}")
print("-------------------------")
# :(number) = allocate that many spaces
print(f"Price 1 is ${price1:10}")
print(f"Price 1 is ${price2:10}")
print(f"Price 1 is ${price3:10}")
print("-------------------------")
# :03 = allocate and zero pad that many spaces
print(f"Price 1 is ${price1:010}")
print(f"Price 1 is ${price2:010}")
print(f"Price 1 is ${price3:010}")
print("-------------------------")
# :< = left justify
print(f"Price 1 is ${price1:<10}")
print(f"Price 1 is ${price2:<10}")
print(f"Price 1 is ${price3:<10}")
print("-------------------------")
# :> = right justify
print(f"Price 1 is ${price1:>10}")
print(f"Price 1 is ${price2:>10}")
print(f"Price 1 is ${price3:>10}")
print("-------------------------")
# :^ = center align
print(f"Price 1 is ${price1:^10}")
print(f"Price 1 is ${price2:^10}")
print(f"Price 1 is ${price3:^10}")
print("-------------------------")
# :+ = use a plus sign to indicate positive value
print(f"Price 1 is ${price1:+}")
print(f"Price 1 is ${price2:+}")
print(f"Price 1 is ${price3:+}")
print("-------------------------")
# :  = insert a space before positive numbers
print(f"Price 1 is ${price1: }")
print(f"Price 1 is ${price2: }")
print(f"Price 1 is ${price3: }")
print("-------------------------")
# :, = comma separator
print(f"Price 1 is ${price1:,}")
print(f"Price 1 is ${price2:,}")
print(f"Price 1 is ${price3:,}")
print("-------------------------")
# mix & match flags
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 1 is ${price2:+,.2f}")
print(f"Price 1 is ${price3:+,.2f}")
print("-------------------------")
