# Regular Expressions Practice Examples

# --------------------------------------------------
# Example 1 - findall() method returns all matches in a list
import re
txt = 'the rain in Spain'
x = re.findall('in', txt)
print(x)

# --------------------------------------------------
# Example 2 - search() returns match object (index position of first occurrence)
import re
txt = 'the rain in Spain'
x = re.search('in', txt)
print(x)

# --------------------------------------------------
# Example 3 - Matching digits using character set
import re
txt = 'th1re is r4in in Spain'
x = re.findall('[1-5]', txt)
print(x)
x = re.search('[1-5]', txt)
print(x)

########################################################################################################
'''
Character Classes Summary:

.              Any character except newline
[abc]          Any one of a, b, or c
[^abc]         Any character except a, b, or c
[a-z]          Any lowercase letter
[A-Z]          Any uppercase letter
[0-9]          Any digit
[a-zA-Z0-9]    Any alphanumeric character
'''

# [abc] list of all matching characters
import re
txt = 'the rain in Spain'
x = re.findall('[abcsp]', txt)
print(x)

# [^abc] characters except the specified ones
import re
txt = 'the rain in Spain'
x = re.findall('[^abcsp]', txt)
print(x)

# [a-z] lowercase letters
import re
txt = 'the rain in Spain'
x = re.findall('[a-z]', txt)
print(x)

# [A-Z] uppercase letters
import re
txt = 'the rain in Spain'
x = re.findall('[A-Z]', txt)
print(x)

# [A-Za-z] both uppercase and lowercase
import re
txt = 'the rain in Spain'
x = re.findall('[A-Za-z]', txt)
print(x)

# [0-9] digits only
import re
txt = 'the 0ra1n in 9pain'
x = re.findall('[0-9]', txt)
print(x)

# [a-zA-Z0-9] alphanumeric only
import re
txt = 'the rain in $ Spain 0911'
x = re.findall('[a-zA-Z0-9]', txt)
print(x)

# --------------------------------------------------
# Quantifiers
'''
?     0 or 1 times
+     1 or more times
*     0 or more times
{N}   Exactly N times
{N,}  N or more times
{X,Y} Between X and Y times
'''

'''
\A  Start of string (not multiline)
\Z  End of string (not multiline)
^   Start of line (multiline)
$   End of line (multiline)
'''

'''
\A     Match at start of string
\b     Match at word boundary
\B     Match not at word boundary
\d     Match any digit
\D     Match non-digit
\s     Match whitespace
\S     Match non-whitespace
\w     Match word character (a-z, A-Z, 0-9, _)
\W     Match non-word character
\Z     Match at end of string
'''

# -----------------------------
# Some matching examples

import re
txt = 'hi,hello how are u'
x = re.findall('h..lo', txt)
print(x)

# ^ start match
import re
txt = 'there is rain in Spain'
x = re.findall('^t', txt)
print(x)

# $ end match
import re
txt = 'there is rain in Spain'
x = re.findall('n$', txt)
print(x)

# Using . + * quantifiers
import re
txt = 'hi,hello how are you'
x = re.findall('he.*lo', txt)
print(x)

import re
txt = 'hi how are you hello'
x = re.findall('he.+o', txt)
print(x)
x = re.findall('y.+u', txt)
print(x)
x = re.findall('y.?u', txt)
print(x)
x = re.findall('he.{2}o', txt)
print(x)
x = re.findall('he.{3}o', txt)
print(x)

# --------------------------------------------------
# 28/01/25

# \A
import re
txt = 'the rain in Spain'
x = re.findall(r'\Athe', txt)
print(x)

# \b start of word
import re
txt = 'if there is rain in Spain'
x = re.findall(r'\bthe', txt)
print(x)

# \b end of word
import re
txt = 'if there is rain in Spain'
x = re.findall(r'ain\b', txt)
print(x)

# \B not at start of word
import re
txt = 'if there is rain in Spain'
x = re.findall(r'\Bhe', txt)
print(x)

# \B not at end of word
import re
txt = 'if there is rain in Spain'
x = re.findall(r'he\B', txt)
print(x)

# \d digits only
import re
txt = 'if there is 10 rain $spain'
x = re.findall(r'\d', txt)
print(x)

# \D non-digit
import re
txt = 'if there is 10 rain $spain'
x = re.findall(r'\D', txt)
print(x)

# \s spaces
import re
txt = 'if there is 10 rain $spain'
x = re.findall(r'\s', txt)
print(x)

# \S non-space
import re
txt = 'if there is 10 rain $spain'
x = re.findall(r'\S', txt)
print(x)

# \w word characters
import re
txt = 'if there is 10 rain $spa_in'
x = re.findall(r'\w', txt)
print(x)

# \W non-word characters
import re
txt = 'if there is 10 rain $spa_in'
x = re.findall(r'\W', txt)
print(x)

# \Z end of string
import re
txt = 'ifels there is 10 rain Spain'
x = re.findall(r'pain\Z', txt)
print(x)

# \A start of string
x = re.findall(r'\Aif', txt)
print(x)

# Example using search() with group, span
import re
txt = 'if there is 10 rain Spain'
x = re.search(r'\bS\w+', txt)
print(x.span())
print(x.start())
print(x.group())
print(x.string)
