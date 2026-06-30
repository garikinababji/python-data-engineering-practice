=============================================
# Topic:  with_statement_practice
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================


file = open("D:\\GCP_2026\\practice\\sample.txt", "r")

content = file.read()

print(content)

file.close()

# This is a better way to read a file using the 'with' statement, which automatically handles closing the file after its suite finishes, even if an exception is raised.


with open("D:\\GCP_2026\\practice\\sample.txt", "r") as file:
    content = file.read()
    print(content)

# Another way to read a file line by line using the 'with' statement.

with open("D:\\GCP_2026\\practice\\sample_2.txt", "r") as file:
    for line in file:
        print(line)

# Writing to a file using the 'with' statement.

with open("D:\\GCP_2026\\practice\\output.txt", "w") as file:
    file.write("Hello Babji")

with open("D:\\GCP_2026\\practice\\output.txt", "a") as file:
    file.write("\nWelcome to GCP")

# Reading from a file using the 'with' statement.

with open("D:\\GCP_2026\\practice\\output.txt", "r") as file:
    content = file.read()
    
    print(content)

# Writing to a log file using the 'with ETL' statement.

with open("D:\\GCP_2026\\practice\\etl_log.txt", "a") as file: # appeding to the log file
    file.write("Customer File Loaded Successfully\n")

with open("D:\\GCP_2026\\practice\\etl_log.txt", "r") as file:
    content = file.read()
    print(content)
