from flask import Flask, jsonify, render_template, request
import sqlite3
import json
import mich

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("search.html")

# @app.route("/check=<name>")
# def check(name):
#     print(name)
#     return json.dumps({'b':name})

@app.route("/search")
def search():
    return render_template()


# for post:
# data = request.args
# name = (data["name"],)

@app.route("/check=<name>")
def check(name):
    conn = sqlite3.connect('medicine_db.db')
    c = conn.cursor()
    name = mich.my_trans(name)
    c.execute('''select distinct med_name from meds_data''')
    all_meds = []
    for med in c.fetchall():
        all_meds.append(med[0])
    name = mich.best_word(all_meds, name)
    name = (name,)
    c.execute('''select meds.uid, meds.med_name, meds.amount, meds.city,
                  meds.expiration_data, meds.is_closed, meds_data.picture
                  from meds
                  inner join meds_data on meds.med_name = meds_data.med_name
                  where meds.med_name = ? collate nocase''', name)
    json_return = json.dumps(c.fetchall())
    conn.close()

    return jsonify(json_return)

@app.route("/add", methods=['POST'])
def add():
    data = request.args
    uid = int(data["uid"])
    med_name = data["med_name"]



if __name__ == "__main__":
    app.run()