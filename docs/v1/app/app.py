from flask import Flask, render_template, jsonify, redirect, flash, session, request, url_for
from models import *
from testing_db import *
import json

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




''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
'''   check login user before every request start   '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
            
@app.before_request
def before_request():
    if request.endpoint not in ['login_view', 'checkLoginView', 'checkRegisterView'] \
    and request.endpoint != 'login' \
    and '/static/' not in request.path:
        
        if "login" in session:
            if session["login"] != True:
                session["login"] = False
                return redirect(url_for('login_view'))
        else:
            session["login"] = False
            return redirect(url_for('login_view'))


''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
'''   check login user before every request end   '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
            
            
            
@app.route('/components')
def components_view():
    return render_template('pages/components.html')

@app.route('/base')
def base_view():
    return render_template('pages/base.html')

@app.route('/create-user')
def create_user_view():

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
        # "callendar_data": callendar_data,
        "user": user,
        # "tasks": tasks,
        # "unmess": unmess,
        # "leads": leads,
    }

    return render_template('pages/settings.html', data=data)

@app.route('/login')
def login_view():

    return render_template('pages/login.html')


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
                # user = next((user for user in users_db if user.email == data_email), None)
                user = User_details.query.filter_by(email=data_email).first()
                
                if not user:
                    json_data = {'success': False, 'message': 'Email not found'}
                    return jsonify(json_data), 404
                else:
                    if user.password == data_password:
                        session["login"] = True
                        session["user"] = {
                            "first_name": user.firstname,
                            "last_name":  user.lastname,
                            "url_image":  user.url_image,
                        }
                        json_data = {'success': True, 'message': 'Login success','url_to_redirect': '/'}
                        return jsonify(json_data), 200
                    else:
                        json_data = {'success': False, 'message': 'Invalid password'}
                        return jsonify(json_data), 401
            
        except Exception as e:
            print(f"Error: {e}") 
            json_data = {'success': False, 'message': 'POST method not valid'}
            return jsonify(json_data), 500
    else:
        json_data = {'success': False, 'message': 'Method not allowed'}
        return jsonify(json_data), 405





@app.route('/profile')
def my_profile_view(): 
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
        "user": user,
    }


    return render_template('pages/my_profile.html', data=data)

if __name__ == "__main__":
    with  app.app_context():
        db.create_all()

    insertToAllTables()
    

    app.run(debug=True, port=8080, host='0.0.0.0')
