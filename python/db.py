import psycopg2
import psycopg2.extras
import networkx as nx
import json
from config import config
from shortest_path import get_path
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)
api = Api(app)

class Juniors(Resource):
    def get(self, eid):
        """ query data from the employees table """
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("WITH RECURSIVE juniors AS (SELECT e_id, m_id, name, value_in_company FROM "+
                        "employees WHERE e_id = %s UNION SELECT e.e_id, e.m_id, e.name, e.value_in_company "+
                        "FROM employees e INNER JOIN juniors s ON s.e_id = e.m_id ) "+
                        "SELECT * FROM juniors;", [eid])

            return cur.fetchall()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                
class Senior_Tree(Resource):
    def get(self, eid):
        """ query data from the employees table """
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("WITH RECURSIVE senior AS (SELECT e_id, m_id, name, value_in_company FROM "+
                        "employees WHERE e_id = (SELECT m_id from employees WHERE e_id= %s) UNION SELECT e.e_id, e.m_id, e.name, e.value_in_company "+
                        "FROM employees e INNER JOIN senior s ON s.e_id = e.m_id ) "+
                        "SELECT * FROM senior;", [eid])
            print("The number of employees under senior of e_id "+str(eid)+": ", cur.rowcount)
    
            #row = cur.fetchall()
            # while row is not None:
            return cur.fetchall()
            #row = cur.fetchone()
    
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:    
            if conn is not None:
                conn.close()

# class Insert_Json(Resource):
#     def put(self, eid, js):
#         """ insert data into employees_json table """
#         conn = None
#         try:
#             params = config()
#             conn = psycopg2.connect(**params)
#             cur = conn.cursor()
#             cur.execute("INSERT INTO employees_json VALUES(%s, %s);",(eid, js))
#             #cur.execute("""SELECT e_id, subtree->>'customer' AS source_url, subtree->>'items' FROM employees_json""")
#             cur.close()
#         except (Exception, psycopg2.DatabaseError) as error:
#             print(error)
#         finally:
#             if conn is not None:
#                 conn.close()

class Shortest_Path(Resource):
    def get(self, node1, node2):
        conn = None
        G = nx.Graph()
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("WITH RECURSIVE juniors AS (SELECT e_id, m_id, name, value_in_company FROM "+
                        "employees UNION SELECT e.e_id, e.m_id, e.name, e.value_in_company "+
                        "FROM employees e INNER JOIN juniors s ON s.e_id = e.m_id ) "+
                        "SELECT * FROM juniors;")

            row = cur.fetchone()
            while row is not None:
                G.add_edge(row['e_id'],row['m_id'], value=row["value_in_company"])
                row = cur.fetchone()
 
            return nx.dijkstra_path(G ,node1, node2, "value")
            
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

api.add_resource(Juniors, '/junior/<eid>')
api.add_resource(Senior_Tree, '/seniortree/<eid>')
#api.add_resource(Insert_Json, '/employees/<eid>')
api.add_resource(Shortest_Path,'/shortestpath/<int:node1>/<int:node2>')

if __name__ == '__main__':
     app.run(port='5002')
     
    #js= '{ "customer": "Lily Bush", "items": {"product": "Diaper","qty": 24}}'
    #print(get_juniors(3))
    #print(get_senior_tree(11))
    #print(get_path(1, 20))
    #get_late_joining(4)
    #insert_eid_json(1, js)