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
    for element in list:
       i += 1
       if i - 1 == number:
        return element
    if number > length_of_list:
                print("No value here!")

# 3. Write a function that has one parameter: a list 
#   a. The list that is passed in needs to be a list of numbers 
#   b. Find the most frequent value in the list and return that value

most_freaquent_list = [3, 1, 2, 3, 3, 2, 3, 1, 3, 4, 3]

def most_freaquent_value(list):
    counter = 0
    number = list[0]
    for i in list:
        freaquency = list.count(i)
        if freaquency > counter:
            counter = freaquency
            number = i
    return number


#   4. Write a function that has two parameters: a list, a list 
#       a. Both lists that are passed in should contain the first names of people 
#       b. Iterate over the lists comparing the values at each index from one list to the 
#           other. If there is a matching name in both lists, return that name from the 
#           function 
#       c. For example: [“Nevin”, “David”, “Mike”] and [“Brett”, “Mike”, “Charles] 
#       i. “Mike” would be returned from the function because it is a match in both 
#           lists

list_with_names1 = ["Brian", "Patrick", "Laura", "Derek", "Nick", "Ryan"]
list_with_names2 = ["Robert", "Damian", "Ryan", "Max", "Greg", "Mitchell"]

def compare_two_lists(list1, list2):
    length_of_list = len(list_with_names1)
    is_name_matching = False
    while is_name_matching is False:
        i = 0                                                       # Not finished! Don't work!
        for name in list_with_names1:
            i += 1
            if name == list_with_names2[i]:
                return name
        continue

average_number_of_list(list_of_numbers)
print(two_parameters(trees_list, 2))
print(most_freaquent_value(most_freaquent_list))
print(compare_two_lists(list_with_names1, list_with_names2))