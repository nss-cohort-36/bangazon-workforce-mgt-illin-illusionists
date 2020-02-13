import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from hrapp.models import model_factory
from ..connection import Connection

def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Department)
        db_cursor = conn.cursor()

#         SELECT 
# e.first_name,
# e.last_name,
# d.dept_name
# FROM hrapp_employee e, hrapp_department d
# WHERE e.department_id = d.id;

        db_cursor.execute("""
        SELECT 
            e.first_name,
            e.last_name,
            d.dept_name
            FROM hrapp_employee e, hrapp_department d
            where e.department_id = d.id;
        """, (department_id,))

        return db_cursor.fetchone()

# @login_required
def department_details(request, department_id):
    if request.method == 'GET':
        library = get_department(department_id)

        template = 'departments/department_details.html'
        context = {
            'department': department
        }

        return render(request, template, context)