# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
coffee = int(input("Enter coffee quantity:"))
muffin = int(input("Enter muffin quantity:"))
water = int(input("Enter water quantity:"))

coffee_price= 3.50
muffin_price= 2.10
water_price= 1.05

total_coffee= float(coffee_price*coffee)
total_muffin= float(muffin_price*muffin)
total_water= float(water_price*water)

subtotal = total_coffee + total_muffin + total_water
tax = float(0.06*subtotal)
total = subtotal + tax

item = "==========RECEIPT==========\nItem\tPrice\tQty\tTotal"
print (f"{item}\nCoffee\t{coffee_price}\t{coffee}\t{total_coffee}\nMuffin\t{muffin_price}\t{muffin}\t{total_muffin}\nWater\t{water_price}\t{water}\t{total_water}\n----------------------------\nSubtotal\t\t{subtotal}\nTax (6%)\t\t{tax}\nTotal\t\t\t{total}\n============================")