n = int(raw_input("number of base leaves"))
trunk_character = str(raw_input ("select your trunk character")).strip()
leaf_character = str(raw_input ("select your leaf character")).strip()

'''
while 3<= n <= 21 and n % 2 == 1:
	print "  " + leaf_character + "  " + "\n" + leaf_character * n + "\n" + trunk_character * 3
	break
else:
	print "please enter an odd integer between 3 and 21 for base leaves"
	n = int(raw_input("number of base leaves"))

'''
count = 0
for i in range(1,n+1,+2):
	#print "  " + leaf_character + "  " + "\n" + trunk_character * 3
	space_count = " " * (((n-1)/2) - (i/2))
	print space_count + leaf_character * i
	count = count +1
print " " * ((((n-1)/2))-1) + trunk_character * 3

 
'''
def tree (n, trunk_character,leaf_character):
	return leaf_character * (n) +"\n"+ trunk_character * 3

while 3<= n <= 21:
	if n/2 ==1:
		print "hello"
	break
	else:
		print "please enter an odd integer between 3 and 21 for base leaves"
		n = int(raw_input("number of base leaves"))


def tree (n, trunk_character,leaf_character):
	while 3<= n <= 21:
		if n/2 ==1:
			return leaf_character * 2
		else:
			print "please enter an odd integer between 3 and 21 for base leaves"
			n = int(raw_input("number of base leaves"))
tree(n, trunk_character,leaf_character)

def tree (n, trunk_character,leaf_character):
	if 2 < n < 22 and n/2==1:
		print "  " + leaf_character + "  " + "\n" + leaf_character * n + "\n" + trunk_character * 3
	else:
		print "please enter an odd integer between 3 and 21 for base leaves"
		n = int(raw_input("number of base leaves"))
		tree (n, trunk_character,leaf_character)
'''