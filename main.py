print "Pydies"
print "CREDITS: PARMIN PATEL & SHIV PATEL"
print "------------------------------------"

#This function just prints the options that the user can choose from
def unit_options():
  print "------------------------------------"
  print " UNIT SELECTION: "
  print "1) Basic Python and Console Interaction"
  print "2) Conditionals"
  print "3) Looping"
  print "4) Functions"
  print "5) Strings"
  print "6) Creating and Altering Data Structures"
  print "7) Final Quiz (all units)"
  print "8) End the Program\n"
  print "Choose the number to learn that unit"  

#This is our first unit
def basic_python_and_console_interaction():

  #This just shoes the user the subunits that they can choose from
  print "\nBASIC PYTHON AND CONSOLE INTERACTION (UNIT 1)"
  print "1. Printing In Python(1.1)"
  print "2. Variables and Types(1.2)"
  print "3. User input(1.3)"
  print "4. Mathematical Operators(1.4) "
  print "5. String Operators(1.5)"
  print "6. Comments(1.6)"
  print "7. UNIT SELECTION"
  print "------------------------------------"

  while True:
    
    user_interaction= int(raw_input(" Please choose and option: "))
    #After getting input from the user, based on the number, it will display a block of code that is an explanation and example of the subunit
    #This one is for Printing in Python
    if user_interaction==1:
      print"PRINTING IN PYTHON\n"
      print "We can print elements to the screen by using the print command. If we want to print text, we need to surround the text with quotation marks " "."
      print" For Example, print ''hello world'' "
      print "------------------------------------"
    #This one if for Variables and Exceptions
    elif user_interaction==2:
      print "VARIABLES AND EXCEPTIONS\n"
      print "We use variables to store values that can be used to control commands in our code. We can also alter these values throughout the code. "
      print " To create a variable the  variable name goes on the left, a value on the right, and an equals sign in the middle. A variable has 3 things: Name, Type, and Value. \n"
      print "For example  var= ''Hello World''\n In the example  The variable name is var an equal sign in the middle and a string value which is Hello World. Your value can be anything it doesn't have to be a string.  "
      print "------------------------------------"
    #This one is for User Input
    elif user_interaction==3:
      print "USER INPUT\n"
      print "User input is useful when we want to get information from the user and store it to user it later. To store the data we use a variable and to retrive the data we use raw_input command. To write the user input code the variable goes on the left and then the user input type  then  open bracekts then raw_input again open brackets then we ask the information from the user as a string to end it we close it with 2 closed brackets."
      print "\nFor Example: name = str(raw_input(''what is your name: ''))"
      print "\nHere the variable name is name the type of the user input is string then raw_input command and then it asks the user for the information it needs. "
      print "------------------------------------"
    #This one if for Mathematical Operators 
    elif user_interaction==4:
      print"MATHEMATICAL OPERATORS\n"
      print "Mathematical operators are used to do caculations within a code. There are 7 Mathematical operators: addition, subtraction, multiplication, integer division, exponentiation, modulus(remainder), and negation. "
      print "\nThere are python signs for each operator listed below with example in brackets.\n \naddition: + (4+5) \nsubtraction: - (7-3) \nmultiplication: * (4*5) \ninterger division: / (7/2) \nexponentiation:** (3**2) \nmodulus: % (17 % 3) \nnegation:- (-3)\n "
      print "------------------------------------"
    #This one if for String Operators
    elif user_interaction==5:
      print "STRING OPERATORS\n"
      print " String operators are a little different you can only user the addition and multiplication operator with strings. Addition is used to combine 2 strings together and multiplication is used to repeat the same string multiple times. \n Example: "
      print " String + String: ''A '' + ''B''= ''AB'' "
      print " String * Integer: ''A'' * 3= ''AAA'' "
      print "Integer * string: 2 * ''A'' = ''AA'' "
      print "------------------------------------"
    #This one is for Comments
    elif user_interaction==6:
        print "COMMENTS\n"
        print "Comments are text in a program that is ignored by the python interpreter. There  are 2 types of comments: Multi-line comment, and the single line comment. "
        print "\nMulti-Line Comment is surrounded by 3 quotation marks and can span multiple lines. This type of comment is usaully used in the beginning of the program to describe the purpose of the program. "
        print " \nMulti-line Comment Example: ''' describe the program purpose here''' "
        print " \nSingle line program begins with a pound sign (#). This type of comment is used to describe specific parts of the code"
        print "\nSingle-line Comment Example: '' #Describe your code here'' "
        print "------------------------------------"
    #This one takes the user back to the area where you can choose other units and will be able to choose any other unit
    elif user_interaction==7:
        print "____________________________________"
        unit_selection()
    #This will just print "Try again" if something is wrong
    else:
      print" TRY AGAIN"

