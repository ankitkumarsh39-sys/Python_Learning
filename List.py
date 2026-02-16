"""marks = input("enter marks") #[50, 60, 100, 80, 90]
print(marks)
print(marks[3])"""

Students = ["Ankit", "Rohit", 60, "Rahul", "Shivam"]
print(Students)
print(Students[3])#indexing
print(Students[3:5])#list slicing
print(Students[-5:-2])#negative indexings

#Methods of list
Students.append("satyam")#add element at the end of list
print(Students)
Students.insert(3, "Aman")#add element at specific index
print("After inserting 'Aman' at index 3:", Students)
Students.remove(60)#remove element from list
print(Students)
Students.sort()#sort the list
print(Students)
Students.pop(4)#remove element at specific index
print(Students)