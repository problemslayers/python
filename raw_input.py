# Get username

username = raw_input('Enter username: ')
print ("Your username is %s.") % username

# Show Menu

print (30 * '*')
print ("   M A I N - M E N U")
print (30 * '*')
print ("1. Backup")
print ("2. User Management")
print ("3. Reboot the server")
print (30 * '*')

## Without error handling
## Just get input
#
#choice = raw_input('Enter choice [1-3]: ')
#
## Convert string to int type
#
#choice = int(choice)


# Robust error handling - only accept int
# Wait for valid input in while-not

is_valid=0

while not is_valid :
		try :
				choice = int (raw_input('Enter your choice [1-3]: '))
				is_valid = 1  # set to 1 to validate input and terminate the while-not
		except ValueError, e :
				print ("'%s' is not a valid integer." % e.args[0].split(": 															")[1])

#Take action as per selected menu option

if choice == 1:
		print ("Starting backup...")
elif choice == 2:
		print ("Starting user management...")
elif choice == 3:
		print ("Rebooting the server...")
else:
		print ("Invalid number. Try again...")
