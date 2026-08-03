#Here what we do is counting from 1 to 20 what number is exact or no
# the number is the name we put to the variable, and the range is how long we want it to be.
#remember this python take 1 so if you put (1, 5) it'll be 1,2,3,4 you need to add one more.

for number in range(1, 21):
    #here the you can say if or else that's mean like yes or no
    #so here the if number % 2 == 0: print means that the number we put in the range divide in 2 is equal to 0 it's a exact number
    if number % 2 == 0:
        print(str(number) + " is exact")
    #here the else means no, so if the number divide in 2 doesn't give 0 means it's not exact, so it'll print "is not exact"
    else:
        print(str(number) + " is not exact")