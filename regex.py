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

# ^ used to indicate beginning substring
re.compile(r'^Hello!') # string starts w/ Hello!
# $ used to indicate ending substring
re.compile(r'world!$') # string ends w/ world!
# Use combination of ^ and $ to match entire string

# wildcard . means any character except newline
# common use: .* matches any pattern
    # Ex: splice out name from string
    nameRegex = re.compile(r'First name: (.*) Last name (.*)') # using findall() returns list of the first and last name match
# greedy vs nongreedy: .* and .*?, respectively
# You can modify the .* search with a 2nd parameter to .compile()
    # for .* to match EVERYTHING(including \n), pass in re.DOTALL
    re.compile(r'.*', re.DOTALL) # includes newline in match
    # To ignore case, use re.IGNORECASE
    re.compile(r'.*', re.I) # short-form of above
    # Use | character to pass in multiple parameter
    re.compile(r'.*', re.I | re.DOTALL)

namesReg = re.compile(r'Agent \w+')
namesReg.sub('REACTED', 'Agent Alice gave info to Agent Bob') # replaces Agent Alice and Agent Bob to REACTED
# You can use groupings to display just first letter of name
namesReg = re.compile(r'Agent (\w)\w*') # places first letter of name into group
namesReg.sub(r'Agent \1*****', 'Agent Alice gave info to Agent Bob') # Displays only first group, which is the first letter of name

# Verbose mode; allows you to add comments inside and ignore whitespace, increase readability
re.compile(r'''
(\d\d\d-) | # area code w/o parens
(\(\d\d\d\)) # or area code w/ just parens
''', re.VERBOSE)