#This is another function for another unit (Unit 2)
def conditional():
  #This just shows the subunits that are in this unit and what they can choose
  print "\n CONDITIONAL (UNIT 2)"
  print "1. Booleans(2.1) "
  print "2. if statements(2.2)" 
  print "3. Comparision operators(2.3)"
  print "4. Logical Operators(2.4)"
  print "5. UNITS SELECTION"
  print "------------------------------------"

  while True:
    user_conditional= int(raw_input("please select an option: "))
    #After getting input from the user, based on the number, it will display a block of code that is an explanation and example of the subunit
    #This is Booleans
    if user_conditional==1:
      print "BOOLEANS\n"
      print "A boolean is a value that can either be true or false. You can think of it as an answer to a yes or no question. You can give variables a value that evaluates to true or false. "
      print "\nExample:\nbrought_food= True\nbrought_drink= False"
      print "------------------------------------"
    #This is for If Statements
    elif user_conditional==2:
      print "IF STATEMENTS\n "
      print "A programming construct that allows a program to behave differently, depending on circumstances. You can write programs that do different. To write a if statement you write the if command then a condition followed with a colon then a write below it indented once and what you want the compilier to do if the statement is true. \nExample: \n"
      print " if True:"
      print "   print 'its correct' "
      print "------------------------------------"
    #This is for Comparison operators
    elif user_conditional==3:
      print "COMPARISION OPERATORS\n"
      print "Comparision operators compare values and return true of false. There are 6 comparision operators. You can directly use comparision expression in if statements. You can store comparision expression in variables and you can use the variable in if statements. You can compare integers, strings and floating points."
      print "\nComparision Operators with Example and Return Value:"
      print " \n1. Equal to- == (6==7) Return: False "
      print "2. Not Equal to- != (6!=7) Return: True"
      print "3. Greater than- > (6>7) Return: False "
      print "4. Less than- < (6<7) Return: True"
      print "5. greater than or equal to- >=(6>=7) Return False"
      print "6. Less than or equal to- <= (6<=7) Return True"
      print "------------------------------------"
    #This is for Logical Operators
    elif user_conditional==4:
      print "LOGICAL OPERATORS\n"
      print "There are 3 logical operators. AND operator, OR operator, NOT operator. AND operator is when both the operands are true then condition becomes true. OR operator is when at least one of the two operands are True then condition becomes true. NOT operator is used to reverse the logical state of its operand. \nExample:\n"
      print "AND Operator: 6>7 and 6<7 Return: False "
      print "OR Operator: 6>7 or 6>3 Return: True"
      print "NOT Operator: not (6>7) Return: True"
      print "------------------------------------"     
    #This will once again take you to the unit selection screen
    elif user_conditional==5:
       print "____________________________________"
       unit_selection() 
    else:
      print "PLEASE TRY AGAIN"

