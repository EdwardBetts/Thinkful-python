from optparse import OptionParser
import sys

meal_base = sys.argv[1]
tax_rate = sys.argv[2]
tip_rate = sys.argv[3]

def get_float(msg):
    while True:
        try:
            num = float(raw_input(msg))
            print "Invalid input, try again"
        except ValueError:
            continue;
    return num

'''

try:
    meal_base = float(sys.argv[1])
except ValueError:
    print("Not a valid integer! Please try again ...")
    meal_base = float(raw_input("meal base amount"))
try:
    tax_rate = float(sys.argv[2])
except ValueError:
    print("Not avalid integer! Please try again ...")
    tax_rate = float(raw_input("tax rate"))
try:
    tip_rate = float(sys.argv[3])
except ValueError:
    print("Not a valid integer! Please try again ...")
    tip_rate = float(raw_input("tip rate"))
'''
def calculate_rate(base, percentage):
    return base * percentage
 
def calculate_meal_costs(meal_base, tax_rate, tip_rate):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(meal_base, tax_rate)
    meal_with_tax = tax_value + meal_base
    tip_value = calculate_rate(meal_with_tax, tip_rate)
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=meal_base,
                    tax_rate=tax_rate,
                    tip_rate=tip_rate,
                    tax_value=tax_value,
                    total = total)
    return meal_info

def main():
    meal_info = calculate_meal_costs(meal_base, tax_rate, 
                                    tip_rate)
 
    print "The base cost of your meal was ${0:.2f}.".format(meal_info['meal_base'])
    print "You need to pay ${0:.2f} for tax.".format(meal_info['tax_value'])
    print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                        int(100*meal_info['tip_rate']), 
                                        meal_info['tax_value'])
    print "The grand total of your meal is ${0:.2f}.".format(meal_info['total'])
 
if __name__ == '__main__':
    main()