import sqlite3

con = sqlite3.connect("autok.db")
print("Adatbázis létrehozva")

con.execute(
    "create table autok (id INTEGER PRIMARY KEY AUTOINCREMENT, gyarto TEXT NOT NULL, tipus TEXT UNIQUE NOT NULL,evjarat TEXT NOT NULL, szin TEXT NOT NULL, ajtok_szama TEXT NOT NULL)")

print("Adatbázis sikeresen létrehozva")

con.close()
