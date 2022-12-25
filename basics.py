# basics
print() # prints value
	# sep: determines separating values of multiple arguments
	# end: specifies ending charater(default is newline)
input() # gets input from user
len() # get length of string value
int() str() float() # converts value into data type

# flow chart
# boolean operators:
and or not
# control statements
if: elif: else: while: # can use "truthy" values; non-blank or non-zero values
bool() # gets the boolean val of expression
# other statements:
break # breaks out of cur loop
continue # next iteration of loop
# for loop
for i in range(num): # starts with i = 0 and goes up to num-1(< num)
# to specify range, use 2 arguments
for i in range(start, fin, step) # from start to end-1(< end), optional step parameter specifies step incrementation

# functions
def funcName(param):
	return val
# to force python to interpret local var as global, use keyword global inside func
def func():
	global var # var from global will stay global

# Handling errors
try:
	# some code
except ErrorName: # not specifiying error will catch all errors
	# handle error

# line continuation
# when initializing list, can use multiple lines w/o worrying abt indents
# another method of line continuation is to use \
