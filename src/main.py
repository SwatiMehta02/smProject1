# print("---------"*4+"Welcome to ERM"+"---------"*4)

# str1 = "Swati Mehta"
# print([i for i in str1])
# print(str1.split('i'))

employee = [
    # "1,Swati,Mehta,24,kolkata,patna,tcs,2022,ase,24000",
    # "2,Rishav,Anurag,25,kolkata,patna,tcs,2021,se,24000",
    # "3,Rishav1,Anurag1,51,kolkata1,patna1,tcs1,2023,se1,24001"
]
emp_data = {}

count_of_employee = int(input("Enter number of employee:"))
for count in range(count_of_employee):
    new_emp = input("enter emp" + str(count + 1) + ":")
    employee.append(new_emp)

for emp in employee:
    emp_split = emp.split(",")
    # ['1', 'Swati', 'Mehta', '24', 'kolkata', 'patna', 'tcs', '2022', 'ase', '24000']
    emp_data[emp_split[0]] = {
        "fname": emp_split[1],
        "lname": emp_split[2],
        "fullname": emp_split[1] + " " + emp_split[2],
        "age": int(emp_split[3]),
        "city": emp_split[4],
        "company": emp_split[6],
        "salary": emp_split[9],
        "designation": emp_split[8],
        "year": emp_split[7]
    }
print(emp_data)
print("-----------------------------------------------------------")
for emp in emp_data:
    if emp_data.get(emp).get("fullname") == "Swati Mehta":
        emp_data[emp]["age"] += 1
print(emp_data)
print("-"*60)
for emp in emp_data:
    if emp_data.get(emp).get("age") >= 24:
        emp_data[emp]["skills"] = ["Java"]
    else:
        emp_data[emp]["skills"] = ["python", "docker"]
print(emp_data)
