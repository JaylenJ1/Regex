#!/usr/bin/env python
# coding: utf-8

# # Regular Expressions

# # Tasks today:
# 1) <b>Importing</b> <br>
# 2) <b>Using Regular Expressions</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) re.compile() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) re.match() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) re.findall() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) re.search() <br>
# 3) <b>Sets</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Integer Ranges <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Character Ranges <br>
# 4) <b>Counting Occurences</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) {x} <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) {, x} <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) {?} <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) {*} <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) {+} <br>
# 5) <b>In-Class Exercise #1</b> <br>
# 6) <b>Escaping Characters</b> <br>
# 7) <b>Grouping</b> <br>
# 8) <b>In-Class Exercise #2</b> <br>
# 9) <b>Opening a File</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) open() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) with open() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) re.match() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) re.search() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Store the String in a Variable <br>
# 10) <b>Regex Project</b> <br>

# ### Importing <br>
# <p>Regular Expressions are universal throughout most programming languages... They are generally imported through the module 're'.</p>

# In[2]:


# import re
import re


# ### Using Regular Expressions <br>
# <p>Regular expressions give us the ability to search for patterns within text, strings, files, etc. They serve several uses, such as; security measures, searching, filtering, pattern recognition, and more...</p>

# ##### re.compile()

# In[4]:


# using compile, pre determines the string to be used in regular expression methods
pattern = re.compile('abcd')


# ##### re.match()

# In[6]:


match = pattern.match('abcd123')
print(match)
print(type(match.span()))
# Accessing the span of the match


# ##### re.findall()

# In[7]:


finders = pattern.findall('123abcd abcd123 abcd abcabd acd')
print(finders)
help(re.findall)


# ##### re.search()

# In[14]:


random_string = '123 123 234 abcd abd'
search = pattern.search(random_string)
print(search)
span = search.span()
print(span)
print(random_string[span[0] : span[1]])


# ### Sets <br>
# <p>The following cells will allow you to use regular expressions to search for certain values within a range such as numbers 1 through 4.</p>

# ##### [a-z] or [A-Z] - any lowercase/uppercase letters from a to z<br/>[^2] - anything that's not 2

# ##### Integer Ranges

# In[16]:


pattern_int = re.compile('[0-7]')

random_numbers = pattern_int.search('67383')
print(random_numbers)
span = random_numbers.span()
print(span)


# ##### Character Ranges

# In[17]:


char_pattern = re.compile('[A-Z][a-z]')
found = char_pattern.findall('Hello there Mr.Anderson')
print(found)


# ### Counting Occurences

# ##### {x} - something that occurs {num_of_times}

# In[20]:


char_pattern_count = re.compile('[A-Z][a-z][0-3]{2}')

found_count = char_pattern_count.findall('Hello Mr.An03derson')

print(found_count)


# ##### {x, x} - something that occurs between x and y times

# In[22]:


random_pattern = re.compile('m{1,5}')
random_statment= random_pattern.findall("This is an example of a regular expression trying to find one m, more if mmmmmm")
print(random_statment) 


# In[25]:


pattern_m = re.compile('Mrss?')

found_pat = pattern_m.findall("Hello M there Mr.Anderson, Mid How is Mrs.Anderson ")

print(found_pat)


# ##### ? - something that occurs 0 or 1 time

# In[26]:


pattern_m = re.compile('M*s')

found_m = pattern_m.findall("M name is Mrs.Smith this is Mssssss")
print(found_m)


# ##### * - something that occurs at least 0 times

# In[ ]:





# ##### + - something that occurs at least once

# In[28]:


pattern_again = re.compile('M+s')

found_m = pattern_again.findall('Mrs.Smith os this Mssssss')

print(found_m)


# ##### In-class exercise 1: 
# 
# Use a regular expression to find every number in the given string

# In[12]:


my_string = "This is has 10909090 numbers, but it only 1 string, I hope you solve this 2day."

# Output(10909090, 1 ,2)
number_pat = re.compile('10909090|[1-3]')

found_s = number_pat.findall( "This is has 10909090 numbers, but it only 1 string, I hope you solve this 2day.")

print(found_s)


# ### Escaping Characters

# ##### \w - look for any Unicode character<br/>\W - look for anything that isnt a Unicode character
# 
# [History on Unicode](http://unicode.org/standard/WhatIsUnicode.html)
# 
# [More on Unicode Characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters)

# In[5]:


pattern_1 = re.compile('[\w]+')
pattern_2 = re.compile('[\W]+')

