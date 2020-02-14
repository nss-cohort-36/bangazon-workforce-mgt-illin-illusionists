import sqlite3
import datetime
from django.shortcuts import render, reverse, redirect
from hrapp.models import TrainingProgram
from ..connection import Connection


def training_program_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            

            db_cursor = conn.cursor()
            db_cursor.execute(
                """
                SELECT 
                tp.id, 
                tp.title, 
                tp.start_date, 
                tp.end_date, 
                tp.capacity
                FROM hrapp_trainingprogram tp
                WHERE tp.start_date > date()
                """
            )

            all_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                training_program = TrainingProgram()
                training_program.program_id = row['id']
                training_program.title = row['title']
                training_program.start_date = row['start_date']
                training_program.end_date = row['end_date']
                training_program.capacity = row['capacity']

                all_programs.append(training_program)

        template = 'trainingprograms/trainingprograms_list.html'
        context = {
            'all_programs': all_programs
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()
            db_cursor.execute("""
            INSERT INTO hrapp_trainingprogram
            (title, start_date, end_date, capacity)
            VALUES (?, ?, ?, ?)
            """,
            (form_data['title'], form_data['start_date'], form_data['end_date'], form_data['capacity']
            ))
        return redirect(reverse('hrapp:training_list'))