import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
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

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_department
            (dept_name, budget)
            VALUES (?, ?)
            """, (form_data['dept_name'], form_data['budget']))

        return redirect(reverse('hrapp:department_list'))