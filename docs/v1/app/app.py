from flask import Flask, render_template, jsonify, redirect, flash, session, request
from models import *
from testing_db import *
import json

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
        'image': 'https://taxcanada.accountants/static/images/base/full_logo.png',
        'name': 'John', 
        'surname': 'Doe',
        'organization': 'Company A',
        'email': 'john@example.com',
        'phone': '123-456-7890',
        'cur_password': '243514',
        'personal_number': '65341367814355081',
        'skills': ['JavaScript', 'HTML', 'CSS', 'Flask', 'Java'],
    }
    
    full_name = user['name'] + ' ' + user['surname']
    
    data = {
        'user': user,
        'full_name': full_name
    }

    return render_template('pages/settings.html', data=data)

@app.route('/login')
def login_view():
    new_user = {
        'name': 'Blob', 
        'surname': 'Kpo',
        'organization': 'Company B',
        'email': 'blob@example.com',
        'phone': '923483-34-22',
    }
    
    data = new_user
    return render_template('pages/login.html', data=data)


@app.route('/check-data-register', methods=["GET", "POST"])
def checkRegisterView():
    if request.method == "POST":
        try:
            data = request.data
            data_dict = json.loads(data)
            
            data_email    = data_dict["reg-email"]
            data_password = data_dict["reg-pass"]
            data_name     = data_dict["reg-name"]
            data_surname  = data_dict["reg-surname"]
            data_job      = data_dict["reg-job"]
            data_address  = data_dict["reg-address"]
            data_phone    = "000000"
            
            # перевірка чи email вже був зареєстрований
            with app.app_context():
                users_db = User_details.query.all()
                
                if any(user.email == data_email for user in users_db):
                    json_data = {'success': False, 'message': 'Email already exists'}
                    return jsonify(json_data), 400

                else:

                    new_user_details = User_details(
                        firstname   = data_name,
                        lastname    = data_surname,
                        email       = data_email,
                        job_title   = data_job,
                        phone       = data_phone,
                        addres      = data_address,
                        url_image   = "",
                        password    = data_password,
                    )
                    db.session.add(new_user_details)
                    db.session.commit()
                    
                    session["login"] = True
                    session["user"] = {
                        "first_name": data_name,
                        "last_name":  data_surname,
                        "url_image":  "",
                    }
                    
                    json_data = {'success': True, 'message': 'Working, all exist, all good', "url_to_redirect": "/"}
                    return jsonify(json_data), 200
            
        except:
            json_data = {'success': False, 'message': 'POST method not valid'}

            return jsonify(json_data), 500
    else:
        json_data = {'success': False, 'message': 'method not allowed'}
        return jsonify(json_data), 405
   



@app.route('/check-data-login', methods=["GET", "POST"])
def checkLoginView():
    if request.method == "POST":
        try:
            data = request.data
            data_dict = json.loads(data)
            
            data_email = data_dict.get("log-email")
            data_password = data_dict.get("log-pass")
            
            with app.app_context():
                users_db = User_details.query.all()
                
                user = next((user for user in users_db if user['email'] == data_email), None)
            
                if not user:
                    return jsonify({'success': False, 'message': 'Email not found'}), 404
                
                if user['password'] == data_password:
                    session["login"] = True
                    return jsonify({'success': True, 'message': 'Login successful'}), 200
                else:
                    return jsonify({'success': False, 'message': 'Invalid password'}), 401
            
        except Exception as e:
            print(f"Error: {e}") 
            return jsonify({'success': False, 'message': 'POST method not valid'}), 500
    else:
        return jsonify({'success': False, 'message': 'Method not allowed'}), 405





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