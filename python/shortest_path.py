#function to get shortest path nodes
import networkx as nx
import psycopg2
from config import config

def get_path(node1, node2):
    conn = None
    G = nx.Graph()
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

    return nx.dijkstra_path(G ,node1, node2)