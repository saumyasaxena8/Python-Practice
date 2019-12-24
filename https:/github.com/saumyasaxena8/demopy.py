import random
import sys
import os
'''
print("Hello World")

# Comment


name = "Saumya"
print(name)


Main Data types in Python
1) Numbers
2) Strings
3) Lists
4) Tuples
5) Dictionaries


7 different arithematic operators
+ - * / % ** //


print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)

quote = "\"Always remember you are unqiue"

#multi_line_quote = just
#like everyone else

new_string = quote + multi_line_quote
print(new_string)

print("%s %s %s" % ('I like the quite', quote, multi_line_quote))
#print('\n' * 5)

print("I don't like", end  = " ")
print("new lines")



# List

grocery_list = ['Juice', 'Tomatoes', 'Bananas', 'Potatoes']
print('First Item is', grocery_list[0])
grocery_list[0] = 'Green Juice'
print('First new Item is', grocery_list[0])
print(grocery_list[1:3]) #starting from second to third since the index 3 is not included
other_events = ['Wash car', 'Pick up kids', 'Cash Check']
to_do_list = [other_events, grocery_list]

print(to_do_list)
print((to_do_list[1][1]))

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1, 'Pickle')
print(to_do_list,'added pickle')
grocery_list.remove('Pickle')
print(to_do_list,'removed pickle')
grocery_list.sort()
print(to_do_list,'sorted ')
grocery_list.reverse()
print(to_do_list,'reversed')

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))


# Tuples = unlike lists we will not be able to change the tuple once it is created

pi_tuple = (1,2,3,6,5,7,4)

new_list = list(pi_tuple)
new_tuple =  tuple(new_list)

print(len(new_tuple))
print(min(new_tuple))
print(max(new_tuple))

# Dictionaries or maps
# it is made up with values with unique keys with each value
# cannot join dictionaries together

super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Sam Scudder',
                  'Mirror Master' : 'Mark Mardon',
                  'Pied Piper' : 'Thomas Peterson'}

print(len(super_villains))
print(super_villains['Captain Cold'])
print(super_villains['Pied Piper'])

del super_villains['Fiddler']

super_villains['Pied Piper'] =  'Hartley Rathaway'
print(len(super_villains))

print(super_villains.get('Pied Piper'))

print(super_villains.values())
print(super_villains.keys())


# Conditionals

# if else elif == != > >= <=

age = 30

if age > 16 :
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

if age >= 21 :
    print('You are old enough to drive a tractor')
elif age >= 16 :
    print('You are old enough to drive a car')
else :
    print('You are old enough')

# Logical Operator
# and or not

if ((age >= 1) and (age <= 18)) :
    print('You get a birthday')
elif (age == 21 ) or (age >= 65):
    print('You get a birthday')
elif not(age == 30):
    print('You dont get a birthday')
else :
    print('You get a birthday Yayy')


#Looping

for x in range(0, 10):
    print(x, ' ', end = " ")

print('\n')

grocery_list = ['Juice', 'Tomatoes', 'Bananas', 'Potatoes']

for y in grocery_list:
    print(y)

for x in [2,4,6,8,10]:
    print(x)

num_list = [[1,2,3], [10,20,30], [100,200,300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

i = 0;

while(i <= 20):
    if(i %2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue

    i += 1


# Functions

def addnumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

string = addnumber(1,4)
print(string)

# User Input
#print('what is your name')
#name = sys.stdin.readline()

#print('Hello', name)

# String Functions

long_string = "I'll call you if you fall - The Floor"
print(long_string[0:4])

print(long_string[-5:])

print(long_string[:-5]) #upto the last five characters

print(long_string[:4] + ' be there')

print('%c is my %s letter and my number %d number is %d number is %.5f' %
      ('X', 'favorite', 1, .14))

'''












