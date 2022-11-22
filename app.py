from flask import Flask
import psycopg2
from flask import request
from datetime import datetime

app = Flask(__name__)
conn = psycopg2.connect(dbname='database', user='postgres', 
                        password='postgres', host='localhost')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS table_Counter (id serial PRIMARY KEY, updated_at timestamp default current_timestamp, client_info varchar);")


@app.route("/")
def hello():
    cur.execute("SELECT id from table_Counter ORDER BY id DESC LIMIT 1;")
    res = cur.fetchall()
    return {"id": res[0][0]}
    
@app.route("/stat")
def stat():
    header = request.headers.get('User-Agent')
    cur.execute(f"INSERT INTO table_Counter (client_info, updated_at) VALUES ('{header}', '{datetime.now()}');")
    return {'inserted': True}


@app.route("/about")
def about():
    return "<h3> Hello, Alexander Yurev </h3>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)