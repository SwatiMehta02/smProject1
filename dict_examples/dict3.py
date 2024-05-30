employee = {
    2205609: {
        "fname": "swati",
        "lname": "mehta",
        "designation": "ase",
        "skills": ["python", "openshift"],
        "email": "itsswatimehta@gmail.com",
        "is_active": True
    },
    1796682: {
        "name": ("rishav", "anurag"),
        "designation": "se",
        "skills": ["python", "openshift"],
        "email": "its@gmail.com",
        "is_active": False
    },
    1234598: {
        "designation": "se",
        "skills": ["python", "java"],
        "email": "its2@gmail.com",
        "is_active": False,
        "fname": "",
        "lname": "",
        "name": ("Gaurav", "Bhadra")
    }
}
for emp_id in employee:
    fname = employee.get(emp_id).get("fname", "")
    lname = employee.get(emp_id).get("lname", "")
    full_name = fname + " " + lname
    if full_name == " ":
        full_name = employee.get(emp_id).get("name")[0] + " " + employee.get(emp_id).get("name")[1]
    print(emp_id, full_name)

    # print(emp_id,employee.get(emp_id).get("fname",))
