import sqlite3

from django.shortcuts import render
from hrapp.models import Employee, model_factory
from .. connection import Connection

#TODO: get individual employee details
def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Employee)
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
                c.model
                 
                from hrapp_employee e
                join hrapp_department d          
                on e.department_id = d.id
                join hrapp_employeecomputer ec 
                on e.id = ec.employee_id
                join hrapp_computer c
                on ec.computer_id = c.id
              where e.id=?
        """, (employee_id,))
        employee = db_cursor.fetchone()
        return employee

#TODO: setup and render detail template
def employee_details(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)
        template = 'employees/detail.html'
        context = {
            'employee': employee
        }
        return render(request, template, context)