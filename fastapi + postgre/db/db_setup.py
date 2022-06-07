import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn = psycopg2.connect(host='localhost', database='history', user='postgres', password='nihalnhk', cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print('Database Connection was Successful')
except:
    print("Connection Error")

def closedb():
    conn.close()