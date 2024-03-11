source .venv/bin/activate

pip install -r requirements.txt

npm install

npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch

flask run --debug
