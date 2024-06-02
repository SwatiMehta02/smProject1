import os
from erm.emp_utils import add_emp


def prepare_data():
    num = int(input("Enter number of employee:"))
    file = open(file_path, "a")
    for count in range(num):
        emp = input("enter emp" + str(count + 1) + " details:")
        file.write(emp + "\n")
    file.close()

    # ['1', 'Swati', 'Mehta', '24', 'kolkata', 'patna', 'tcs', '2022', 'ase', '24000\n']

    file1 = open(file_path, "r")
    flag = True
    employee = {}
    while flag:
        line = file1.readline()
        if line == "":
            flag = False
        else:
            # print(line)
            data = line.strip().split(",")
            employee[data[0]] = {
                "fname": data[1],
                "lname": data[2],
                "full_name": data[1] + " " + data[2],
                "age": data[3],
                "city": data[4],
                "home": data[5],
                "company": data[6],
                "year": data[7],
                "designation": data[8],
                "salary": data[9]
            }
    file1.close()
    return employee


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError as ex:
        print("file does not exist")


file_path = "/mnt/c/Users/RISHAV/OneDrive/Desktop/MyCodeBase/Python/smProject1/src/emp_data.txt"

delete_file(file_path)

employee = prepare_data()
print(employee)
print("-" * 60)
add_emp(employee, file_path)
print(employee)
# employee = add_emp(employee, file_path)
# print(employee)
