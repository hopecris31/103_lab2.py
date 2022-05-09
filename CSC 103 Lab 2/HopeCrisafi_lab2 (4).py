#circle code - python - Lab 2
#Crisafi
#4/6/2021
#Partner: Samantha Sotland






cat = 7
mouse = 2.7
#mouse = float(2.7)
giraffe = 'mouse'
zebra = cat
cat = 28
#cat = str('28')
hippo = 2.3
sausage = int(mouse)
burger = str(hippo)
balloon = hippo
#balloon = int(hippo)

print('cat is: ', cat)
print('mouse is: ',mouse)
print('giraffe is: ',giraffe)
print('zebra is: ',zebra)
print('cat is: ',cat)
print('hippo is: ',hippo)
print('sausage is: ', sausage)
print('burger is: ',burger)
print('balloon is: ',balloon)

#1. When you change it to a string, the print function displays 28 without quotes or any indicator of a string.  However, when you just type the variable name and return, it shows up in quotes indicating the string.
#2. When you add int to balloon, it converts the variable to an integer, and 2.3 becomes 2.
#3. When you add float to mouse (2.7), nothing changes because the variable is already a float.




#NJW DO NOT leave code commented out if it satisfies
#NJW one of my requirements, please.

#name  = input('enter name: ')
#number = int(input('enter a number: '))
#print('Hello: ', name * number)

#name = input('enter first name: ')
#lastName = input('enter last name: ')

#NJW ' ' is already a string.

#fullName = name + str(' ') + lastName
#print(fullName)






#numberOne = input('enter a number: ')
#numberTwo = input('enter a second number: ')
#print('your numbers are: ',int(numberOne), str('and'), int(numberTwo))
#print('sum: ',(int(numberOne) + int(numberTwo)))
#print('difference: ',(int(numberOne) - int(numberTwo)))
#print('product: ',(int(numberOne) * int(numberTwo)))

numberOne = input('enter a number: ')
numberTwo = input('enter a second number: ')
numberThree = input('enter a third number: ')
numberFour = input('enter a fourth number: ')

#NJW It's better to MAKE it a number when we create it, rather then when we USE it.
#NJW See how many times you have to use the int fucntion?

total = int(numberOne) + int(numberTwo) + int(numberThree) + int(numberFour)
average = total / 4

print('your numbers are: ',int(numberOne), int(numberTwo), int(numberThree),'and',int(numberFour))
print(str('sum: '),int(total))
print('average: ', average)








#part 5

#step 1: set out a cutting board
#step 2: get a knife
#step 3: get bread
#Step 4: get peanut butter
#step 5: get jelly
#step 6: lay out two pieces of bread
#step 7: spread peanut butter on one slice
#step 8: spread jelly on the other slice
#step 9: put the two pieces of bread together
#step 10: cut in half

#this process took 10 instructions








