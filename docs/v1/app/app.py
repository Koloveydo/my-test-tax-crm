from flask import Flask, render_template, jsonify, redirect, flash, session
from models import *
from testing_db import *

app = Flask(__name__)
app.secret_key = 'Asdasd@E!d121'

user = 'root'
password = '0000'
host = 'localhost'
port = '3306'
database = 'tax_crm'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

db.init_app(app)


@app.route('/components')
def componentsView():
    return render_template('pages/components.html')

@app.route('/', methods=['GET', 'POST'])
def settings_view():
    user = {
        'image': '',
        'name': 'John', 
        'surname': 'Doe',
        'organization': 'Company A',
        'email': 'john@example.com',
        'phone': '123-456-7890',
        'cur_password': '243514',
        'personal_number': '65341367814355081',
        'skills': ['JavaScript', 'HTML', 'CSS', 'Flask', 'Java']
    }
    
    full_name = user['name'] + ' ' + user['surname']
    
    data = {
        'user': user,
        'full_name': full_name
    }

    return render_template('pages/settings.html', data=data)

@app.route('/login')
def login_view():
    return render_template('pages/login.html')

@app.route('/contacts')
def contacts_view():
    contacts = [
        {'photo': '','name': 'John','surname': 'Doe','organization': 'Company A','email': 'john@example.com','phone': '123-456-7890','skills': ['JavaScript', 'HTML', 'CSS', 'Flask', 'Java']},
        {'photo': '','name': 'John','surname': 'Doe','organization': 'Company A','email': 'john@example.com','phone': '123-456-7890','skills': ['JavaScript', 'HTML', 'CSS', 'Flask',]},
        {'photo': '','name': 'John','surname': 'Doe','organization': 'Company A','email': 'john@example.com','phone': '123-456-7890','skills': ['JavaScript', 'HTML', 'CSS',]},
        {'photo': '','name': 'John','surname': 'Doe','organization': 'Company A','email': 'john@example.com','phone': '123-456-7890','skills': ['JavaScript', 'HTML',]},
        {'photo': '','name': 'John','surname': 'Doe','organization': 'Company A','email': 'john@example.com','phone': '123-456-7890','skills': ['JavaScript',]},
    ]
    leads = [
        {'photo': '','name': 'John','surname': 'Doe','organization': 'Company A','email': 'john@example.com','phone': '123-456-7890','skills': ['JavaScript', 'HTML', 'CSS',]},
        {'photo': '','name': 'John','surname': 'Doe','organization': 'Company A','email': 'john@example.com','phone': '123-456-7890','skills': ['JavaScript', 'HTML', 'CSS',]},
        {'photo': '','name': 'John','surname': 'Doe','organization': 'Company A','email': 'john@example.com','phone': '123-456-7890','skills': ['JavaScript', 'HTML', 'CSS',]},
    ]
    
    all_contacts = contacts + leads
    
    data = {
        "contacts":     contacts,
        "leads":        leads,
        "all_contacts": all_contacts,
    }
    
    return render_template('pages/contacts.html', data=data)
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    insertToAllTables()

    app.run(debug=True, port=8080, host='0.0.0.0')