found_1= pattern_1.findall('This is a sentance. With, exclamation mark at the end')
found_2= pattern_2.findall('This is a sentance. With, exclamation mark at the end')

print(found_1)

print(found_2)


# ##### \d - look for any digit 0-9<br/>\D - look for anything that isnt a digit

# In[13]:


pattern_nums = re.compile('\d{1,2}[a-z]{2}') 

found_date= pattern_nums.findall('Today is the 7th in 20 days it will be the 27th. 3rd, 1st,30th')
print(found_date)


# ##### \s - look for any white space<br/>\S - look for anything that isnt whitespace

# In[15]:


pattern_no_space = re.compile('\S[a-z]+')

pattern_space = re.compile('\s+')

found_space = pattern_space.findall('Are you afraid of the dark?')
print(found_space)

found_dark = pattern_no_space.findall('Are you afraid of the dark again?')
print(found_dark)


# ##### \b - look for boundaries or edges of a word<br/>\B - look for anything that isnt a boundary

# In[24]:


pattern_bound = re.compile(r'\bTheCodingTemple\b')
pattern_bound_none = re.compile(r'\BTheCodingTemple\B')

no_found_bound = pattern_bound_none.findall("TheCodingTemple")
print(no_found_bound)

found_bound = pattern_bound.findall("TheCodingTemple")
print(found_bound)


# ### Grouping

# In[29]:


my_string_again = "Max Smith, aaron rodgers, Sam Darnold, Lebron James, Micheal Jordan, Kevin Durant, Patrick McCormick"

#Group of Names Regex Compiler

pattern_name = re.compile('([A-Z][a-zA-Za-z]+) ([A-Z][A-Za-z]+)')

found_names= pattern_name.findall(my_string_again)
print(found_names)

for name in my_string_again.split(','):
    match = pattern_name.search(name)
    
    if match:
        print(match.groups(2))
    else:
        print("Not a name")


# ##### In-class Exercise 2:
# 
# Write a function using regular expressions to find the domain name in the given email addresses (and return None for the invalid email addresses)<br><b>HINT: Use '|' for either or</b>

# In[ ]:





# In[5]:


my_emails = "jordanw@codingtemple.orgcom pocohontas1776@gmail.com helloworld@aol..com yourfavoriteband@g6rn.org @codingtemple.com"

pattern_email = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
# You can also use the $ at the end of your compile expression -- this stops the search

#.com OR .org => com|org

found_emails = pattern_email.findall(my_emails)
#Expected output:
#None
#pocohontas1776@gmail.com
#None
#yourfavoriteband@g6.org
#None




# ### Opening a File <br>
# <p>Python gives us a couple ways to import files, below are the two used most often.</p>

# ##### open()

# In[35]:


f = open("names.txt")

date = f.read()

print(date)

f.close()


# ##### with open()

# In[36]:


with open('names.txt') as f:
    data = f.read
    print(data)


# ##### re.match()

# In[37]:


print(re.match(r'Hawkins, Derek', date))


# ##### re.search()

# In[38]:


print(re.search(r'ripalp@codingtemple.com', date))


# ##### Store the String to a Variable

# In[42]:


answer = input("What would you like to search for? ")

found = re.findall(answer, date)
if found:
    print(f'I found your data:{found}')
else:
    print("Nothing Found")
    


# ### In-Class Exercise #3 <br>
# <p>Print each persons name and twitter handle, using groups, should look like:</p>
# <p>==============<br>
#    Full Name / Twitter<br>
#    ==============</p>
# Derek Hawkins / @derekhawkins
# 
#  Erik Sven-Osterberg / @sverik
# 
#  Ryan Butz / @ryanbutz
# 
#  Example Exampleson / @example
# 
#  Ripal Pael / @ripalp
# 
#  Darth Vader / @darthvader

# In[10]:


my_list_1 = " Derek Hawkins/@derekhawkins, Erik Sven-Osterberg/@sverik, Ryan Butz/@ryanbutz, Example Exampleson/@example, Ripal Pael/@ripalp, Darth Vader/@darthvader "

pattern_handle = re.compile(([A-Za-z]+ [A-Za-z]+))

found_names= pattern_handle.findall(my_list_1)
print(found_names)


for name in my_list_1:
    match = pattern_handle.search(name)
    
    if match:
        print(match.groups(2))
    


# 
# ### Regex project
# 
# Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)
# ##### Hint: use with open() and readlines()

# In[ ]:


"""
Expected Output
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""


# In[ ]:




