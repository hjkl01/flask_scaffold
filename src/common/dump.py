# import json
# from models import Project, Saler, SalesTicket, Purchase, PurchaseTicket, Cost, File, Employees, Market

import records
import setting


def dump():

    table_names = [
        'project_project'
    ]

    db = records.Database(setting.DATABASE_URL)
    for table_name in table_names:
        dump_detail(db, table_name)


def dump_detail(db, table_name):

    rows = db.query('select * from %s' % table_name)

    with open('result/%s.json' % table_name, 'w') as file:
        file.write(rows.export('json'))
