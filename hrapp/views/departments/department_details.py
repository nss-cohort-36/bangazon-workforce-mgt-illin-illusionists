import sqlite3
# from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from hrapp.models import Employee
from hrapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required


def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Department)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        d.id,
        d.dept_name,
        d.budget,
        e.first_name,
        e.last_name,
        e.department_id	
        FROM hrapp_department d
        LEFT JOIN hrapp_employee e
        ON e.department_id = d.id;
        """, ( ))

        department = db_cursor.fetchone()
        return department

@login_required
def department_details(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)

        template = 'departments/department_details.html'
        context = {
            'department': department
        }

        return render(request, template, context)