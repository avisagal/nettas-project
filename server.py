from flask import Flask, jsonify, render_template, request
import sqlite3
import json
import mich

SUB_MED_FOUND = "כותרת למצאנו תרופה"
BODY_MED_FOUND = "טקסט למצאנו תרופה"
HEADERS = ["id", "medicine name", "amount", "city", "expiration date", "is closed", "owner name", "picture"]


app = Flask(__name__)

def translate_to_dict(list_data):
    dict_id = 1
    outer_dict = {}
    for cur_tuple in list_data:
        inner_dict = {}
        for i in range(8):
            inner_dict[HEADERS[i]] = cur_tuple[i]
        outer_dict[dict_id] = inner_dict
        dict_id += 1

    return outer_dict


@app.route("/")
def index():
    return render_template("search.html")


@app.route("/check=<name>")
def check(name):
    name = mich.my_trans(name)
    name = mich.best_word(all_meds, name)
    name = (name,)
    c.execute('''select meds.uid, meds.med_name, meds.amount, meds.city,
                  meds.expiration_date, meds.is_closed, meds.owner_name, meds_data.picture
                  from meds
                  inner join meds_data on meds.med_name = meds_data.med_name
                  where meds.med_name = ? collate nocase''', name)
    dict_result = translate_to_dict(c.fetchall())
    json_return = json.dumps(dict_result)

    return json_return

@app.route("/add_waiting", methods= ["POST"])
def add_waiting():
    details = (request.args["mail"], request.args["name"], request["med"])
    c.execute("INSERT INTO waiting VALUES (?,?,?)", details)
    conn.commit()
    return


def send_mails_to_waiting_list(med_name):
    med_tuple = (med_name,)
    c.execute('''select mail, name
                      from waiting
                      where med_name = ? collate nocase''', med_tuple)
    data = c.fetchall()
    if data:
        for tup in data:
            mich.send_mail(tup[0], tup[1], SUB_MED_FOUND, BODY_MED_FOUND)

@app.route("/add", methods=['POST'])
def add():
    global uid
    data = request.args
    med_name = mich.best_word(all_meds, data["med_name"])
    if med_name is None:
        return jsonify(json.dumps({'state': 1}))
    details = (uid, med_name, data["date"], float(data["amount"]), data["is_closed"],
               data["city"], data["mail"], data["name"])
    uid += 1
    c.execute("INSERT INTO meds VALUES (?,?,?,?,?,?,?,?)", details)
    send_mails_to_waiting_list(med_name)
    conn.commit()
    return jsonify(json.dumps({'state': 0}))


if __name__ == "__main__":
    conn = sqlite3.connect('medicine_db.db')
    c = conn.cursor()
    c.execute('''select distinct med_name from meds_data''')
    all_meds = []
    for med in c.fetchall():
        all_meds.append(med[0])
    c.execute('''select max(uid) from meds''')
    uid = c.fetchone()[0] + 1
    app.run()
    conn.close()
