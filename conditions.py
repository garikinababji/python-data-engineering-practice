
# Conditional Statements in Python
marks = 75

if marks >= 35:
    print("Pass")
else:
    print("Fail")


score = int(input("Enter your score: "))

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
else:
    print("Grade C")


#age check

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# bigquery file size check

file_size_mb = 120

if file_size_mb > 100:
    print("Large file - process in batches")
else:
    print("Process normally")


#vote eligibility

age=20
if age>=18:
	print("Eligible to Vote")
else:
	print("Not Eligible")

 # test marks   

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

# task 1

employee = {
"emp_id": 101,
"emp_name": "Babji",
"emp_exp": 4
}
if employee["emp_exp"]>=4:
	print("Experienced Data Engineer")
else:
	print("Learning Stage")