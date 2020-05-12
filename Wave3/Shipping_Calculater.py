def shipping_calculator(NumberofItems):
    return (NumberofItems - 1) * 2.95 + 10.95

NumberofItems = float(input("Please enter the number of items: "))

print("Total shipping charge: $", shipping_calculator(NumberofItems))