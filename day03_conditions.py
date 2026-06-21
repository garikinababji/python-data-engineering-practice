=============================================
# Topic: Python conditions
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================
# Conditional Statements in Python
# Task 1
marks = 75

if marks >= 35:
    print("Pass")
else:
    print("Fail")

# Task 2
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
else:
    print("Grade C")


#age check
# Task 3

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Task 4
# bigquery file size check

file_size_mb = 120

if file_size_mb > 100:
    print("Large file - process in batches")
else:
    print("Process normally")

# Task 5
#vote eligibility

age=20
if age>=18:
	print("Eligible to Vote")
else:
	print("Not Eligible")

 # test marks   
# Task 6

m=int(input("Enter Marks: "))
if m>100:
    print("Invalid Marks")
elif m>=90 and m<=100:
	print("A")
elif m>=75 and m<=89:
	print("B")
elif m<=74 and m>=50:
	print("C")
else:
	print("Fail")

# Task 7

employee = {
"emp_id": 101,
"emp_name": "Babji",
"emp_exp": 4
}
if employee["emp_exp"]>=4:
	print("Experienced Data Engineer")
else:
	print("Learning Stage")
