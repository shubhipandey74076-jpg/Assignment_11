# create dictionary
student = {
    "name": "Rahul",
    "age": 18,
    "course": "BCA"
}

# print dictionary
print("Student Details:", student)

# access value
print("Name:", student["name"])






#advance dic with user input 
student = {}

# add data
n = int(input("How many students: "))

for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    student[name] = age   # store in dictionary (details)

# print dictionary
print("\nStudent Dictionary:", student)

#search according to your need 
search = input("Enter name to search: ")

if search in student:
    print("Age =", student[search])
else:
    print("Student not found")

