from flask import Flask, render_template, jsonify, redirect, flash, session, request
from flask_sqlalchemy import SQLAlchemy 
from models import *
from testing_db import *

app = Flask(__name__)
app.secret_key = 'Asdasd@E!d12'
user = 'root'
password = '0000'
host = 'localhost'
port = '3306'
database = 'tax_crm'


app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.context_processor
def context_all_page():
    if "login" in session:
        if session["login"] == True:
            pass

        else:
            session["login"] = True 
            session["profile_info"] = {
                "first_name": "Влад",
                "last_name":  "Коловейдо",
                "url_image":  "none",
            } 
            session["lich"] = 0
    else:
        session["login"] = False
        
    return { "session": session }

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


@app.route('/logout')
def logoutView():
    if "login" in session:
        if session["login"] == True:
            session["login"] = False
            del session["profile_info"]
            del session["lich"]
            
 
@app.route('/')
def indexView():
    callendar_data = [
        {'name':'','photo':''},
        {'name2':'','photo2':''},
    ]
    user = [
        {'id' : '1','name' :'Vlad', 'surname' : 'Koloveydo', 'work' : 'Developer', 'company' : 'none', 'photo' : 'images/avatar.png'},
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

@app.route('/my_profile')
def my_profile_view():

    user = [
        {'id' : '1','name' :'Vlad', 'surname' : 'Koloveydo', 'work' : 'Developer', 'bdate' : '08.11.2002', 'company' : 'none',  'address' : 'Lviv', 'email' : 'koloveydo8qazqsxedc@gmail.com', 'photo' : 'images/avatar.png'},
    ]

    sender = [
        {'id' : '1', 'name' : 'Vadim', 'surname' : 'Romanyuk', 'date' : '30.11.2024', 'phone' : '0676776767', 'email' : 'vadim@dot.com', 're' : 'Please sign/Tax Company', 'photo' : 'images/sender_picture.png', 'message' : 'Your adaptation is dogshit. Cthulhu is a fictional cosmic entity created by writer H. P. Lovecraft. It was introduced in his short story "The Call of Cthulhu",[2] published by the American pulp magazine Weird Tales in 1928. Considered a Great Old One within the pantheon of Lovecraftian cosmic entities, this creature has since been featured in numerous pop culture references. Lovecraft depicts it as a gigantic entity worshipped by cultists, in the shape of a green octopus, dragon, and a caricature of human form. It is the namesake of the Lovecraft-inspired Cthulhu Mythos.'}
    ]

    data = {
        "user": user,
        "sender": sender,
    }




    return render_template('pages/my_profile.html', data=data)

if __name__ == "__main__":
    with  app.app_context():
        db.create_all()

    insertToAllTables()

    app.run(debug=True, port=8088, host='0.0.0.0')
