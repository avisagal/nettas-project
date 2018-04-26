from flask import Flask, jsonify, render_template, request
import sqlite3
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("search.html")

@app.route("/check=<name>")
def check(name):
    return json.dumps({name:'b'})

@app.route("/search")
def search():
    return render_template()


# for post:
# data = request.args
# name = (data["name"],)

@app.route("/query/<name>")
def query(name):
    conn = sqlite3.connect('medicine_db.db')
    c = conn.cursor()
    name = (name,)
    c.execute('select * from meds where med_name = ? collate nocase', name)
    json_return = json.dumps(c.fetchall())
    conn.close()

    return json_return


if __name__ == "__main__":
    app.run()