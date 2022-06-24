# 1. Write a function that has one parameter: a list 
#       a. The list that is passed in needs to be a list of numbers 
#       b. Compute the average of the numbers inside the list 
#       c. Any numbers in the list that are less than the computed average will be 
#          appended into a separate list. That list will then be returned from the function.

list_of_numbers = [1, 13, 56, 87, 53, 12, 123, 55, 67]
list = []

def average_number_of_list(numbers):
    average_number = sum(numbers) / len(numbers)
    i = 0
    for number in list_of_numbers:
        i = number
        if i < average_number:
            list.append(i)



# 2. Write a function that has two parameters: a list, a number 
#       a. Return the value in the list at the index represented by the number parameter 
#       b. If there is no value at the specified index, print to the console “No value here!”

trees_list = ["Oak", "Hamlock", "Linden", "Maple"]

def two_parameters(list, number):
    i = 0
    length_of_list = len(list)
    for tree in list:
       i += 1
       if i - 1 == number:
        return tree
    if number > length_of_list:
                print("No value here!")

# 3. Write a function that has one parameter: a list 
#   a. The list that is passed in needs to be a list of numbers 
#   b. Find the most frequent value in the list and return that value

average_number_of_list(list_of_numbers)
two_parameters(trees_list, 2)