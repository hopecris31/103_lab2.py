# story.py - a program that creates a great story
# N.Webb
# September 2017



one = "There once was a terrifying creature called"
two = "that ruled the land, using the power of their"
three ="One day"
four = "was challenged by a mighty intellectual academic, called"
five = "easily defeated"
six = "and took the"
seven = "to bring peace throughout the land"

#******************************
# DEFINE YOUR VARIABLES BELOW *
#******************************


#NJW No need to make these strings. They already are!

#monster = str('Dragon')
#weapon = str('Ruby Sword')
#heroine =str('Santa')


monster = input('Type monster name: ')
weapon = input('Type weapon name: ')
heroine = input('Type hero name: ')





# Part 1

print(one,monster,two,weapon,".",three,monster,four,heroine,".",heroine,five,monster,six,weapon,seven,".")

#This code is feasible, but difficult to read and edit mistakes.  

# Part 2

new = one + " " + monster + " " + two + " " + weapon+". " + three + " " + monster + " " + four + " " + heroine + ". " + heroine + " " + five + " " + monster + " " + six + " " + weapon + " " + seven+"."
print(new)

#This code is better because it is much cleaner and easier to read. If there were an error, it would be easier to find and correct. Also, spaces are added as strings, making it easier to read comapred to the last one. 
