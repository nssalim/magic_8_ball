# Control Flow - Python
# Project 1 - Magic 8-Ball


#import random module in order to use its functions.
import random

#declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball their fortune
name = "Dr Watson"

question = "Will we solve this crime?"
answer = ""

#use the .randint() function from the random module to 
# generate a random number between 1 (inclusive) and 10 (inclusive). 
random_number = random.randint(1, 10)

#add a print() statement, then run program several times to ensure random values are generated as expected.
#print(random_number)

#utilize CONTROL FLOW using an if/elif/else statement to assign different answers for each randomly generated value.
if random_number == 1:
  answer = "Yes - definitely!"
elif random_number == 2:
  answer = "It is decidedly so!"
elif random_number == 3:
  answer = "Without a doubt!"
elif random_number == 4:
  answer = "Reply hazy, try again!"
elif random_number == 5:
    answer = "Ask again later!"
elif random_number == 6:
  answer = "Better not tell you now!"
elif random_number == 7:
  answer = "My sources say no!"
elif random_number == 8:
  answer = "Outlook not so good!"
elif random_number == 9:
  answer = "Very doubtful!"
elif random_number == 10:
  answer = "Signs point to yes!"
else:
  answer = "Error!"

#output the asker’s name (if provided) and their question
#if len(name) == 0
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

#output the Magic 8-Ball’s answer (depending on whether question a has been asked)
if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
  print("Sherlock Holmes\' answer: " + answer)
