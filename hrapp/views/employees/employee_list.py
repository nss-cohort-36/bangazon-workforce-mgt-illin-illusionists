import sqlite3
from django.shortcuts import render
from hrapp.models import Employee
from hrapp.models import Department
from ..connection import Connection

def employee_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # TODO: Add to query: e.department,
            db_cursor.execute("""
            	select
                e.id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor,
                d.dept_name
                from hrapp_employee e
                join hrapp_department d               
                on e.department_id = d.id
            """)

            all_employees = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                employee = Employee()
                employee.id = row['id']
                employee.first_name = row['first_name']
                employee.last_name = row['last_name']
                employee.start_date = row['start_date']
                employee.is_supervisor = row['is_supervisor']
                
                department = Department()
                department.name = row['dept_name']
                
                employee.department = department

                all_employees.append(employee)
    
            template = 'employees/employees_list.html'
            context = {
            'employees': all_employees
                }
            return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_employee
            (first_name, last_name, start_date, is_supervisor, department_id)
            VALUES(?,?,?,?,?)
            """, (form_data['first_name'], form_data['last_name'], form_data['start_date'], form_data['is_supervisor'], form_data['department_id']))

        return redirect(reverse('hrapp:employee_list'))

