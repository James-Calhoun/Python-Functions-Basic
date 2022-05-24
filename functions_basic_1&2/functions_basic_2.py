# Countdown: Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countDown(x):
    # creates a for loop starting at any (x) incrementing by -1 all the way to 0
    newList = []
    for ind in range(x, -1, -1):
        newList.append(ind)
    return newList

# print(countDown(5))         (Code Test)

# Print and Return: Create a function that will receive a list with two numbers. Print the first value and return the second.

def printAndReturn(list):
    print(list[0])
    return list[1]

# print(printAndReturn([1, 2]))     (Code Test)

# First Plus Length: Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def firstPlusLength(list):
    sum = list[0] + len(list)
    return sum

# print(firstPlusLength([1, 4, 3, 5, 6, 7]))

# Values Greater than Second: Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
#   Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def valuesGreaterthanSecond(list):
    if(len(list) < 2):
        return False
    newList = []
    sum = 0
    for ind in range(0, len(list)):
        if (list[ind] > list[1]):
            newList.append(list[ind])
            sum += 1
    print(sum)
    return newList

# print(valuesGreaterthanSecond([1, 3, 2, 1, 4, 5, 6, 3, 2]))

# This Length, That Value: Write a function that accepts two integers as parameters: size and value. The function should create and return a 
#   list whose length is equal to the given size, and whose values are all the given value.

def this_length_that_value(size, value):
    output = []
    for index in range(0, size):
        output.append(value)
    print(output)

# this_length_that_value(3, 540)        (Code Test)

