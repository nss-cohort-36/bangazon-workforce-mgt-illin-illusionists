import sqlite3
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from hrapp.models import Department

def employee_form(request):
    if request.method == 'GET':
          with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # TODO: Add to query: e.department,
            db_cursor.execute("""
               select id, dept_name
               from hrapp_department            
            """)

            all_departments = []
            dataset = db_cursor.fetchall()
            for row in dataset:
                department = Department()
                department.id = row['id']
                department.dept_name = row['dept_name']
                all_departments.append(department)
    template = 'employees/form.html'
    context = {'all_departments': all_departments}

    return render(request, template, context)