#This is another function for another unit (Unit 3)
def looping():
  #All the subunits in this unit
  print " \nLOOPING(UNIT 3)"
  print "1. While loops(3.1)"
  print "2. For loops(3.2)"
  print "3. Break and continue(3.3)"
  print "4. Nested control structure(3.4)"
  print "5. UNIT SELECTION"
  print "------------------------------------"

  while  True:
    user_looping= int(raw_input("PLease select and option: "))
    #After getting input from the user, based on the number, it will display a block of code that is an explanation and example of the subunit
    #This is for While Loops
    if user_looping==1:
      print "WHILE LOOPS\n"
      print "While loops is a programming construct that allows you to repeatedly check an condition and execute a code. While loops are mostly used when you are unsure on how many times you want a code to repeat. To write a while loop you have to have the while commmad followed by a condition(must evaluate to True) and a colon, the body of the while loop must be indented by 1 level. Once the while loop condition becomes false the continues on to the rest of the program. The while loops runs if it is true and stops when it becomes false if the condition doesn't become false it is an infinite loop these are bad AVOID INFINITE LOOPS. \nExample:\n"
      print "while condition: "
      print "   do something"
      print "------------------------------------"
    #This is for For Loops
    elif user_looping==2:
      print "FOR LOOPS\n"
      print " A for loops is a programming construct that allows you to excute code a predetermined number of times. For loops are similar to while loops the only difference is that in a for loops we know how many times to repeat a code but in while loop we don't know.\nExample:\n"
      print "for i in range(4): "
      print "   ...do something..."
      print "------------------------------------"
    #This is for Break and Continues
    elif user_looping==3:
      print "BREAK AND CONTINUE\n"
      print " Break is a statement that immediately terminates the whole loop. Continue is a statement that skips only the top of the loop.\nExample for Continue:\n "
      print "for i in range(10):"
      print  " if i == 5:"
      print   "  continue"
      print    "print i"
      print " \nExample for Break:\n "
      print "for i in range(10):"
      print "   if i == 5:"
      print  "     print i"
      print  "     break"
      print "------------------------------------"
    #This is for Nested Control Structures
    elif user_looping==4:
      print "NESTED CONTROL STRUCTURE\n"
      print "Nested control strucute is when there is a loop within a loop.\nExample:\n" 
      print "for i in range(2):"
      print "   for j in range(2):"
      print "       print i + j"
      print "------------------------------------"
    #This takes the user back to the area where they can select units
    elif user_looping==5:
      print "____________________________________"
      unit_selection()

#This is another function for another unit (Unit 4)      
def functions_and_exceptions():
  #All the subunits in this unit
  print " \n FUNCTIONS AND EXPCEPTIONS (UNIT 4)"
  print "1. Functions(4.1)"
  print "2. Namespaces in Functions(4.2)"
  print "3. Functions and Perameter(4.3)"
  print "4. Functions and Return Values(4.4) "
  print "5. Exceptions(4.5)"
  print "6. UNIT SELECTION"
  print "------------------------------------"

  while True:
    user_interaction = int(raw_input("Please choose and option: "))
    #After getting input from the user, based on the number, it will display a block of code that is an explanation and example of the subunit
    #This is for Functions
    if user_interaction==1:
      print "\nFUNCTIONS"
      print "Functions are organized blocks of code that can be run multiple times."
      print "Functions are useful when you have a block of code that you want to run multiple times.\n"
      print "To create a function, you must use the 'def' functions with the name of the function after  it.\nFor example:\ndef function_name():\n     print 'Hello World'\n"
      print "------------------------------------"
    #This is for Namespaces in Functions
    elif user_interaction==2:
      print "NAMESPACES IN FUNCTIONS\n"
      print "Collecion of variable names that exist at a certain point in your code . Names don't exist  throughout the entire program, they only exist in a certain namespace."
      print "This is something you must pay attention to when making and using functions.\n"
      print "*  Any variable that is called outside of the function, is from the global namespace and can be used anywhere.\nExample:\nx =3\ndef add_num\n  print x\nThis code above will print 3 because x is not called in the function so it finds it in the global namespace.\n"
      print "------------------------------------"
    #This is for Functions and Peramets
    elif user_interaction==3:
      print "FUNCTIONS AND PERAMETERS\n"
      print "Pieces of information that you give to functions when you call them."
      print "Perameters can be told to the function in the beginning, when it is called, and that value will be used throughout that function.\nExample:\ndef functions_name(x):\n   print x\n\nIn the example above, if I were to call the function and write 4 in the place of x, the functions would print 4 because the value of x is 4\n"
      print "------------------------------------"
    #This is for Functions and Return Values
    elif user_interaction==4:
      print "FUNCTONS AND RETURN VALUES\n"
      print "Functions can either print or return values. When returning a value, the function basically wont run anything after the return statement."
      print "If there is no return statement in the fucntion, it will print 'None'.\n\nExample:\ndef function():\n  x = 4\nprint function(). This will print 'None' because there is no return value given"
      print "In order to call the function if you have a return statement, you must print the function. So for example, you must do: print functions() and that will print the return value inside the function."
      print "Inside of a funcion, you return anything, a string, a variable, anything."
      print "------------------------------------"
    #This is for Exceptions
    elif user_interaction==5:
      print "EXCEPTIONS\n"
      print "Python has many built-in exceptions which forces your program to output an error when something in it goes wrong"
      print "Runtime errors in a program. By default, they stop the program"
      print "------------------------------------"
    #This will take the user back to where they can select the unit again
    elif user_interaction==6:
        print "____________________________________"
        unit_selection()
    else:
      print" TRY AGAIN"

