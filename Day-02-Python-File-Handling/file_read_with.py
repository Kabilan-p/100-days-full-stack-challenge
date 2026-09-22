##########READ()########
# with open("employee.txt", "r") as file:
#     data = file.read()
#     print(data)


######READLINE()########
with open("employee.txt","r") as file:
    data=file.readline()
    data1=file.readline()
    print(data)
    print(data1)    


    #####READLINES()########

with open("employee.txt", "r") as file:
    employees = file.readlines()

for employee in employees:
 print(employee.strip())


#  write()      → string எழுதும்
# writelines() → multiple strings எழுதலாம்

# read()       → full content
# readline()   → one line
# readlines()  → all lines as list