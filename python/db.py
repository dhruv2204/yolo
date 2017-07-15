import psycopg2
from config import config

def get_juniors(eid):
    """ query data from the employees table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("WITH RECURSIVE juniors AS (SELECT e_id, m_id, name FROM "+
                    "employees WHERE e_id = %s UNION SELECT e.e_id, e.m_id, e.name "+
                    "FROM employees e INNER JOIN juniors s ON s.e_id = e.m_id ) "+
                    "SELECT cast(row_to_json(res) as text) FROM juniors res;", [eid])
        print("The number of employees under e_id 2: ", cur.rowcount)
        row = cur.fetchall()
  
        # while row is not None:
        print(list(row))
        #row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
 
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.exe
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    get_juniors(2)