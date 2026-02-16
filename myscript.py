""" # variables and Data Types in Python
name="ankit"
print("my name is", name, "i am learning python programming")
age = 21
print("my age is", age)
CTC = 10.5
print("my CTC is", CTC, "lpa")
Profile = (name, age, CTC)
print("my profile is :", Profile)
print(type(name))
print(type(age))
print(type(CTC))
print(type(Profile))

# arithmetic operations
a = 2
b = 3
c = a + b
print("the sum of a and b is:", c)
print(a - b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a == b)
print( a != b)

# assignment operators
x = 5
x += 3
print(x)

#logical operators
p = True
q = False
print(p and q)
print(p or q)   
print(not p)

#type conversion
a = 2
b = 3.5
c = complex(a)
print(c)
print(type(c))
print(a * b)

# intput in Python
input_str = input("Enter a number: ")
num = float(input_str)
print("You entered:", num)
print("Type of num is:", type(num))

# pratice set
# write a program to take two numbers as input and print their sum
input_srt1 = input("Enter first number :")
num1 = int(input_srt1)
num2 = int(input("Enter second number :"))
print("the sum of num1 and num2 is :", num1 + num2)

#WAP to take the radius of a circle as input and print its area.
radius = input("enter the radui        s of circle :")
radius = float(radius)
area = 3.14 * radius * radius
print("the area of circle is :", area)

#string formatting
str = "This is Ankit"
print("the string is :", str)

# Indexing and slicing
print(str[0])
print(str[9:])
ch = str[2:7]
print(ch)
print("count is :",str.count("is"))

name = input("Enter your first name :")
print("length of your name is :", len(name))
print("finding", name.find("e"))
print("count a string :", name.count("a"))

# if-elif-else statement
age = 2
if(age >= 18):
    if(age >= 40):
        print("you are eligible to vote", age)
    else:
        print("you can also drive")
elif(age >= 18):
    print("you are a teenager", age)
else:
    print("you are a chile", age)

# practice set
# WAP to take input of age of 3 people and determine oldest and youngest among them.
age1 = int(input("enture age of first person :"))
age2 = int(input("enter age of second person :"))
age3 = int(input("enter age of third person :"))
if(age1 >= age2 and age1 >= age3):
    print("first person is oldest")
    if(age2 < age3):
        print("second person is youngest")
else:
        print("third person is youngest")

marks = input("entre your maks :")
marks = float(marks)
if(marks >=90):
     grede = "A"
elif(marks >=80 and marks < 90):
     grade = "B"
elif(marks >=70 and marks < 80):
     grade = "C"
else: 
     grade = "D"
     print("your grade is :", grade)
"""

                
    # Simple decision-making system
def get_recommendation(marks, age):
        """
        Decision-making system that provides recommendations based on marks and age
        """
        recommendations = []
        
        if marks >= 90:
            recommendations.append("Excellent performance! Consider advanced courses.")
        elif marks >= 80:
            recommendations.append("Good performance! Keep up the effort.")
        elif marks >= 70:
            recommendations.append("Average performance. Focus on weak areas.")
        else:
            recommendations.append("Need improvement. Seek additional help.")
        
        if age < 18:
            recommendations.append("You are a student. Focus on education.")
        elif age >= 18 and age < 25:
            recommendations.append("You are young professional. Build your skills.")
        else:
            recommendations.append("You have experience. Share knowledge with others.")
        
        return recommendations
# Test the decision-making system
user_marks = float(input("Enter your marks: "))
user_age = int(input("Enter your age: "))

advice = get_recommendation(user_marks, user_age)
print("\nRecommendations:")
for i, recommendation in enumerate(advice, 1):
        print(f"{i}. {recommendation}")
else:
    print("No recommendations available.")

    """Once you provide more details, I can help you write the appropriate code."""