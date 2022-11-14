from flask import *
import json
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/view")
def view():
    con = sqlite3.connect("autok.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from autok")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/savedetails/", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        data = request.get_json(force=True)
        print(data)
        gyarto = data["gyarto"]
        tipus = data["tipus"]
        evjarat = data["evjarat"]
        szin = data["szin"]
        ajtok_szama = data["ajtok_szama"]
        with sqlite3.connect("autok.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into autok (gyarto, tipus, evjarat, szin, ajtok_szama) values (?,?,?,?,?)", (gyarto, tipus, evjarat, szin, ajtok_szama))
            con.commit()
            msg = "Autó hozzáadva"
    except:
        con.rollback()
        msg = "Nem tudjuk hozzáadni az autót a listához"
    finally:
        return gyarto
        con.close()

@app.route("/deleterecord/", methods=["POST"])
def deleterecord():
    data = request.get_json(force=True)
    id = str(data["id"])
    print(id)
    with sqlite3.connect("autok.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from autok where id = ?", id)
            msg = "Sikeres törlés"
        except:
            msg = "Nem lehet törölni"

@app.route("/updatedetails/", methods=["POST"])
def updaterecord():
    try:
        data = request.get_json(force=True)
        print(data)
        id = data["id"]
        gyarto = data["gyarto"]
        tipus = data["tipus"]
        evjarat = data["evjarat"]
        szin = data["szin"]
        ajtok_szama = data["ajtok_szama"]

        with sqlite3.connect("autok.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE Autok SET gyarto=?, tipus=?, evjarat=?, szin=?, ajtok_szama=? WHERE id=?", (gyarto, tipus, evjarat,szin, ajtok_szama, id))
            con.commit()
            msg = "Az autót sikeresen hozzáadtad az adatbázishoz"
    except:
        con.rollback()
        msg = "Nem lehet frissiteni az autót a listában"
    finally:
        return msg
        con.close()

if __name__ == "__main__":
    app.run(debug=True)
