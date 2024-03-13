from flask import Flask, render_template, request, redirect
from flask_session import Session
from cs50 import SQL

# Configure lithurgical sessions in a catholic mass to sort sheet musics.
SESSOES_DA_MISSA = {
    1:  "Aclamação",
    2:  "Amém",
    3:  "Comunhão",
    4:  "Cordeiro",
    5:  "Consagração",
    6:  "Entrada",
    7:  "Geral",
    8:  "Glória",
    9:  "Santo",
    10:  "Saída",
    11: "Perdão",
    12: "Paz",
    13: "Ofertório"
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



@app.route("/filtered_list", methods=["GET", "POST"])
def filtered_list():
    selected_filters = []
    if request.method == "POST":
        for section in SESSOES_DA_MISSA.values():
             if request.form.get(section):
                selected_filters.append(section) 
        print(selected_filters)
        return redirect('/filtered_list')
    else:
        sheets = db.execute("SELECT * FROM cifras")
        return render_template("filter.html", sheets=sheets, sessions = SESSOES_DA_MISSA.values())
    
# sheets = db.execute("SELECT * FROM cifras WHERE session = ?", filter_session)
   
            




@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        input_list = request.form.get("list")
        selected_sheet_music_list = input_list.split(',')
        print(selected_sheet_music_list)
    
        with open("cifras_selecionadas.txt", "w") as file:
            for selected in selected_sheet_music_list:
                selected = int(selected.strip())
                query = db.execute("SELECT * FROM cifras WHERE id = ?", selected)
                if len(query) != 0:
                    file.write(f"{query[0]['sessao']}\n\nMúsica: {query[0]['nome']}\n\n{query[0]['cifra']}\n\n")
                
        return redirect('/')
    else:
        return render_template("generate.html")




if __name__ == '__main__':
	app.run(debug=True)