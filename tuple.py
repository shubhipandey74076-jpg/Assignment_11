# create empty list first
temp = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    temp.append(num)

# convert list to tuple
numbers = tuple(temp)

print("Tuple:", numbers)

# operations
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))