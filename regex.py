import re # has all regex expressions

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # use raw strings in regex
    # in this expression, \d represents a number, and we're looking for a phone number pattern
match = phoneNumRegex.search(str) # finds first occurence of str, returns match object
print(match.group()) # returns first matched subgroup
    # using int paramter allows you to output only specific groups of regex(which is specified by parentheses)
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    print(match.group(1)) # returns '\d\d\d'
    # int parameter starts with 1, 0 will return whole match
# if you want all matches, use findall
print(phoneNumRegex.findall(str)) # finds all occurences of str
    # returns list of strings, for regex w/ 0 or 1 groups
    # returns list of tuples, for regex w/ more than 1 group
# Groups: use () to specify groups in regex, which can be targetted using .group(n)
    # to search for literal () in regex, use \ before each
# Pipe(|): allows for mult possible values
re.compile(r'Bat(man|mobile|copter)')

# Not finding a match returns the None value

# Repetition
# ? matches 0 or 1 time
batRegex = re.compile(r'Bat(wo)?man') # matches Batman or Batwoman
# * matches 0 or more times
# + matches 1 or more times
# {x} matches exactly x number of times
# {x, y} matches a range from at least x and at most y, instead of a specific number
    # leaving out either first or second parameter includes range up to beginning/end

# By default, regex do greedy matches in Python
# to get nongreedy match for ranges, use ?
re.compile(r'(\d) {3,5}?') # will try to get shortest match possible(close to 3)

# Character classes
\d # 0-9
\D # not 0-9
\w # any letter, number or underscore(match "word" characters)
\W # not letter, number or underscore
\s # any space, tab or newline
\S # not space, tab or newline
# creating own character class:
# wrap chars in []
re.compile(r'[aeiou]')
# ^ is negative character class; matches everything not in class
re.compile(r'[^aeiou]')
