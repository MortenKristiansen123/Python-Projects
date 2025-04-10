# Dictionaries, python dictionaries have {} brackets


# A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
# If we take the example of band as can be seen below, vocals and guitar are the keys and Plant and Page are the values.
band = {
    'vocals': 'Plant',
    'guitar': "Page",
}

band2 = dict(vocals='Plant', guitar='Page')

print(band)
print(band2)
print(type(band))
# length of the dictionary, returns the number of key-value pairs in this case 2
print(len(band))


# Accessing items in a dictionary

print(band['vocals'])  # returns 'Plant'
print(band.get('guitar'))  # returns 'guitar'


# list all keys

# returns a list of all keys in the dictionary # dict_keys(['vocals', 'guitar'])
print(band.keys())


# list all values

# returns a list of all values in the dictionary # dict_values(['Plant', 'Page'])
print(band.values())

# a list of key/value pairs as tuples
# returns a list of all key-value pairs in the dictionary # dict_items([('vocals', 'Plant'), ('guitar', 'Page')])
print(band.items())


# verifying if a key exists in the dictionary

print('vocals' in band)  # returns True
print('bass' in band)  # returns False


# Changing values in a dictionary

# changing the value of the key 'vocals' to 'Robert Plant'
band['vocals'] = 'Robert Plant'
# When you use .update on a dicrionary it's kind of like saying:
# Hey dictionary, here’s some new info — add it if it’s not there, but if it is, overwrite it....
# However it is important to note that this is only true if the key already exists in the dictionary.
# If the key does not exist, it will add a new key-value pair to the dictionary.
band.update({'bass': 'JPJ'})
band.update({'bass': 'Test'})
# {'vocals': 'Robert Plant', 'guitar': 'Page', 'bass': 'Test', 'Test': 'Test'}
band.update({'Test': 'Test'})
print(band)


# Removing items from a dictionary

# {'vocals': 'Robert Plant', 'guitar': 'Page', 'Test': 'Test'}
print(band.pop('bass'))
# print(band.pop('JPJ')) # KeyError: 'JPJ' - this will raise an error because 'JPJ' is not a key in the dictionary
# .pop() only works with keys, not values.
print(band)


band["drums"] = "Bonham"
print(band)

# removes the last item(key-value pair) added to the dictionary, in this case 'drums': 'Bonham'
# also returns a tuple of the key-value pair that was removed
print(band.popitem())
print(band)


# Delete and clear methods

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()  # removes all items from the dictionary
print(band2)  # returns {} as the dictionary is now empty

del band2  # deletes the dictionary itself


# Copying dictionaries
#     # how not to copy a dictionary
# band2 = band  # creates a reference to the original dictionary, not a copy
# # so any changes made to band2 will also affect band
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)  # returns {'vocals': 'Robert Plant', 'guitar': 'Page'}
# returns {'vocals': 'Robert Plant', 'guitar': 'Page', 'drums': 'Dave'}
print(band2)
# as can be seen both were printed after adding the key-value pair to band2, but only band2 was affected.
# This is because band2 is a copy of band, not a reference to it.

# another good way to copy a dictionary is to use the dict() constructor
band3 = dict(band)
band3["trumpet"] = "Morten"
print("Good copy!")
print(band3)


# Nested Dictionaries
# A dictionary inside a dictionary is called a nested dictionary. (this means that the key-value can be another dictionary)

member1 = {
    'name': 'Plant',
    'instrument': 'vocals',
}
member2 = {
    'name': 'Page',
    'instrument': 'guitar',
}
band = {
    'member1': member1,
    'member2': member2,
}

print(band)
print(band['member1'])  # returns {'name': 'Plant', 'instrument': 'vocals'}
print(band['member1']['name'])  # returns 'Plant'


# Sets

nums = {1, 2, 3, 4, 5}

nums2 = set((1, 2, 3, 4))

print(nums)  # returns {1, 2, 3, 4, 5}
print(nums2)  # returns {1, 2, 3, 4, 5}
print(type(nums))  # returns <class 'set'>
print(len(nums))  # returns 5

# No duplicates allowed in a set, so if you try to add a duplicate it will be ignored
nums = {1, 2, 3, 4, 5, 5}
print(nums)  # returns {1, 2, 3, 4, 5}

# True is a dupe of 1, False is a dupe of 0 (true has the value 1 and false has the value 0)
nums = {1, True, 2, 3, 4, False, 5, 0}
# returns {False, 1, 2, 3, 4, 5} # since 1 is input before true, true is ignored and since false is input before 0, 0 is ignored
print(nums)


# Check if a value exists in a set

print(2 in nums)  # returns True
print(6 in nums)  # returns False
# You can't refer to any specific value based on position in a set, or a key in a dictionary.
# AKA Sets are unordered and unindexed, so you can't access items by index or key.


# Adding a new item to a set
nums.add(6)  # adds 6 to the set
print(nums)  # returns {1, 2, 3, 4, 5, 6}

# You can also add items from one set to another set
morenums = {7, 8, 9}
nums.update(morenums)  # adds all items from morenums to nums
print(nums)  # returns {1, 2, 3, 4, 5, 6, 7, 8, 9}
# You can use .update() with lists, tuples, and dictionaries as well. As seen above it where a set was used, but it used with these as well.


# Merge two sets to create a new set

one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)  # creates a new set with all items from both sets
print(mynewset)  # returns {1, 2, 3, 4, 5, 6}


# Keep only the duplicates in a set in a new merged set

three = {0, 1, 2}

one.intersection_update(three)  # keeps only the items that are in both sets
print(one)  # returns {1, 2}


# Keep everything except the duplicates in a set in a new merged set

four = {2, 3, 4}

# keeps only the items that are not in both sets
one.symmetric_difference_update(four)
print(one)  # returns {1, 3, 4}
