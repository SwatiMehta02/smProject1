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


def all_employee_from_location(employee_dict, location):
    emp_list = []
    for id in employee_dict:
        if employee_dict[id]["city"] == location:
            emp_list.append((id, employee_dict[id]["fname"]))
    return emp_list


def emp_with_designation(emp_dict, designation):
    """
    checking designation
    :param emp_dict:
    :param designation:
    :return: list of tuple having id, fname
    """
    list_emp = []
    for id in emp_dict:
        if emp_dict[id]["designation"] == designation:
            list_emp.append((id, emp_dict[id]["fname"] + " " + emp_dict[id]["lname"]))
    return list_emp


def all_employee(dict_emp, field_to_check, field_value):
    """
    to check field and its corresponding values, it will return list of employee
    :param dict_emp:
    :param field_to_check:
    :param field_value:
    :return: [(id, fname), ...........]
    """
    emp_list = []
    try:
        for id in dict_emp:
            if dict_emp[id].get(field_to_check) == field_value:
                emp_list.append((id, dict_emp[id].get("fname", "not present")))
        return emp_list
    except Exception as ex:
        return emp_list


def remove_employee(emp, id):
    if id in emp:
        del emp[id]
        return True
    else:
        return False
#
#
# emp = {
#     # '5': {'fname': 'Swati7', 'lname': 'Mehta', 'full_name': 'Swati7 Mehta', 'age': '24', 'city': 'kolkata',
#     #              'home': 'patna', 'company': 'tcs', 'year': '2022', 'designation': 'ase', 'salary': '24000'},
#     '1': {'fname': 'Swati2', 'lname': 'Mehta', 'full_name': 'Swati2 Mehta', 'age': '24', 'city': 'kolkata',
#           'home': 'patna', 'company': 'tcs', 'year': '2022', 'designation': 'ase', 'salary': '24000'},
#     '2': {'lname': 'Mehta', 'full_name': 'Swati2 Mehta', 'age': '24', 'city': 'kolkata',
#           'home': 'patna', 'company': 'tcs', 'year': '2022', 'designation': 'ase', 'salary': '24000'},
#     '3': {'fname': 'Swati2', 'lname': 'Mehta', 'age': 24, 'city': 'kolkata', 'home': 'patna', 'company': 'tcs',
#           'year': '2022', 'designation': 'ase', 'salary': '24000'},
#     '5': 8
# }
# # emp = 1345678
#
# # print(all_employee_from_location(emp, "kolkata"))
# # print(emp_with_designation(emp, "ase"))
# # print(all_employee(emp, "year", "2022"))
# # print(all_employee(emp, "city", "kolkata"))
# # print(all_employee(emp, "fname", 67))
# print(remove_employee(emp,'5'))
# print(emp)