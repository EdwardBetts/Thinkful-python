'''
meal = 100.00
tax = 0.20
tip = 0.10

tax_value = tax * meal
meal_with_tax = meal + tax_value
tip_value = meal * tip
total = meal_with_tax + tip_value

print "${0:.2f}".format(meal)
print "${0:.2f}".format(tax_value)
print "${0:.2f}".format(tip_value)
print "${0:.2f}".format(total)

'''
meal = float(raw_input("meal cost before tax"))
tax = float(raw_input("tax rate"))
tip = float(raw_input("tip rate"))

tax_value = tax * meal
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "${0:.2f}".format(meal)
print "${0:.2f}".format(tax_value)
print "${0:.2f}".format(tip_value)
print "${0:.2f}".format(total)

print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(int(100*tip), tip_value)