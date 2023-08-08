# Create an array with some elements
my_array = [1, 2, 3, 4, 5]

# Find the index of the second-to-last element
second_to_last_index = len(my_array)//3
# second_to_last_index=2
# second_to_last_index=len(my_array)-2


# Remove the second-to-last element using the del keyword
del my_array[second_to_last_index]

# Print the updated array
print(my_array)