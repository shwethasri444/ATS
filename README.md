# ATS
Installation:

python 3.6.2
django 2.0.6
MySQL 8.0 command line client

to install a specific version:

>pip install XX==1.0.3

to ignore previous versions and reinstall:

>pip install _Iv XX==1.0.3

to check version in cmd:

>python

>import XX as YY

>YY.__version__

to download MySQL client:
https://dev.mysql.com/downloads/mysql/

To run the project:

Create and activate a virtualenv:

>virtualenv lol

>cd lol

>Scripts\activate 

Clone the repository on your local environment 

git clone https://github.com/shwethasri444/ATS.git 

Navigate to the folder 

>cd ATS

>cd ats

Install the required dependencies 

>pip install -r requirements.txt

open MySQL command line client

>CREATE DATABASE cityhunter

in cmd,

>python manage.py makemigrations

sync the database:

>python manage.py migrate

Run the localhost-server :

>python manage.py runserver


The web-app will be available at 127.0.0.1:8000 on your browser.(use google only)
