# Example:

# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']
# Joining a string is simple:

# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 
# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# Function Description

# Complete the split_and_join function in the editor below.

# split_and_join has the following parameters:

# string line: a string of space-separated words
# Returns

# string: the resulting string
# Input Format
# The one line contains a string consisting of space separated words.

# Sample Input

# this is a string   
# Sample Output

# this-is-a-string

def split_and_join(line):
    line1 = line.split(" ")
    print(line1)
    print('-'.join(line1))    
split_and_join("this is a string")