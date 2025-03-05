#Problem 1: Count the frequency of elements in a list

name="joseph,santhosh,kumar,joshva,joseph,santhosh,sonthash,joshva,santhosh,"
name=name.split(",")
print(name)
name_count={}
for i in name:
    name_count[i]=name_count.get(i,0)+1
print(name_count)
for key,value in name_count.items():
    print(key,value)

#Problem 2: Find the maximum value in a dictionary

scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 91}
max_key = None
max_value = float('-inf')  
for key, value in scores.items():
    if value > max_value:
        max_value = value
        max_key = key

print(f"The highest score is {max_value}, achieved by {max_key}")

#Problem 3: Merge two dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
for key, value in dict2.items():
    dict1[key] = value  

print(dict1)

#Problem 4: Get the sum of all values in a dictionary
prices = {'apple': 2, 'banana': 3, 'orange': 1.5}

total_price = 0
for price in prices.values():
    total_price += price

print(f"The total price is {total_price}")

#Problem 5: Remove keys with a certain condition

ages = {'Alice': 30, 'Bob': 18, 'Charlie': 25, 'David': 15}
threshold = 20
keys_to_remove = []
for key, value in ages.items():
    if value < threshold:
        keys_to_remove.append(key)
for key in keys_to_remove:
    del ages[key]

print(ages)
#Problem 6: Update dictionary values using a function

numbers = {'a': 2, 'b': 3, 'c': 4}
def square(x):
    return x ** 2
for key in numbers:
    numbers[key] = square(numbers[key])

print(numbers)

#Problem 7: Filtering dictionary by value

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = {}
for key, value in my_dict.items():
    if value > 2:
        filtered_dict[key] = value

print(filtered_dict)

#Problem 8:Modifying values in a dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    my_dict[key] = my_dict[key] * 2

print(my_dict)

#Problem 9:Looping through dictionary key-value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

