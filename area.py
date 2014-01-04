def area_options():
	print "Options:"
	print " 'p' print options"
	print " 's' area of a square"
	print " 't' area of a rectangle"
	print " 'c' area of a circle"
	print " 'q' quit program"

def square_area(l):
	return l ** 2

def rectangle_area(w,h):
	return w * h

def circle_area (r):
	return 3.14 * (r ** 2)

def get_positive(msg):
    num = input(msg)
    while num < 0:
        print "ERROR! must be positive"
        num = input(msg)
    return num

area_options()
option = raw_input("Choose option: ")
while option != "q":
    if option == "s":
        print square_area(get_positive("Square side length: "))
        option = raw_input("Choose option: ")
    elif option == "t":
        print rectangle_area(get_positive("rectangle width: "),get_positive("rectangle height: "))
        option = raw_input("Choose option: ")
    elif option == "c":
        print circle_area(get_positive("circle radius: "))
        option = raw_input("Choose option: ")











