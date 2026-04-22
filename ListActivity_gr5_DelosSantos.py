# 🔹 Activity 1: Create a List
fruits = ["apple", "banana", "cherry"]
print(fruits)


# 🔹 Activity 2: Access Items
print(fruits[0])   # first item
print(fruits[-1])  # last item


# 🔹 Activity 3: List Length
colors = ["red", "blue", "green", "yellow"]
print(len(colors))


# 🔹 Activity 4: Change Item
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)


# 🔹 Activity 5: Add Items
fruits = ["apple", "banana"]
fruits.append("mango")
fruits.insert(1, "grape")
print(fruits)


# 🔹 Activity 6: Remove Items
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
fruits.pop()
print(fruits)


# 🔹 Activity 7: For Loop
animals = ["dog", "cat", "bird"]

for animal in animals:
    print(animal)


# 🔹 Activity 8: With Index
numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(i, ":", numbers[i])


# 🔹 Activity 9: Check if Item Exists
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("banana is in the list")


# 🔹 Activity 10: Sorting
numbers = [5, 2, 9, 1]

numbers.sort()
print(numbers)  # ascending

numbers.sort(reverse=True)
print(numbers)  # descending


# 🔹 Activity 11: Copy List
list1 = ["a", "b", "c"]
list2 = list1.copy()

print(list2)
