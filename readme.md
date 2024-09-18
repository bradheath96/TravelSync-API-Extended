### Create the basic project directory

Initilize Git

```
git init
```

use the following to make a virtual environment:

```
python -m venv venv
```

Why do we need venv in python?

- Dependency Management: Keeps your project’s dependencies isolated from the system-wide Python installation.
- Environment Consistency: Ensures consistent behavior across different development environments.

if this doesnt work it likely means the installed python has been named python3 rather than python. This means we will also have pip3 rather than pip. To resolve this we will make a name alias for both:

```
echo "alias python=python3" >> ~/.zshrc
source ~/.zshrc
```

```
echo "alias pip=pip3" >> ~/.zshrc
source ~/.zshrc
```

now try again

once this is made, activate the venv using:

```
source venv/bin/activate
```

in the main project directory make a src folder that will house the main code:
make the first python file main.py

```
my_project/
├── src/
│   └── my_module/
│       ├── __init__.py
│       └── calculator.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── requirements.txt
├── setup.py
└── README.md
```

**_Install first dependancy fastAPI:_**

```
pip install fastapi uvicorn
```

to then run the server we can use from the root dir

```
fastapi dev src/app.py
```

but this isnt needed yet.

**\* Dependancy Management with requirements.txt \***

The requirements.txt file lists all the Python packages your project depends on. This ensures that anyone working on the project can install the exact versions of packages needed.

```
pip freeze > requirements.txt
```

This command captures all currently installed packages in your virtual environment and writes them to requirements.txt.

Therefore each time dependancies are installed during development it is important to run this code again to update the requirements.txt.

Others can install these dependencies by running:

```
pip install -r requirements.txt
```

**_.gitignore_**

- .gitignore: Specifies files and directories that Git should ignore, like venv/, **pycache**/, and other generated files.

Virtual environment directory (venv) (not typically included in version control).

For making API requests we will need the following dependancy

```
pip install requests
```

### Google Places API

find the docs here

```
https://developers.google.com/maps/documentation/places/web-service/search-nearby#maps_http_places_nearbysearch-txt
```

**_create google cloud console account_**

- create an account and add a billing option
- create a project and enable the placesAPI (new)
- go to the credentials page and create an API (restricted)
- add API to a .env file and add .env to the .gitignore

\*\*\*TEST-DRIVEN DEVELOPMENT

so i will be using pytest as it seems to be quite beginner friendly and is a widely adopted choice.
to run tests we need to use the command

```
pytest
```

\*\*\*Setting up the database

to create the database and then seed it

run this command from the root dir

```
python -m src.db.setup_and_seed
```