#This is another function for another unit (Unit 5)
def strings():
  #All the subunits in in this unit
  print " \n STRINGS (UNIT 5)"
  print "1. Indexing (5.1)"
  print "2. Slicing (5.2)"
  print "3. Immutability (5.3)"
  print "4. Strings and For Loops (5.4) "
  print "5. The IN Keyword (5.5)"
  print "6. String methods"
  print "7. UNIT SELECTION"
  print "------------------------------------"

  while True:
    user_interaction = int(raw_input("Please choose and option: "))
    #After getting input from the user, based on the number, it will display a block of code that is an explanation and example of the subunit
    #This is for Indexes
    if user_interaction==1:
      print "INDEXES\n"
      print "Indexes are used when strings are cut down and each character in the string."
      print "They are set up as:\nh e l l o\n0 1 2 3 4 \nor\n h e l l o\n-5-4-3-2-1\n"
      print "You can print certain things in said string by putting the string in a variable (in this case lets call it x) an type:\nprint x[2]\nand if x was 'Hello', it would print the second index which is 'l'"
      print "Typing x[:3] would print everything from the beginning to the third index, meaning in this case it would print 'Hel'"
      print "Typing x[2:] would print everything from the second index to the end of the string."
      print "Make sure you use square brackets"
      print "------------------------------------"
    #This is for Slicing
    elif user_interaction==2:
       print "SLICING\n"
       print "You can use indexes to slice strings into pieces and only print certain characters"
       print "example: \nx = hello and y = friend"
       print "print x[2] + y[4]\n this would print 'ln'"
       print "Another example: \nx[0] + y[2] + '' + y\n this will print hi friend"
       print "------------------------------------"
    #This is for Immutability
    elif user_interaction==3:
       print "IMMUTABILITY\n"
       print "Strings cannot be mutated or changed"
       print "You cannot try to change anything in the string without replacing it completely\n"
       print "For example:\ngreeting = 'hello there'\n farewell = 'goodbye'\n\nfarewell[0] = 'H'\n"
       print "This would be an error because you are trying to change the original string."
       print "However, you are able to make a new string with the same name with a changed string\n"
       print "Example:\nfarewell = farewell + '!'"
       print "After doing this, farewell would become 'goodbye!'"
       print "------------------------------------"
    #This is for Strings and Loops
    elif user_interaction==4:
      print "STRINGS AND LOOPS\n"
      print "Something to know when doing this is that you can print the length of a string by using the 'len' function.\nexample: print len(var_name)\n"
      print "You can use this in for loops to print every character in a string seperately.\nExample:\nstring = 'hello'\nfor i in range(len(string)):\n   print string[i]"
      print "Output:\nh\ne\nl\nl\no"
      print "However you can also do:\nfor i in letter:\n   print letter\nthis would print the same thing"
      print "------------------------------------"
    #This is for the In keyword
    elif user_interaction==5:
      print "THE IN KEYWORD\n"
      print "We've seen that the keyowrd 'in' has been used in the for loops that we use."
      print "you can also use the in keyword to check if there is a certain character in a string\nx = 'hello'\nif 'e' in x:\n  print x"
      print "this code basically says if the letter e is in x (which is 'hello'), it will print x"
      print "It returns either True or False and the if statement will take that and print [anything]"
      print "------------------------------------"
    #This is for String Methods 
    elif user_interaction==6:
        print "STRING METHODS\n"
        print "This will change up the string, but as we learned before, strings are immutable, meaning you have to put it into new variable."
        print "there are many different methods:\nstring.upper - this will make everything in the string uppercase.\nstring.lower - this will make everything in the string lowercase.\nstring.swapcase - this will alternate between uppercase and lowercase letters.\n There are many more than this but these ae just a few examples."
        print "\nIn order to actually use these methods, you must do:\nstring = 'Hello'\nnewstring = string.upper()\nstring.lower\nstring.swapcase"
        print "------------------------------------"
    #This will take the user back to where they can select the units again
    elif user_interaction==7:
        print "____________________________________"
        unit_selection()
    else:
      print "TRY AGAIN"

