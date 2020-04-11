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


# Mixing Boolean and Comparison Operators
# Recall that the and, or, and not operators are called Boolean operators because they always operate on the Boolean values True and False. 
# While expressions like 4 < 5 aren’t Boolean values, they are expressions that evaluate down to Boolean values. 

print( 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2) #True



# Flow Control Statements

#   if Statements
#           An if statement’s clause (that is, the block following the if statement) will execute if the statement’s condition is True. 
#           The clause is skipped if the condition is False.

name = 'Alice'

if name == 'Alice' :
    print('Hi, Alice.')


#   else Statements
#           An if clause can optionally be followed by an else statement. 
#           The else clause is executed only when the if statement’s condition is False. 

if name == 'John':
    print('Hi, John')
else:
    print('John? Where u are')


#   elif Statements
#           While only one of the if or else clauses will execute, you may have a case where you want one of many possible clauses to execute. 
#           The elif statement is an “else if” statement that always follows an if or another elif statement.
#           It provides another condition that is checked only if any of the previous conditions were False.

if name == 'Mecs':
    print('Hi, Mecs')
elif name == 'Alice':
    print('Oh, Its you Alice, I was waiting Mecs')


#   while Loop Statements
#           You can make a block of code execute over and over again with a while statement.
#           The code in a while clause will be executed as long as the while statement’s condition is True.   

spam = 0
while spam < 5:
    print('Hi :)')
    spam = spam + 1


#   break Statements
#           There is a shortcut to getting the program execution to break out of a while loop's clause early.
#           If the execution reaches a break statements, it immediately exits the while loop´s clause.
#           In code, a break statement simply contains the break keyword.
# (See yourName2.py)


#   continue Statements
#           Like break statements, continue statements are used inside loops. 
#           When theprogram execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition. 
#           (This is also what happens when the execution reaches the endof the loop.)



# There are some values in other data types that conditions will consider equivalent to True and False. When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True.


# for Loops and the range() Function

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')



# The Starting, Stopping, and Stepping Arguments to range()
#   Some functions can be called with multiple arguments separated by a comma, and range() is one of them

for i in range(12, 100):     #The first argument will be where the foor loop´s variable starts, and the second argument will be up to, but not includin, the numbre to stop at.
    print(i)            

for i in range (0, 10, 2):   #The first two arguments will be the start and stop valyes, and the thrd will be the step argument. The step is the amount that the variable is increase by after each iteration.
    print(i)

    