meal = 100.00
tax = 0.20
tip = 0.10

tax_value = tax * meal
meal_with_tax = meal + tax_value
tip_value = meal * tip
total = meal_with_tax + tip_value

print meal
print tax_value
print tip_value
print total

'''
meal = raw_input(meal cost before tax)
tax = raw_input(tax charged)
tax = raw_input(tax charged)
tip = 0.1 * 100

tax_value = ({:.2f}.format(tax))
meal_with_tax = ({:.2f}.format(meal)) + tax_value
tip_value = raw_input("how much is the tip?")
total = meal_with_tax + tip_value

print meal
print tax_value
print tip_value
print total
'''