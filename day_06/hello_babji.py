
'''
with open("D:\\GCP_2026\\practice\\Python\\day_06\\hello.txt", "w") as file:
	file.write("Hello Babji")
''
with open("D:\\GCP_2026\\practice\\Python\\day_06\\hello.txt", "a") as file:
	file.write("\nLearning Python")


''
with open("D:\\GCP_2026\\practice\\Python\\day_06\\hello.txt", "r") as file:
	content = file.read()
	print(content)

''

import csv

with open("D:\\GCP_2026\\practice\\sample_csv_3.txt", "r") as file:
	reader= csv.DictReader(file)
	
	for row in reader:
		print(row['name'])    
''

import csv

with open("D:\\GCP_2026\\practice\\csv_status.txt", "r") as file:
	reader= csv.DictReader(file)
	
	for row in reader:
		if row['status'] == 'Active':
			print(row['name'])

'''

import csv

def is_active(status):
    with open("D:\\GCP_2026\\practice\\csv_status.txt", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['status'] == 'Active':
                print(row['name'])

    return status == "Active"

#is_active("name")
#print(is_active("Active"))  # Output: True

