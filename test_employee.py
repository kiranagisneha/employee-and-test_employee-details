from employee import employee_details
def test_employee_details():
    expected_output = (
        "Employee Name: alice\n"
        "Employee ID: E101\n"
        "Department: IT\n"
        "Salary: 55000"
    )
    assert employee_details(name, emp_id, department, salary) == expected_output
