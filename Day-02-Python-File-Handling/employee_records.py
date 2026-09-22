employee_records=["Kabil-Developer\n","Arun-Tester\n","Priya-Designer\n"]

with open("employee_records.txt","w", encoding="utf-8") as file:
    file.writelines(employee_records)

with open ("employee_records.txt","r",encoding="utf-8")as file:
    data=file.readlines()   
    print(data)
for emp in data:
    print(emp.strip())  