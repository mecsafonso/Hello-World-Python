print ('Hello World!')

# Math Operators from Highest to Lowest Precedence
# Operator          Operation               Example         Evaluates to..
#   **              Exponent                2 ** 3              8
#   %               Modulus/remainder       22 % 8              6
#   //              Integer division /
#                   floored quotient        22 // 8             2
#   /               Division                22 / 8              2.75
#   *               Multiplication          3 * 5               15
#   -               Subtraction             5 - 2               3
#   +               Addition                2 + 2               4


# Data Types

#   Integers                -2, -1, 0, 1, 3,
#   Floating-point numbers  -1.25, -1.0, --0.5, 0.0, 0.5, 1.0
#   Strings                  'a', 'aa', 'aaa', 'Hola'

# When + operator is used on two string values, it joins the strings as the string concatenation operator.
print('Mecs' + 'Afonso')

# When * operator is used on one string value and one integre value, it becomes the string replication operator.
print('Mecs' * 5) 

print ('Goodbye cruel world!')


# Assignment Statemets
# The equal sign is called the assignment operator
spam = 40
eggs = 3
spam = spam + eggs
print (spam)
# A variable is initialized (or created) the first time a value is stored in it.
# After that, you can use it in expressions with other variables and values.
# When a variable is assigned a new value, the old value is forgotten


# The str(), int(), and float() Functions
# We use this functions to pass them values of the other data types to obtain a string, a integer, our floating-point from of those values.

str(-3.14) #'-3.14' 
int('42') #42
float(10) #10.0


# Boolean Values
# The Boolean data type has only two values: True and False

# Comparison Operators
#   Compare two values and evaluate down to a single Boolean value.
#   Operator        Meaning
#      ==           Equal to
#      !=           Not equal to
#      <            Less than
#      >            Greater than
#      <=           Less than or equal to
#      >=           Greater than or equal to

42 == 42 #True
42 == 99 #False
2 != 3 #True
2 != 2 #False      

#Not than an integer of floating-point value will always be unequal to a string value.
#The expression 42 == '42' evaluates to False because Python consider the integer 42 to be different from the string '42'.

#The <, >, <=, and >= operators, on the other hand, work properly only with integer and floating-point values.


# Boolean Operators
# And, Or and Not
# And: Only true if both are True
# Or: Only false if both are False
# Not: The not operator simply evaluates to the opposite Boolean value. 