#This is another function for another unit (Unit 6)
def creating_and_altering_data_structures():
  print " \n Creating and Alternating Data Structures (UNIT 6)"
  print "1. Tuples (6.1)"
  print "2. Lists (6.2)"
  print "3. For Loops and Lists (6.3)"
  print "4. List Methods (6.4) "
  print "5. UNIT SELECTION"
  print "------------------------------------"

  while True:
    user_interaction = int(raw_input("Please choose and option: "))
    #After getting input from the user, based on the number, it will display a block of code that is an explanation and example of the subunit
    #This is for Tuples
    if user_interaction==1:
      print "TUPLES\n"
      print "A heterogenous, immutable data type that stores an ordered sequence of things"
      print "Hererogenous means that it can hold any type of data, in the form of strings, integers and much more."
      print "Immutable meaning that it cannot be changed, like strings, it must be made into a new tuple in order to add things."
      print "An example of a tuple is \nx = (1, 'Hello', 6, 8, 9)"
      print "Like strings, every element in the tuple also has an index meaning that you can print a single element in the tuple. You can also use the len() function to get the length of the tuple"
      print "You can concatinate tuples, but only with other tuples, if you try to do it with anything else, you will get an error."
      print "Making an empty tuple is quite easy: \nx = ()\nbut make sure that you use the regular brackets, not the square ones, you will learn why in the next few subunits"
      print "If you would like to concatinate two tuples, all you must do is:\ntuple1 = (2,3)\ntuple2 = (4,5)\ntuple1 + tuple2."
      print "This would print (2,3,4,5)"
      print "------------------------------------"
    #This is for Lists
    elif user_interaction==2:
      print "LISTS\n"
      print "Lists are similar to tuples because they are heterogenous and can hold any type of data.\nHOWEVER, lists can be changed unlike tuples"
      print "Lists use square brackets '[]'."
      print "Lists also have index values, meaning you can also print a single element in the list."
      print "An example of lists is:\n x = ['Hello',2,3.14,5,'This is a list']"
      print "You can add things to the list by using the .append method:\n x.append(14)\n that will add the number 14 to the list"
      print "------------------------------------"
    #This is for For Loops and Lists
    elif user_interaction==3:
      print "FOR LOOPS AND LISTS\n"
      print "Just like strings and for loops, you can do the same thing with lists. You are able to print each element in the list one-by-one by doing:\nx = [2,4,5,6]\n for item in x:\n  print item"
      print "Output:\n2\n4\n5\n6"
      print "------------------------------------"
    #This is for List Methods
    elif user_interaction==4:
      print "LIST METHODS\n"
      print "Just like strings, lists have many methods that you can use to change it."
      print "One of the examples that was showed before is:\nlist.append() - this just adds things to the list.\n"
      print "A couple other examples of list methods include:\n.remove() - removes a certain element in the list\n.count(x) - returns  the number of times x apears in the list\n.reverse - Reverses the elements of the list in place\n"
      print "len(list_name) isn't actually a method, but it does work on lists."
      print "An example of one of the methods actually being used on a list:\nx = [4,5,6,7]\n x.reverse\nprint x\nOutput:\n[7,6,5,4]"
      print "------------------------------------"
    #This will take the user back to where they can select another unit
    elif user_interaction==5:
        print "____________________________________"
        unit_selection()
    else:
      print "TRY AGAIN"

