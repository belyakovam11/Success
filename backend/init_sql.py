# init_sql.py
from django.db import connection

def run_sql():
    with open("init.sql") as f:
        sql = f.read()
        with connection.cursor() as cursor:
            cursor.execute(sql)

if __name__ == "__main__":
    run_sql()
