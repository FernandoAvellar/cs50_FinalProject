from flask import Flask, render_template, request, redirect
from flask_session import Session
from cs50 import SQL

# Configure lithurgical sessions in a catholic mass to sort sheet musics.
SESSOES_DA_MISSA = {
    1:  "Aclamação",
    2:  "Amém",
    3:  "Comunhão",
    4:  "Cordeiro",
    5:  "Entrada",
    6:  "Geral",
    7:  "Glória",
    8:  "Santo",
    9:  "Saída",
    10: "Perdão",
    11: "Paz",
    12: "Ofertório"
}

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database/database.db")

@app.route("/")
@app.route("/index")
def index():
	return render_template("layout.html")

@app.route("/list")
def list():
	sheets = db.execute("SELECT * FROM cifras")
	return render_template("list.html", sheets=sheets)

@app.route("/insert", methods=["GET", "POST"])
def insert():
    if request.method == "POST":
        nome = request.form.get("name")
        sessao = request.form.get("session")
        cifra = request.form.get("music_sheet")

        db.execute("INSERT INTO cifras (nome, sessao, cifra) VALUES(?, ?, ?)", nome, sessao, cifra)

        return redirect('/')
    else:
        return render_template("insert.html", sessions = SESSOES_DA_MISSA.values())

if __name__ == '__main__':
	app.run(debug=True)