from flask import Flask
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='lentopeli',
         password='lentokone',
         autocommit=True
)


@app.route("/kentta/<icao>")
def kentta(icao: str):
    cursor = db.cursor()

    query = """SELECT ident, name, municipality FROM airport WHERE ident = %s"""

    cursor.execute(query, (icao.upper(),))

    result = cursor.fetchone()

    if not result:
        return {
            "message": f"No airport found with ICAO code {icao.upper()}."
        }

    return {
        "icao": result[0],
        "name": result[1],
        "municipality": result[2]
    }
