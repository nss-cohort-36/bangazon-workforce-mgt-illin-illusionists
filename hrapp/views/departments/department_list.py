import sqlite3
from django.shortcuts import render
from hrapp.models import Department
from hrapp.models import model_factory
from ..connection import Connection

def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Department)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT COUNT() emp_count, dept_name, budget, d.id
            FROM hrapp_employee e, hrapp_department d
            ON e.department_id = d.id
            GROUP BY e.department_id;
            """)

            all_departments = db_cursor.fetchall()

    template = 'departments/department_list.html'
    context = {
        'departments': all_departments
    }

    return render(request, template, context)
