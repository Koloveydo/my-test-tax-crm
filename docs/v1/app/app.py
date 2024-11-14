from flask import Flask, render_template, jsonify, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy 
from models import *

app = Flask(__name__)
app.secret_key = 'Asdasd@E!d121'
user = 'root'
password = '0000'
host = 'localhost'
port = '3306'
database = 'tax_crm'


app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


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
        'Vadim Romaniyk',
        'Vadim Romaniyk',
        'Vadim Romaniyk',
        'Vadim Romaniyk',
    ]
    tasks = [
        'Vadim Romaniyk',
        'Vadim Romaniyk',
        'Vadim Romaniyk',
        'Vadim Romaniyk',
    ]
    unmess = [
        'Vadim Romaniyk',
        'Vadim Romaniyk',
        'Vadim Romaniyk',
        'Vadim Romaniyk',
    ]
    leads = [
        'Vadim Romaniyk',
        'Vadim Romaniyk',
        'Vadim Romaniyk',
        'Vadim Romaniyk',
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
    app.run(debug=True, port=8088, host='0.0.0.0')
