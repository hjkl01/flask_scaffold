import setting
import records


def alter_table():

    sqls = [
        'alter table project_project ALTER column cost type NUMERIC;',
    ]

    db = records.Database(setting.DATABASE_URL)
    for sql in sqls:
        db.query(sql)
