import sqlite3
from django.shortcuts import render
from hrapp.models import Department
from ..connection import Connection

def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT COUNT() emp_count, dept_name, budget
            FROM hrapp_employee e, hrapp_department d
            ON e.department_id = d.id
            GROUP BY e.department_id;
            """)

            all_departments = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                department = Department()
                department.emp_count = row['emp_count']
                department.dept_name = row['dept_name']
                department.budget = row['budget']

                all_departments.append(department)

    template = 'departments/department_list.html'
    context = {
        'departments': all_departments
    }

    return render(request, template, context)
