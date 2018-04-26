from flask import Flask, jsonify, render_template
import sqlite3
import json

app = Flask(__name__)


@app.route("/search")
def search():
    return render_template()


@app.route("/query", methods=['POST'])
def query():
    conn = sqlite3.connect('medicine_db.db')
    c = conn.cursor()

    c.execute('select * from meds')


if __name__ == "__main__":
    app.run()