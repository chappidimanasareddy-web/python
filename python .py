# Student Information & Marks Calculator

# Input
name = input("Enter name: ")
age = int(input("Enter age: "))

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))

# Calculate total and average
total = maths + python + english
average = total / 3

# Boolean variable
is_student = True

# Output
print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)
print("Maths:", maths)
print("Python:", python)
print("English:", english)
print("Total Marks:", total)
print("Average Marks:", average)
print("Is Student:", is_student)

# Data Types
print("\n--- Data Types ---")
print("Name:", type(name))
print("Age:", type(age))
print("Maths:", type(maths))
print("Python:", type(python))
print("English:", type(english))
print("Total:", type(total))
print("Average:", type(average))
print("Is Student:", type(is_student))

# Type Conversion
age_string = str(age)
print("\nAge converted to string:", age_string)
print("Converted type:", type(age_string))