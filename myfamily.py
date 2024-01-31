myfamily = ('mother', 'father', 'sister', 'brother', 'sister')
print(myfamily)
#1
print(type(myfamily))
#2
print(myfamily[2])
print(myfamily[-1])
#3
x=list(myfamily)
x.append('me')
myfamily=tuple(x)
print(myfamily)
#4 We can not use the pop() method to remove the items, but we can use the remove() method to remove items.
# If we use pop() method it will raise an error.
y=list(myfamily)
y.remove('brother')
myfamily=tuple(y)
print(myfamily)