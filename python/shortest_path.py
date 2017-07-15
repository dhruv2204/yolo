import psycopg2
import networkx as nx
from config import config

G = nx.Graph()

def get_juniors():
    """ query data from the employees table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("WITH RECURSIVE juniors AS (SELECT e_id, m_id, name, value_in_company FROM "+
                    "employees UNION SELECT e.e_id, e.m_id, e.name, e.value_in_company "+
                    "FROM employees e INNER JOIN juniors s ON s.e_id = e.m_id ) "+
                    "SELECT * FROM juniors;")
        row = cur.fetchone()
        # while row is not None:
        #     G.add_node(row[0])
        #     row=cur.fetchone()

        while row is not None:
            G.add_edge(row[-3],row[0], distance=row[-1])
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_juniors()
print(nx.dijkstra_path_length(G ,1, 7, "distance"))