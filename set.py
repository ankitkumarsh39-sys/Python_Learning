# A set is an unordered collection of unique elements. It is defined using curly braces {} or the set() constructor.
# set is mutable but it does not allow duplicate values and it is unordered collection of unique elements
# set is collection of unique elements and it is mutable but it does not allow duplicate values and it is unordered collection of unique elements
# set is mutable but its elements are immutable
# unhashable means that the elements of a set cannot be changed after they are added to the set. This is because sets use a hash function to store and retrieve elements, and if the elements were mutable, their hash values could change, leading to inconsistencies in the set.
nums ={1,2,3,4,5}
"""print(nums)
print(type(nums))"""

# empty set
empty_set = set()
empty_set.add(1)# method to add element in set
empty_set.add(2)
empty_set.add(3)
empty_set.add(5.5)
print(type(empty_set))
print(empty_set)
print(len(empty_set))
print(list(empty_set))#to convert set to list
"""empty_set.clear()#to clear the set
print(len(empty_set))"""
print(empty_set.pop())#to remove and return an arbitrary element from the set

print(nums.union(empty_set))#to return a new set that is the union of two sets
print(nums.intersection(empty_set))#to return a new set that is the intersection of two sets
print(nums)
print(empty_set)