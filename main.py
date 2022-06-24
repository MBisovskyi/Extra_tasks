# 1. Write a function that has one parameter: a list 
#       a. The list that is passed in needs to be a list of numbers 
#       b. Compute the average of the numbers inside the list 
#       c. Any numbers in the list that are less than the computed average will be 
#          appended into a separate list. That list will then be returned from the function.

list_of_numbers = [1, 13, 56, 87, 53, 12, 123, 55, 67]
list = []

def average_number_of_list(numbers):
    average_number = sum(numbers) / len(numbers)
    print(average_number)
    i = 0
    for number in list_of_numbers:
        i = number
        if i < average_number:
            list.append(i)
    print(list)


average_number_of_list(list_of_numbers)