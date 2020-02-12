import sqlite3

from django.shortcuts import render
from hrapp.models import Computer, model_factory
from .. connection import Connection

#TODO: get individual computer details
def get_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Computer)
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT 
                c.id, 
                c.purchase_date, 
                c.decommission_date, 
                c.manufacturer, 
                c.model
            FROM hrapp_computer c
            WHERE c.id = ?;
        """, (computer_id,))

        computer = db_cursor.fetchone()
        # print(computer.manufacturer, computer.model)

        return computer

#TODO: setup and render detail template
def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)
        template = 'computers/detail.html'
        context = {
            'computer': computer
        }
        return render(request, template, context)