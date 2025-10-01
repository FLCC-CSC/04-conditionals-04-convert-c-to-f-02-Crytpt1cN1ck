# FILE NAME - convert_C_to_F_02.py

# NAME: Nicholas Sheppard
# DATE: 09/30/2025
# BRIEF DESCRIPTION: This program asks the user if they want to convert from Celsius to Fahrenhirit or from Fahrenheit to
#Celsius, then converts properly based on their choice.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
  C_to_F_converter()

def C_to_F_converter():
  print("===== Temperature Converter =====")
  print()
  print("  1. Convert from Celsius to Fahrenheit")
  print("  2. Convert from Fahrenheit to Celsius")
  print()
  choice = int(input("Please choose from the above menu: "))
  if choice == 1:
    celsius = float(input("Enter a temperature to convert: "))
    converted = celsius *9/5 + 32
    print()
    print(f"{celsius} degrees Celsius is {converted} degrees Fahrenheit.")
  elif choice == 2:
    fah = float(input("Enter a temperature to convert: "))
    converted = (fah - 32) * 5/9
    print()
    print(f"{fah} degrees Fahrenheit is {converted} degrees Celsius.")


main()








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

I wasn't able to use a conditional if statement without converting the user's choice to an integer. Using 'if variable == 1' and 'elif variable == 2'
would kick me out of the code block no matter what I chose. Once I converted the variable to an integer everything worked.





'''
