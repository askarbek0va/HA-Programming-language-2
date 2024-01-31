import os
a=input('What is the user\'s name? ')
b=input('What is the user\'s age? ')
c=input('What is the user\'s country of birth? ')
d=input('What is the user known for? ')
os.system('clear')
user={ 
    'What is the user\'s name?':a,
    'What is the user\'s age?': b,
    'What is the user\'s country of birth?':c,
    'What is the user known for?': d
}
print(user)
for x, y in user.items():
  print(x, y)