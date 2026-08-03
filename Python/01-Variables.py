#Easy, here you can see differents things, like the variables, that is the name we put for understand their value, we use first the name after it "="
#And the the value we put to the variable
#There're differents type of variables here below this you can see them.

Word = "Crazy"          # string
Number = 10                # int 
Numbre_no_exacted = 1.70   # float 
Condition = True      # bool 



Name = "Akali" #Name inside the ""
Age = 0 #Age
Height = 0.0 #Height
#Here we print it, print is like what's is going to see the user in the display.
#the f-string before the "" is for format the print means that you can mix words with the variables, but take care
# becase you need to use {} for tell the language the difference between.
print (f"My name {Name}, I'm {Age} years old and my height is {Height}")
# without the f-string you can still use the variables but you need to put doble , and ""
#It take more time so it's better using the f-string
print ("My name", Name, "I'm" , Age, "years old and my height is" ,Height,)
# The 3 way is using connectors "+"
print("My name " + str(Name) + ", I'm " + str(Age) + " years old and my height is" + str(Height))



