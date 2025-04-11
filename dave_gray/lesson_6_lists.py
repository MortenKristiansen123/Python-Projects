# Remember that 0 is the first index in a list
# Remember that -1 is the last index in a list

users = ["Morten", "Dave", "John", "Jane"]

data = ["Morten", 52, 1.75, True]

emptylist = []

print("Dave" in users)  # True
print("Dave" in data)  # True
print("Dave" in emptylist)  # False


print(users[0])  # Morten
print(users[1])  # Dave
print(users[-1])  # Jane
print(data[0])  # Morten
print(data[1])  # 52
print(data[-1])  # 1.75

print(users.index("Dave"))  # 1
print(users.index("Jane"))  # 3

print(users[0:2])  # ['Morten', 'Dave']
print(users[1:3])  # ['Dave', 'John']
print(users[1:])  # ['Dave', 'John', 'Jane']
print(users[:3])  # ['Morten', 'Dave', 'John']

print(len(users))  # 4
print(len(data))  # 4
print(len(emptylist))  # 0

# The .append() method can only add one element at a time to the list, no matter what type of element it is.
users.append("Bob")  # adds "Bob" to the end of the list
print(users)
# ['Morten', 'Dave', 'John', 'Jane', 'Bob']

# Make sure if you're using the += that the element you're adding is in [""] or it will add 'J', 'a', 's', 'o', 'n' to the list
users += ["Jason"]  # creates a new list with "Jason" as the only element
print(users)
# ['Morten', 'Dave', 'John', 'Jane', 'Bob', 'Jason']

# If you want to add multiple elements from another list, that’s when you’d use .extend()
# adds "Alice" and "Charlie" to the end of the list
users.extend(["Alice", "Charlie"])
print(users)
# ['Morten', 'Dave', 'John', 'Jane', 'Bob', 'Jason', 'Alice', 'Charlie']

# users.extend(data)  # adds the elements of data to the end of the list
# print(users)
# ['Morten', 'Dave', 'John', 'Jane', 'Bob', 'Jason', 'Alice', 'Charlie', 'Morten', 52, 1.75, True]

# users.extend("Zoe")  # adds the letters of "Zoe" to the specified part of the list in this case
# 0 = the beginning of the list
users.insert(0, "Zoe")  # adds "Zoe" to the beginning of the list
print(users)
# ['Zoe', 'Morten', 'Dave', 'John', 'Jane', 'Bob', 'Jason', 'Alice', 'Charlie']

# users[2:2] the first 2 indicates the starting index and the second 2 indicates the ending index
# this way you won't overwrite anything in the list that was there before
# so basically if you start and end at the same value you will not replace anything
users[2:2] = ["Lars", "Mike"]  # adds "Lars" and "Mike" to the list at index 2
print(users)
# ['Zoe', 'Morten', 'Lars', 'Mike', 'Dave', 'John', 'Jane', 'Bob', 'Jason', 'Alice', 'Charlie']

# replaces the elements at index 1 and 2 with "Tom" and "Jerry"
users[1:3] = ["Tom", "Jerry"]
print(users)
# ['Zoe', 'Tom', 'Jerry', 'Mike', 'Dave', 'John', 'Jane', 'Bob', 'Jason', 'Alice', 'Charlie']

users.remove("Bob")
users.remove("Zoe")
print(users)
# ['Tom', 'Jerry', 'Mike', 'Dave', 'John', 'Jane', 'Jason', 'Alice', 'Charlie']

# removes the last element of the list and returns it so (you can see what was removed?)
print(users.pop())
# ['Tom', 'Jerry', 'Mike', 'Dave', 'John', 'Jane', 'Jason', 'Alice']
print(users)

del users[0]  # deletes the element at index 0=(the first spot in this case)
print(users)  # ['Jerry', 'Mike', 'Dave', 'John', 'Jane', 'Jason', 'Alice']

# you can also delete the whole list with the del keyword
# del data  # deletes the whole list # commented out so it doesn't throw an error/delete the list
# print(data) # Should see an error here because data is deleted

data.clear()  # clears the list but doesn't delete it
print(data)  # []

# replaces the elements at index 1(second spot) with "dave"
users[1:2] = ["daniel"]
users.sort()  # sorts the list in alphabetical order
# ['Alice', 'Dave', 'Jane', 'Jason', 'Jerry', 'John', 'daniel']
print(users)

# sorts the list in alphabetical order ignoring upper/lower case
users.sort(key=str.lower)
# ['Alice', 'daniel', 'Dave', 'Jane', 'Jason', 'Jerry', 'John']
print(users)

nums = [5, 32, 77, 4, 6]
nums.reverse()  # reverses the order of the list
print(nums)  # [6, 4, 77, 32, 5]

nums.sort(reverse=True)  # sorts the list in descending order
print(nums)  # [77, 32, 6, 5, 4]

print(sorted(nums, reverse=True))  # [77, 32, 6, 5, 4]
# sorted() creates a new list and doesn't change the original list
print(nums)  # [77, 32, 6, 5, 4]

# different ways to create a copy of a list
numscopy = nums.copy()  # creates a copy of the list
mynums = list(nums)  # creates a copy of the list
mycopy = nums[:]  # creates a copy of the list

print(numscopy)  # [77, 32, 6, 5, 4]
mycopy.sort()  # sorts the copy of the list just to showcase that it doesn't affect the original list
# as I'm changing the copy of the list and not the original list
print(mynums)  # [77, 32, 6, 5, 4]
print(mycopy)  # [77, 32, 6, 5, 4]
print(nums)  # [77, 32, 6, 5, 4]

print(type(nums))  # <class 'list'>
# just like above with the mynums = list(nums) you can create a list by imputting the content as shown below
mylist = list(["Morten", 4, 1.65, True])
print(mylist)  # ['Morten', 4, 1.65, True]