#This is the Final Quiz, which incudes questions from every single unit
def final_quiz():
    #This is a variable called score, and it will increase whenever the user gets a question correct
    score = 0
    #This is a list. It holds the questions and the options to that question. It will display on the screen depending on the index (Look to the for loop below)
    questions = ["1. Which Python code segment will display 'hello, world!' on the screen?\nOptions:\n1) display 'hello, world!'\n2) print 'hello,world!'\n3) print hello world!\n4) 'hello world'\n",
    "2. What does the following Python code display?\n print 'hello'\n print 'world'\nOptions\n1) hello\n   world\n2) helloworld\n3) hello world\n4) hello\n\n   world\n",
    "3. What type of variable is this: x = 'Hello There'\nOptions:\n1) float\n2) integer\n3) string\n4) boolean\n",
    "4. What is the type of the variable x in the following Python program?:\nx = input('Enter something: ')\nOptions:\n1) string\n2) integer\n3) float\n4) boolean\n",
    "5. Which of the following will print a value of 5?:\nOptions:\n1) 11/2\n2) 11.0/2\n3) float(11)/2\n4) 2 + 3 * 3",
    "6. Which of the following is NOT a valid type of comment in Python?\nOptions\n1) %% This is a comment\n2) #This is a comment\n3) '''\n   This is a comment\n   '''",
    "7. How may possible values are there for boolean variables?\nOptions\n1) 1\n2) 3\n3) 2\n4) There are an infinite amount of values\n",
    "8. Which of the following progams will print nothing?\nOptions:\n1) x = True\n   if x:\n    print 'hi'\n2) if false:\n      print 'hi'\n3) x = False\n   if x:\n     print 'hi'\n   else:\n     print 'hello'\n",
    "9. Which of the following is NOT a comparison operator?\nOptions:\n2) <=\n3) !=\n3) >\n4) ?\n",
    "10. Which of the following is NOT a logical operator in Python?\nOptions:\n1) and\n2) or\n3) not\n4) because\n",
    "11. Which of the following evaluates to the variable x rounded to two decimal places?\nOptions:\n1) round (x,2)\n2) round (2,x)\n3) round (2), 2\n4) round (2), x\n",
    "12. How many lines will this program print?\nwhile True\n  print 'hi'\nOptions\n1) 0\n2) an infinite amount of lines\n3) 1\n",
    "13. Which of the following best describes the purpose of a for loop?\nOptions\n1) A for loop is for doing something an indeterminate number of times.\n2) A for loop is doing something an infinite number of times.\n3) A for loop is for doing something a fixed number of times.\n4) A for loop is for doing something three times.\n",
    "14. Which of the following Python keywords skips back to the beginning of a loop?\nOptions:\n1) break\n2) continue\n",
    "15. What does the following program print?\nfor i in range(2):\n   for j in range(2):\n      print i + j\Options:\n1) 0\n   1\n   1\n   2\n2) 0112",
    "16. What is the correct way to define a function?\nOptions:\n 1)def function_name():\n 2)function_name():\n 3)function_name\n 4)call function_name",
    "17. What type of variable is x in this code\nx = 10\ndef add_nums():\n   y = 2\n   z = x  y\n   print z\nOptions:\n 1)Functions namespace\n 2)Global namespace\n 3)Object namespace\n 4)Class namespace",
    "18. Which of the following code samples properly passes the number 10 as an argument to the function print_number?\nOptions:\n (1)print_number(10)\n 2)print_number()\n   print 10\n 3)10(print_number)\n 4)print print_number\n   print 10\n",
    "19. Which of the following functions successfully returns the number 10?\nOptions:\n1) def my_function():\n      10\n2) def_myfunction(10):\n      return\n3) def my_function():\n      return 10\n4) def my_function():\n      print 10\n",
    "20. Which of the following keywords are relevant to exceptions in Python?\nI. def\nII. except\nIII. try\n\nOptions:\n1) II and III\n2) II only\n3) I and II\n4) none of the above\n",
    "21. Which operator allows you to create a string that is the result of putting two different strings together, side by side?\nOptions:\n1) +\n2) - \n3) *\n4) /\n",
    "22. Which word applies to strings in Python?\nOptions\n1) mutable\n2) immutable\n",
    "23. What does len('hello') evaluate to?\nOptions:\n1) 'hello\n2) 4\n3) '__'\n4) 5\n",
    "24. What does the following program print?:\nprint 'a' in 'banana'\nOptions:\n1) True\n2) False\n3) 1\n4) 'aaa'\n",
    "25. Which of the following is not a string unit?:\nOptions:n1) .upper\n2) .lower\n3) .isupper\n4) .together\n",
    "26. Which of the following is the correct way to declare a tuple?\nOptions:\n1) x = (1, 2, 3)\n2) x = [1, 2, 3]\n",
    "27. Which of the following Python programs creates a list with the numbers 1 through 5?\nOptions:\n1) my_list = (1, 2, 3, 4, 5)\n\m2) my_list = [1, 2, 3, 4, 5]\n3) my_list = 1, 2, 3, 4, 5\n4) my_list = '1, 2, 3, 4, 5\n'",
    "28. Which of the following is not a list method?\nOptions:n1) .reverse\n2) .remove\n3) .append\n 4) .highest"]

    #This is another list, called Answers. This list holds the answers for all of questions in the list above. The indexes for each answer match up with the indexes of the questions
    answers = ["2", "1", "3", "1", "1", "1", "3", "2", "4", "4", "1", "2", "3", "2", "1", "1", "2", "1", "3", "1", "1", "2", "4", "1", "4", "1", "2", "4"]

    #This for loop runs through the list with the questions. Using the variable "i", it can go through ever index in that list and print it
    for i in range (len(questions)):
        print "-------------------------------------------------------------------"
        print questions[i]
        user_answer = raw_input("What is the answer to this question?: ")\
        #After printing the question, and asking the user for their input as an answer to that queston, this if/else statement will run, and if what they entered is correct, it will go to the next question. This will also add 1 to score
        if user_answer == answers[i]:
            print "Thats correct\n"
            score = score + 1
        
        #However, if they enter anything other than the right answer, they will be asked to enter another number, until it is correct. This will add nothing to the variable "score"
        else:
            while user_answer != answers[i]:
                user_answer = raw_input("that was wrong try again: ")
            print "Correct\n"
    
    #This statement just prints your score, and shows how many you got correct out of the amount of questions 
    print "You scored " + str(score) + "/" + str(len(questions))
    print "____________________________________"
    unit_selection()

