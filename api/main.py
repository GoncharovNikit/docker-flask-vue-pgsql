import psycopg2, os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api_test')
def api_test():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD')
    )

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users;")

        users = cur.fetchall()
        cur.close()
        conn.close()

    return jsonify(users)
