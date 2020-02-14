import sqlite3
from django.shortcuts import redirect, render, reverse
from hrapp.models import TrainingProgram
from ..connection import Connection



def get_training_program(program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute( """
        SELECT
        tp.title,
        tp.start_date,
        tp.end_date,
        tp.capacity,
        e.first_name as employee_first_name,
        e.last_name as employee_last_name
        FROM hrapp_trainingprogram tp
        LEFT JOIN hrapp_trainingprogramemployee tpe
        ON tp.id = tpe.training_program_id
        LEFT JOIN hrapp_employee e
        ON tpe.employee_id = e.id
        WHERE tp.id = ?
        """, (program_id,))

        return db_cursor.fetchone()

def training_details(request, program_id):
    if request.method == 'GET':
        program = get_training_program(program_id)

        template = 'trainingprograms/detail.html'
        context = {
            'program': program
        }

    return render(request, template, context)