#With all of these functions, this is the code
#This function uses all the functions that have been called above and calls them when necessary
def unit_selection():
  while True:
    #This units that you can choose from
    unit_options()
    user_unit = raw_input("What would you like to learn?: ")
    #Makes sure that the number that is entered is valid, and if not, asking the user to another number again
    while int(user_unit) <1 or int(user_unit) >8:
      user_unit = raw_input("Please enter a valid number: ")
    
    #If the user enters the number 1, it will call the function for the first unit (basic_python_and_console_interaction) which will print all the options and the information along with some examples
    if user_unit == "1":
      basic_python_and_console_interaction()
    #If the user enters the number 2, it will call the function for the second unit (conditional) which will print the options and the information along with some examples
    elif user_unit == "2":
      conditional()
    #If the user enters the number 3, it will call the function for the third unit (looping) which will print the options and the information along with some examples
    elif user_unit == "3":
      looping()
    #If the user enters the number 4, it will call the function for the fourth unit (functions_and_exceptions) which will print the options and the information along with some examples
    elif user_unit == "4":
      functions_and_exceptions()
    #If the user enters the number 5, it will call the function for the fifth unit (strings) which will print the options and the infromation along with some examples
    elif user_unit == "5":
      strings()
    #If the user enters the number 5, it will call the function for the sixth unit (creating_and_altering_data_structures) which will print the options and the information along with some examples
    elif user_unit == "6":
      creating_and_altering_data_structures()
    #If the user enters the number 7, it will call the function that has the quiz (final_quiz)
    elif user_unit == "7":
      print "Final Quiz (All Units)"
      final_quiz()
    #Finally, this will end the program if the user enters the number 8
    elif user_unit == "8":
      print "THIS PROGRAM HAS ENDED"
      print "____________________________________"
      exit()

#This calls the final function to actually run the code
unit_selection()