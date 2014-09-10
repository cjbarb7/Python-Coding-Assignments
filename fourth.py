##this program is to understand the use of parenthesis for order of operations to see how 
##parenthesis can change your results 

##assigning variables
firstVariable = 5

secondVariable = 8

thirdVariable = 10

fourthVariable = 2

combinationOne = firstVariable + secondVariable * thirdVariable - fourthVariable

combinationTwo = (firstVariable + secondVariable) * thirdVariable - fourthVariable

combinationThree = firstVariable + secondVariable * (thirdVariable - fourthVariable)

combinationFour = (firstVariable + secondVariable) * (thirdVariable - fourthVariable)

print "First combination is %d" % combinationOne

print "Second combination is %d" % combinationTwo

print "Third combination is %d" % combinationThree

print "Fourth combination is %d" % combinationFour

print "Using parenthesis with +, -, and * can change your results"
