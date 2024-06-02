# add employee function
# 1,Swati,Mehta,24,kolkata,patna,tcs,2022,ase,24000
def add_emp(employee_dict, file_path):
    file = open(file_path, "a")
    emp_data = input("enter new employee detail:")
    file.write(emp_data + "\n")
    data = emp_data.split(",")
    employee_dict[data[0]] = {
        "fname": data[1],
        "lname": data[2],
        "age": int(data[3]),
        "city": data[4],
        "home": data[5],
        "company": data[6],
        "year": data[7],
        "designation": data[8],
        "salary": data[9]
    }
    file.close()
    return employee_dict
