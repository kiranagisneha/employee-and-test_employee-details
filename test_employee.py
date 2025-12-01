from employee import employee_details

def test_employee_details():
    # sample input
    name = "alice"
    emp_id = "E101"
    department = "IT"
    salary = 55000

    expected_output = (
        "Employee Name: alice\n"
        "Employee ID: E101\n"
        "Department: IT\n"
        "Salary: 55000"
    )

    assert employee_details(name, emp_id, department, salary) == expected_output
