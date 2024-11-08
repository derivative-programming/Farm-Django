# Python 3.11 Django 4.2 API

## Intro

This repo is holding an example of a djnago application. This source code is used to create templates for the source code generator used by  https://github.com/derivative-programming/ModelWinApp and https://secure.derivative-programming.com

Addiition of features to this repo adds features to source code generated by the deriviative-programming domains services.

##Features
Django Admin
Django Debug Toolbar

Model...
- Test Classes
- Test Factories
- Audit Columns
- Admin Panel Updates
- DB change detection on save
- additional Code unique UUID field. (UUID Preferred in URLS instead of numberic values)





##Tech Used
Python 3.11
Django 4.2
djangorestframework 3.14
factory-boy 3.2
faker 18.7




##notes

Install python

Update pip...
>python.exe -m pip install --upgrade pip

Install python

>cd farm_project

create a virtual env...
python -m venv env

start virtual env...
env\scripts\activate

pip install django

Install requirements...
>pip install -r requirements.txt

make migration after model updates...
python manage.py makemigrations [namespace]

Create\update DB with migrations...
>python manage.py migrate

view sql applied by a migration...replace 0001 with migration name
>python manage.py sqlmigrate [namespace] 0001


create django admin user...
python manage.py createsuperuser

clear database of all records. keep tables.
>python manage.py flush

initialize db with core objects...
>python manage.py loaddata initialize-db.json

generate seed data...
python manage.py seed [namespace] --number=10

tests...
python manage.py test

run server....
>cd farm_project
>python manage.py runserver

collect requirements...
>pip freeze > requirements.txt

clean py cache...
>python manage.py clean_pyc


django toolbar is installed

# Getting Started
Before you can contribute, you'll need to set up a local copy of the repository:

* Fork the repository by clicking on the "Fork" button in the top right corner of the repository page.
* Clone the forked repository to your local machine: git clone https://github.com/YOUR_USERNAME/Farm-Django.git
* Navigate to the repository directory: cd Farm-Django
* Now you're ready to make changes to the code!

# Making Changes
* Create a new branch for your changes: git checkout -b my-new-branch
* Make your changes to the code.
* Commit your changes: git commit -am "Added some new feature"
* Push your changes to your fork: git push origin my-new-branch

# Creating a Pull Request
* Go to your forked repository on GitHub and click the "New pull request" button.
* Select the branch you just pushed your changes to.
* Give your pull request a meaningful title and description.
* Submit the pull request and wait for a project maintainer to review your changes.

