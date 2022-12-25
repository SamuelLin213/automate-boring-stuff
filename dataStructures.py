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

# Dictionaries: maps in other OOP
# key-value pairs
# items in dictionary are unordered
dict = {'key': 'val', 'key2': 'val2'}
dict['key'] # returns 'val'
# use in and not in to check if key is in dict
'key' in dict # true
'key' not in dict # false
# dict commands
list(dict.keys()) # returns list of keys
list(dict.values()) # return list of values
list(dict.items()) # returns list of objects
# use alongside for loops:
for k, v, in dict.items():
	print(k, v)
# use get() method to retrieve value from dict, using fallback if not found
dict.get('key', null)
# opposite of get() is setdefault() method, which sets pair only if key doesn't exist
dict.setdefault('key3', 'val3') # if key3 already existed, does nothing
# use pprint module to print out formatted
import pprint
pprint.pprint(dict) # newlines and ordered
pprint.pformat(dict) # returns string of pprint format

# Advanced string manipulation
# Two ways to specify string: '' and ""
# Use escape character \ to include ' or " in string
# Use ''' or """ to indicate multiline string
# String methods
	str.upper() # returns uppercase of string
	str.lower() # returns lowercase of string
	str.title() # converts words to titlecase
	str.isupper()
	str.islower()
	str.isalpha() # checks if letters only
	str.isalnum() # letters and nums only
	str.isdecimal() # numbers only
	str.isspace() # whitespace only
	str.istitle() # titlecase only(all words' first letter are capitalized)
	str.startswith('str')
	str.endswith('str')
	' '.join(strList) # joins strings in list with ' '
	str.split(' ') # splits string into list with ' '
	str.ljust(10, '*') # adds whitespace on right to make string a length of 10, specify filling char as *
	str.rjust(10) # adds whitespace on left to make string a length of 10, default filling char of whitespace
	str.center(10) # centers the text in length 10
	str.strip() # trims off whitespace on both sides
		str.strip('sTr') # strips chars s, T and r from both sides
		str.lstrip()
		str.rstrip()
	str.replace('e', 'XYZ') # replaces all e's w/ XYZ
# string formatting
# Like printf in C
'Hello %s, I\'m %s' % ("there", "Sam")
