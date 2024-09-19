#####################################################################

# Program Name: Rubber Duck Calculator
# Author: Jayce Johnson
# Date: September 18th, 2024
# Description: Finds the amount of rubber ducks that will fit in a 
#              reservoir depending on the size of the reservoir.

#####################################################################

# Sets the size of the rubber duck at 75 square inches
SIZE_OF_DUCK_SQIN = 75

# Setting a constant defined as 144, so that converting from square feet to square inches is more readable
SQFT_TO_SQIN_CONVERSION = 144

# Getting the size of the reservoir from the user with a prompt.
# I am re-using some of my code from the last assignment. https://github.com/jaycebaxter/ice_cream_sold/blob/main/ice_cream_sold.py

while True:
      try:
            size_of_reservoir_sqft = float(input("What is the size of the reservoir? Please enter your answer in square feet. "))
            if size_of_reservoir_sqft < 0:
                  print ("Invalid input. Please enter a positive number.")
                  continue
      except:
            print("Invalid input. Please enter a number.")
      else:
            break

# Converting the size of the reservoir into square inches so it's easier to work with
size_of_reservoir_sqin = int(size_of_reservoir_sqft)*SQFT_TO_SQIN_CONVERSION

# Dividing the size of the reservoir by the size of the duck to see how many ducks will fit
amount_of_ducks = size_of_reservoir_sqin/SIZE_OF_DUCK_SQIN

# Printing the answer to the user
print("Assuming the size of the duck is roughly 75 square inches, a " + str(size_of_reservoir_sqft) + \
      " square foot reservoir can fit about " + str(amount_of_ducks) + " rubber ducks.")