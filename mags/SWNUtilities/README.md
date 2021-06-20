# SWN Utilities

This is a django application - to start:

1. Set up a virtual environment, activate and install requirements
 - Get virtualenv: `pip install virtualenv` (if not already installed)
 - Create a virtual environment for this project: `virtualenv venv`
 - start the virtual environment Bash:`source venv/bin/activate` or Win:`venv/Scripts/activate` 
 - Install requirments `pip install -r requirements.txt`

2. Create a new secret key in an environment file
 - from this folder, run `python setup.py`

3. Run initial migrations and instantiate your db: `python manage.py makemigrations` `python manage.py migrate`

4. Make sure tests are passing: `python manage.py test -v2` (2 is level of verbosity 2, which will identify tests)

5. Start the server: `python manage.py runserver`

 