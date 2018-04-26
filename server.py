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
    c.execute('''select meds.uid, meds.med_name, meds.amount, meds.city,
                  meds.expiration_data, meds.is_closed, meds_data.picture
                  from meds
                  inner join meds_data on meds.med_name = meds_data.med_name
                  where meds.med_name = ? collate nocase''', name)
    json_return = json.dumps(c.fetchall())
    conn.close()

    return json_return

@app.route("/add", methods=['POST'])
def add():
    data = request.args
    uid = int(data["uid"])

if __name__ == "__main__":
    app.run()