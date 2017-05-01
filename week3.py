# This week we use the randint function from the random library.
# We are going to ask the user how many questions they want to answer.
# Also, we are introducing print formatting in python3.
# We use a boolean to control the increment of correct answers.
# Finally, we will summarize the results and print the percent correct!

# We tell Python that we are using its library called 'random'.
# Python libraries have pre-written functions that can be used, once you
# import that library.
import random

print("Welcome to Multiplication Facts!")
# Ask the user how many questions he/she wants to answer, then
# set that number to a variable called 'how_many'.
how_many = int(input("How many questions do you want to try? "))
# Initialize the counter for correct answers.
correct = 0
# Initialize a boolean variable (true/false) for 'first_try'.  This 
# is so we can count how many questions were answered correctly on 
# the first try, and then make the user keep quessing until the answer
# is correct.
first_try = True

# This function will use the random library's function 'randint'.
# 'randint' takes 2 numbers and will return a random number between
# and including those two passed-in numbers.
def getnum():
    return random.randint(0,15)

for i in range(how_many):
  # Now we call the function we defined above twice, to get our 2 
  # numbers to multiply.
  number1 = getnum()
  number2 = getnum()
  # Here is where we ask the user to enter the product of the 2 numbers.
  # The Python3 print formatting here is going to require some 
  # explanation during our club time...but you can copy here if you 
  # are going ahead...
  print("{}. Product of {} and {}?".format(i+1, number1, number2))

  # Now we go back to the logic we worked out last week..
  result = number1 * number2
  guess = None

  while guess != result:
    guess = int(input("What do you think the answer is? "))
    # Only increment 'correct' if correct on first_try!
    # When we simply say 'first_try' we are really saying
    # 'when first_try is true'...
    if guess == result and first_try:
      print("AMAZING! :)")
      # 'correct' is our counter for first_try correct answers.
      correct += 1
    else:
      # If the program gets here, it means the user did not get
      # the answer correct on the first try.  We therefor set 
      # first_try to false, and although the program keeps asking
      # for the correct answer, the correct counter will not be
      # incremented when the user gives the correct answer.
      first_try = False
    # Now, we keep asking until the user enters correctly
    if guess == result and not first_try:
        print("Finally, you got it!")
        # Reset the first_try boolean for next question
        first_try = True
    elif guess < result:
      print("Too low, try again...")
    elif guess > result:
      print("Too high, try again...")

# Summary of results
# Look at the print formatting here, we'll explain during club time...
print("You tried {} questions.".format(how_many))
print("You answered {} correct on the first try!".format(correct))
# This format says 'print the quotient of correct/how_many as a percentage,
# to the nearest tenth of a percent'
print("Your grade is {:.1%}.".format(correct / how_many))
