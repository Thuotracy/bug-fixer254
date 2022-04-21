## Bug-fixer254

## Author
 Tracy Wangari

# Neighbourhood  Description
 This is an app that enables users to report bugs or issues that they find on differents app and the developers of the apps are able to see the complains and once they fix the problem they are able to share the progress they have made.

## Set Up and Installations

### Prerequisites
    - Python3.8.10
    - Postgres
    - python virtual environment (virtual:venv).
    - Visual Studio Code Editor.

### Clone the  project Repo
Run the following command on the terminal:
 https://github.com/Thuotracy/bug-fixer254.git

* cd Neighbourhood254

###  Install and activate virtual environment
Activate virtual environment using python3.8 
1. Install
* python3 -m venv newenv
2. Activate
source newenv/bin/activate

### Install dependancies
Install  all dependancies that will make the app run/function
* pip install -r requirements.txt

### Create the Database
* psql
* create database tracybugfixer;

### Make Migrations
* python3 manage.py makemigrations starproject(App name)
* python3 manage.py migrate

### Run the app
* python3 manage.py runserver
* open your browser with the local host; `127.0.0.1:8000` provided on the terminal

## Testing the application
* python3 manage.py test starproject

### Admin dashboard
`Username: tracy`
`Password: wangari`

### Technologies used
    - Python 
    - HTML
    - Django 
    - Bootstrap4
    - Heroku
    - GIT

### Live Link



### License

Bugfixer254 is under the ***[MIT](LICENSE)*** license.






