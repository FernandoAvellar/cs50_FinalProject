from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from utilities import login_required


# Configure lithurgical sessions in a catholic mass to sort sheet musics.
SESSOES_DA_MISSA = {
    1:  "Aclamação",
    2:  "Amém",
    3:  "Ato penitencial",
    4:  "Comunhão",
    5:  "Cordeiro",
    6:  "Consagração",
    7:  "Entrada",
    8:  "Geral",
    9:  "Glória",
    10: "Santo",
    11: "Saída",
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
@login_required
def index():
    return render_template("layout.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not (username and password and confirm_password):
            flash('Please, fill all inputs!', 'error')
            return redirect('/register')

        if password != confirm_password:
            flash('Password does not match', 'error')
            return redirect('/register')

        # Insert new user into the database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                   username, generate_password_hash(password))
        return redirect("login")

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if not (username and password):
            flash('Please, fill username and password', 'error')
            return redirect('/login')

        # Query database for username
        user_query = db.execute(
            "SELECT * FROM users WHERE username = ?", username)

        if len(user_query) == 0:
            flash('Invalid user', 'error')
            return redirect("/login")

        elif not check_password_hash(user_query[0]["hash"], password):
            flash('Invalid password.', 'error')
            return redirect("/login")

        else:
            # Remember which user has logged in
            session["user_id"] = user_query[0]["id"]
            session["username"] = user_query[0]["username"]
            flash('Logged in successfully.', 'info')
            return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # Forget any user_id and redirect to login page
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect("/login")


@app.route("/list")
@login_required
def list():
    sheets = db.execute("SELECT * FROM cifras")
    return render_template("list.html", sheets=sheets)


@app.route("/insert", methods=["GET", "POST"])
@login_required
def insert():
    if request.method == "POST":
        nome = request.form.get("name")
        sessao = request.form.get("session")
        cifra = request.form.get("music_sheet")

        if not (nome and sessao and cifra):
            flash('Please, fill all inputs!', 'error')
            return redirect('/insert')

        db.execute(
            "INSERT INTO cifras (nome, sessao, cifra) VALUES(?, ?, ?)", nome, sessao, cifra)

        return redirect('/list')
    else:
        # allow /insert route only accesible to admin user.
        if session["username"] != 'admin':
            return redirect('/')

        return render_template("insert.html", sessions=SESSOES_DA_MISSA.values())


@app.route("/filtered_list", methods=["GET", "POST"])
@login_required
def filtered_list():
    selected_filters = []
    if request.method == "POST":
        # Get filters selected
        for section in SESSOES_DA_MISSA.values():
            if request.form.get(section):
                selected_filters.append(section)
        # If there is any selected filter, format message and query database
        if (selected_filters):
            ','.join(f"{elemento}" for elemento in selected_filters)
            '('.join(f"str_selec_filters)")
            sheets = db.execute(
                "SELECT * FROM cifras WHERE sessao in (?)", selected_filters)
        else:
            sheets = db.execute("SELECT * FROM cifras")

        return render_template("filter.html", sheets=sheets, sessions=SESSOES_DA_MISSA.values())
    else:
        sheets = db.execute("SELECT * FROM cifras")
        return render_template("filter.html", sheets=sheets, sessions=SESSOES_DA_MISSA.values())


@app.route("/generate", methods=["GET", "POST"])
@login_required
def generate():
    if request.method == "POST":
        input_list = request.form.get("list")
        selected_sheet_music_list = input_list.split(',')

        with open("static/cifras_selecionadas.txt", "w") as file:
            for selected in selected_sheet_music_list:
                selected = int(selected.strip())
                query = db.execute(
                    "SELECT * FROM cifras WHERE id = ?", selected)
                if len(query) != 0:
                    file.write(
                        f"{query[0]['sessao']}\n\nMúsica: {query[0]['nome']}\n\n{query[0]['cifra']}\n\n")
        flash('Repertorie generated successfully.', 'info')
        return redirect('/generate')
    else:
        return render_template("generate.html")


@app.route('/delete/<int:id>')
@login_required
def delete(id):
    db.execute("DELETE FROM cifras WHERE id = ?", id)
    flash('Sheet music deleted successfully', 'info')
    return render_template("list.html")


if __name__ == '__main__':
    app.run(debug=True)
