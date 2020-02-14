import sqlite3

from django.shortcuts import render
from hrapp.models import Employee, model_factory
from hrapp.models import TrainingProgram
from .. connection import Connection
from django.contrib.auth.decorators import login_required

#TODO: get individual employee details
def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                e.id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor,
                d.dept_name,
                c.manufacturer,
                c.model,
                tp.title as training
                
                from hrapp_employee e
                left join hrapp_department d          
                on e.department_id = d.id
                left join hrapp_employeecomputer ec 
                on e.id = ec.employee_id
                left join hrapp_computer c
                on ec.computer_id = c.id
                left join hrapp_trainingprogramemployee tpe
                on e.id = tpe.employee_id
                left join hrapp_trainingprogram tp 
                on tpe.training_program_id = tp.id
           
           where e.id=?
      
           
        """, (employee_id,))

        employee_rows = db_cursor.fetchall()
        print (employee_rows)

        employee_groups = {}

        for (employee, ) in employee_rows:
                # create key if not in dict
            if employee.id not in employee_groups:
                employee_groups[employee.id] = employee
                # append book to employee in dict
            employee_groups[employee.id].trainings.append(employee.training)
        print (employee_groups[employee.id])
        print (employee_groups[employee.id].trainings)

        return employee_groups

#TODO: setup and render detail template
@login_required
def employee_details(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)
        template = 'employees/detail.html'
        context = {
            'employee': employee[employee_id]
        }
        return render(request, template, context)

def create_employee(cursor, row):
    _row = sqlite3.Row(cursor, row)

    employee = Employee()
    employee.id = _row['id']
    employee.first_name = _row['first_name']
    employee.last_name = _row['last_name']
    employee.dept_name = _row['dept_name']

    if _row['model'] is not None:
        employee.computer = _row['manufacturer'] + ' ' +  _row['model']
    else: employee.computer = "Not Assigned"

    employee.start_date = _row['start_date']
    employee.is_supervisor = _row['is_supervisor']

    if _row["training"] is not None:
        employee.training = _row["training"]
    else: employee.training = "Not Assigned"

    employee.trainings= []

    return (employee, )