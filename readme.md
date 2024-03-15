source .venv/bin/activate

pip install -r requirements.txt

npm install

npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch

flask run --debug


Database Definition:

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    username TEXT NOT NULL, 
    hash TEXT NOT NULL
);

CREATE UNIQUE INDEX username ON users (username);

CREATE TABLE IF NOT EXISTS cifras (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    sessao TEXT NOT NULL,
    cifra TEXT NOT NULL
);
