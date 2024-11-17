from flask import Flask, render_template, jsonify, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy 
from models import *
from testing_db import *

app = Flask(__name__)
app.secret_key = 'Asdasd@E!d121'
user = 'root'
password = 'koloveydo8'
host = 'localhost'
port = '3306'
database = 'taxcrm'


app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/components')
def components_view():
    return render_template('pages/components.html')

@app.route('/base')
def base_view():
    return render_template('pages/base.html')

@app.route('/create-user')
def create_user_view():

    return render_template('pages/components.html')

@app.route('/users')
def users_view():
    users = User_details.query.all()
    return render_template('pages/database_testing.html', users=users)

@app.route('/')
def indexView():

    callendar_data = [
        {'name':'','photo':''},
        {'name2':'','photo2':''},
    ]
    user = [
        {'id' : '1','name' :'Vlad', 'surname' : 'Koloveydo', 'work' : 'Developer', 'company' : 'none'},
    ]
    tasks = [
        {'id' : '1','name' :'Vadim Romaniyk'},
        {'id' : '2','name' :'Vadim Romaniyk'},
        {'id' : '3','name' :'Vadim Romaniyk'},
    ]
    unmess = [
        {'id' : '1','name' :'Vadim Romaniyk', 'sender' : 'Koloveydo'},
        {'id' : '2','name' :'Vadim Romaniyk', 'sender' : 'Koloveydo'},
        {'id' : '3','name' :'Vadim Romaniyk', 'sender' : 'Koloveydo'},
        {'id' : '4','name' :'Vadim Romaniyk', 'sender' : 'Koloveydo'},
    ]
    leads = [
        {'id' : '1','name' :'Vadim Romaniyk', 'time' : '16.11.2024'},
        {'id' : '2','name' :'Vadim Romaniyk', 'time' : '16.11.2024'},
        {'id' : '3','name' :'Vadim Romaniyk', 'time' : '16.11.2024'},
        {'id' : '4','name' :'Vadim Romaniyk', 'time' : '16.11.2024'},
    ]
    
    data = {
        "callendar_data": callendar_data,
        "user": user,
        "tasks": tasks,
        "unmess": unmess,
        "leads": leads,
    }
    
    
    return render_template('pages/index.html', data=data)

if __name__ == "__main__":
    with  app.app_context():
        db.create_all()

    insertToAllTables()

    app.run(debug=True, port=8088, host='0.0.0.0')
