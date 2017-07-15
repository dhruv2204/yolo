import psycopg2
import psycopg2.extras
from config import config
from shortest_path import get_path

def get_juniors(eid):
    """ query data from the employees table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("WITH RECURSIVE juniors AS (SELECT e_id, m_id, name, value_in_company FROM "+
                    "employees WHERE e_id = %s UNION SELECT e.e_id, e.m_id, e.name, e.value_in_company "+
                    "FROM employees e INNER JOIN juniors s ON s.e_id = e.m_id ) "+
                    "SELECT cast(json_agg(res) as text) FROM juniors res;", [eid])
        
        row = cur.fetchall()
        # while row is not None:
        return row[0][0]
        #row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_senior_tree(eid):
    """ query data from the employees table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("WITH RECURSIVE senior AS (SELECT e_id, m_id, name, value_in_company FROM "+
                    "employees WHERE e_id = (SELECT m_id from employees WHERE e_id= %s) UNION SELECT e.e_id, e.m_id, e.name, e.value_in_company "+
                    "FROM employees e INNER JOIN senior s ON s.e_id = e.m_id ) "+
                    "SELECT cast(json_agg(res) as text) FROM senior res;", [eid])
        print("The number of employees under senior of e_id "+str(eid)+": ", cur.rowcount)
        row = cur.fetchall()
  
        # while row is not None:
        return row[0][0]
        #row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_eid_json(eid, js):
    """ insert data into employees_json table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("INSERT INTO employees_json VALUES(%s, %s);",(eid, js))
        #cur.execute("""SELECT e_id, subtree->>'customer' AS source_url, subtree->>'items' FROM employees_json""")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    js= '{ "customer": "Lily Bush", "items": {"product": "Diaper","qty": 24}}'
    print(get_juniors(3))
    print(get_senior_tree(11))
    print(get_path(1, 20))
    #get_late_joining(4)
    insert_eid_json(1, js)