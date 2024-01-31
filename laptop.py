laptop={'brand':'dell' , 'model':'alienware', 'year': 2010}
#1
print(laptop['brand'])
#2
laptop['home']=True
print(laptop)
#or we can also use update() method to add new information
laptop.update({'home': True})
print(laptop)
#3
laptop['year']=2018
print(laptop)