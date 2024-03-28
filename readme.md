
> # Catholic Sheet Music Organizer
>
>> ## CS50 Final Project 


**Video Demo**: [Video demo](https://youtube.com)
**Name**: Fernando Octávio de Avellar Júnior (<favellar@yahoo.com.br>)
**Github username**: [FernandoAvellar](https://github.com/FernandoAvellar)
**edX username**: FernandoAvellar
**City**: Santa Rita do Sapucaí
**Country**: Brazil
**Record date**: 28 March 2024.


#### Description:

This project was created with the intention of helping people responsible for the music ministry in Catholic churches.
This ministry has the responsibility of preparing and performing the songs during the holy mass.

As a participant in this ministry, I felt like I was spending a lot of my time each week preparing the musical repertoire that would be performed during that week's Mass.
This repertoire changes every week, as it needs to follow the rites of the liturgy and in this rite there are rules that always instruct us to adapt the songs to the biblical readings that will be proclaimed at that mass.

As I needed to create a final project for the CS50 course, I dedicated myself to solving the problem explained above.

The project allows us to catalog all the songs we have already performed and also indicate in which session of the Catholic Holy Mass that song is suitable to be performed.
With the musical scores registered, the project allows us to generate the final repertoire of the week simply by indicating in a comma separet fromat the id of the songs we want to play at a given mass.

After the repertoire is generated, it is much easier to copy it to a text editor, make final edits and visual improvements and generate a PDF that can be sent to all musicians than to make all the process mannualy like it was done before this tool.
The program also allows us to delete sheet music that we no longer want it in our database and also allows us to edit them in order to correct any errors that may have occurred at the time of insertion.

To ensure that multiple people can use the program, it has a login session and privileges, that is, only the administrator of the music ministry of a given church will have permission to access the **insert**, **edit** and **delete** menu.

Other users will be allowed to view the all the sheet music, including a very useful functionality that is to quickly view the content of a song just by clicking on its name in the **list** or **list by session** menu.

And of course, the **common user** will be able to generate their own repertoire, avoiding a lot of time spent on preparation that would previously have to be done manually.

**The choosen technologies details**

- **Python**: A high-level language that allows us to do incredible things with fewer lines of code, it also has an incredible community around the world, which makes it much easier to get help to overcome challenges.

- **Flask**: A lightweight web application framework that runs Python.

- **HTML**: The responsible for construct the program that will be showed in browsers.

- **JavaScript**: Language necessary to make the page have dynamic behaviors, such as: the day and night button, loading the sheet music in the generate menu and displaying the sheet music in the list menu.

- **TailwindCSS**: The framework  responsible for styling our entire application. I decided on it, because I aspire to continue developing in frontend and this technology is closely associated today with REACT and NativeJS, which are respectively a library and a framework widely used in WEB development today. Tailwindcss helped me a lot by not having to leave the HTML code to style it. It made application development more agile and efficient by keeping HTML and CSS tied together.

 - **Flowbite**: In order not to reinvent the wheel, I chose Flowbite as it is a set of open source components built using tailwindcss and which allowed me to create parts of my application by reusing already developed code. Example: Header and Footer were created using this library.

- **SQLITE3**: To store the sheet music, I opted for this minimalist database that perfectly met the needs of the project.

- <https://www.pythonanywhere.com/>: Online environment that I chose to deploy the application and give access to other members of the music ministry here at the church in my city.

**How to setup the project in your local development environment**

1. Your machine must have **Python3** and **Node** previously installed.

2. Clone the code on github to your computer:
    > git-clone git@github.com:FernandoAvellar/cs50_FinalProject.git

3. Run the commands below that are responsible for create a virtual environment, activate it and install the project dependencies:

    >cd cs50_FinalProject
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    npm install

4. Compile the styles, run the project and open your browser to see the final result:

    >npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
    flask run
    Open your browser at: http://127.0.0.1:5000

5. Predefined Users:

    >User: admin / Password: admin - Administrator user with full permissions on the application.
     User: user / Password: user - Common user with permission to view the sheet music and generate the final repertoire.

**Database definition:**

The project already has the database built and populated, however, if it is necessary to define the database from scratch, follow the commands below so that this can be executed:

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

**Research sources and useful tools used to complete the project:**

- [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/)
- [https://tailwindcss.com/](https://tailwindcss.com/)
- [https://flowbite.com/](https://flowbite.com/)
- [https://flask.palletsprojects.com/en/latest](https://flask.palletsprojects.com/en/latest)
- [https://chat.openai.com/](https://chat.openai.com/)
- [https://www.sqlite.org/](https://www.sqlite.org/)
- [https://github.com/](https://github.com/)
- [https://stackoverflow.com/](https://stackoverflow.com/)
