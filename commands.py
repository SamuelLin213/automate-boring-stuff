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

# Lists = arrays in other OOP
# array of elements inside [], separated by comma
# can embed list within list
# can use negative integer to refer to elements starting from end
# slice
listVar[start:end] # returns list of values from start to end-1(doesn't include end)
	# can leave out one of start/end values, to represent from start/to end
# deleting from list
del listVar[n]
# Can get list length using len()
len(listVar)
# Can also use concatenation and multiplication w/ lists
# Convert to list using list()
list("Hello") # returns ['H', 'e', 'l', 'l', 'o']
# Use the in keyword to check if elem exists in list
42 in ["hello"] # False
# Alternatively, use not in to check for absence of elem
"hello" not in ["hello"] # False
# Mult assignment
var1, var2 = listVar # stores listVar[0] into var1 and listVar[1] into var2
# Methods
listVar.index(elem) # returns index of elem in list, returns exception if not found, dup elem will return first occurence
listVar.append(elem) # adds elem to end of list
listVar.insert(n, elem) # inserts elem at index n
listVar.remove(elem) # removes elem from list regardless of index, nonexistent elem returns exception
listVar.sort() # sorted in ascending order, can't sort mixed values, uppercase comes before lowercase
	listVar.sort(reverse=True) # sorts in reversed order
# comparison w/ string:
	# string is immutable, while list is mutable
		# need to splice string and set to new var(using [:] format)
	# list uses reference so changing var value will affect all copies
		# immutable types don't have this concern, as they can only be replaced by new values
# doing deep copy
import copy
newList = copy.deepcopy(listVar) # creates new deep copy and stores in newList

# line continuation
# when initializing list, can use multiple lines w/o worrying abt indents
# another method of line continuation is to use \

# Dictionaries: maps in other OOP
