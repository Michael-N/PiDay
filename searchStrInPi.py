'''
Code by Michael Naguib ... Day after Pi Day 2020
... I want to find my phone number in Pi ... could not find it in 1mil
using online searchers ... ill write my own
'''

# Note .... I do not pretend this is efficient ... it is not ... it is brute force ... 
print("loading File")
with open("pi-billion.txt","r") as f:
    lines = f.read()
    print("Searching for #")
    searchStr='919'
    location = lines.find(searchStr)
    print("{0} Digit of Pi starts {1}".format(location+1,searchStr))