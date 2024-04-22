# Creating a list
my_list = [1, 2, 3, 4, 5]

# Adding elements to the list
my_list.append(6)
print("List after adding element:", my_list)

# Removing an element from the list
my_list.remove(3)
print("List after removing element:", my_list)

# Modifying an element in the list
my_list[0] = 10
print("List after modifying element:", my_list)

# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Adding a key-value pair to the dictionary
my_dict['d'] = 4
print("Dictionary after adding key-value pair:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict['b']
print("Dictionary after removing key-value pair:", my_dict)

# Modifying a value in the dictionary
my_dict['a'] = 100
print("Dictionary after modifying value:", my_dict)

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)
print("Set after adding element:", my_set)

# Removing an element from the set
my_set.remove(3)
print("Set after removing element:", my_set)

# Modifying an element in the set (Sets are unordered and do not support indexing)
# We can remove an element and then add a new element
my_set.remove(2)
my_set.add(10)
print("Set after modifying element:", my_set)
