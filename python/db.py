import psycopg2
import networkx as nx
from config import config

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
        print("The number of employees under e_id "+str(eid)+": ", cur.rowcount)
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
        print(list(row))
        #row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


g = nx.Graph()
g.add_edge('a', 'b', distance=0.3)
g.add_edge('a', 'c', distance=0.7)
print(nx.dijkstra_path_length(g, 'b', 'c', 'distance'))
if __name__ == '__main__':
    get_juniors(3)