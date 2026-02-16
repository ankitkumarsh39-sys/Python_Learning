# tuples are immutable

"""tup = (1,23,3,4,5)
print(tup)
print(type(tup))
print(tup.count(3))"""

#Wap to take input from user and print the type of input
"""name = []
input_str = input("enter namees :")

print("your inuput is: ", input_str)
print((name.append(input_str)))
print("the type of input is : ", type(name))
print(name)
"""

# palandrome
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list2:
    print("palandrome")
else:
    print("not palandrome")