# This week we introduced functions
print ("Welcome to Multiplication Facts!")
# asknum is a function, so any time you want to ask the user to input a 
# number, you can call asknum() and an int will be returned to your program.
def asknum(word):
    raw_num = input("Number "+word)
    return int(raw_num)

# We initialize variables and use the 'asknum' function to get their values.
number1 = asknum("1: ")
number2 = asknum("2: ")

result = number1 * number2
# We have to initialize guess here with a value of 'None',
# then we create a 'while loop' that will run while the
# guess is a)None or b)not correct.  Once the user guesses 
# the correct answer, the 'while loop' will exit.
guess = None
while guess != result:
  guess = int(input("What do you think the answer is? "))
  if guess == result:
    print("AMAZING! :)")
  elif guess < result:
    print("Too low, try again...")
  else:
    print("Too high, try again...")

# Next week, to add to this program and make it better:
# 1) We'll introduce Python's 'random' library and the function 'randint'.
# 2) We'll set the program up to ask a designated number of questions.
# 3) We'll improve on the print formatting.
# 4) We'll summarize our test results.

# Ready? Go to 'week3.py'!!
