from flask import Flask, render_template, jsonify, redirect, flash, session, request, url_for
from models import *
from testing_db import *
import json
import mysql.connector
# pip install mysql
# pip install mysql-connector-python-rf
# pip install MySQL-connector-python

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
            
            
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
'''   create context processor, with all session data start  '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
from flask import session

@app.context_processor
def utility_processor():
    session_data = {
        "profile_info": {
            "url_image": session["user"]["url_image"] if "user" in session and "url_image" in session["user"] else "",
            "first_name": session["user"]["first_name"] if "user" in session and "first_name" in session["user"] else "",
            "last_name": session["user"]["last_name"] if "user" in session and "last_name" in session["user"] else "",
        },
        "login": "user" in session, 
    }
    return {"session": session_data}

            
            
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
'''   create context processor, with all session data end  '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

            
@app.route('/components')
def components_view():
    return render_template('pages/components.html')

@app.route('/base')
def base_view():
    return render_template('pages/base.html')

@app.route('/create-user')
def create_user_view():

    return render_template('pages/components.html')

@app.route('/setting', methods=['GET', 'POST'])
def settings_view():
    if "login" in session and session["login"]:
        user_session = session["user"]

        with app.app_context():
            user = User_details.query.filter_by(
                firstname=user_session["first_name"], 
                lastname=user_session["last_name"]
            ).first()
        
        if user:
            user_data = {
                'url_image': user.url_image,
                'name': user.firstname,
                'surname': user.lastname,
                'organization': user.job_title,
                'email': user.email,
                'phone': user.phone,
                'cur_password': user.password,
                'personal_number': 'EMPTY', 
                'full_name' : user.firstname + " " + user.lastname
            }

            data = {
                "user": user_data,
            }
            return render_template('pages/settings.html', data=data)
        
    return redirect(url_for('login_view'))


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
            data_phone    = data_dict["reg-phone"]
            
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
            
        except Exception as e:
            print("Error:", str(e))
            json_data = {'success': False, 'message': 'An error occurred: ' + str(e)}

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

@app.route('/')
def indexView():
    callendar_data = [
        {'name':'','photo':''},
        {'name2':'','photo2':''},
    ]
    user = [
        {'id' : '1','name' :'Vlad', 'surname' : 'Koloveydo', 'work' : 'Developer', 'company' : 'none', 'photo' : 'images/avatar.png', 'message' : 'Test letter for page', 'time' : '5d'},
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

@app.route('/info', methods=["GET", "POST"])
def my_profile_view():
    user = User_details.query.filter_by(firstname=session["user"]["first_name"], lastname=session["user"]["last_name"]).first()
    print(user.email)
    user_mydetails = {
        'id':user.id,
        'firstname':user.firstname,
        'lastname':user.lastname,
        'email':user.email,
        'job_title':user.job_title,
        'phone':user.phone,
        'addres':user.addres,
        'url_image':user.url_image,
        'datetime_update':user.datetime_update,
        'datetime_create':user.datetime_create,
    }
    skills = [
        {'id' : '1', 'title' : 'HTML'}
    ]

    admin =  [
        {'id' : '1', 'name' : 'Admin' , 'date' : '12.12.2024', 'message' : 'You completed full register on our platfotm, thanks!', 'photo' : ''}
    ]

    sender = [
        {'id' : '1', 'name' : 'Vadim', 'surname' : 'Romanyuk', 'date' : '30.11.2024', 'work' : 'Team-lead', 'phone' : '0676776767', 'email' : 'vadim@dot.com', 're' : 'Please sign/Tax Company', 'photo' : 'images/sender_picture.png', 'message' : 'Your adaptation is dogshit. Cthulhu is a fictional cosmic entity created by writer H. P. Lovecraft. It was introduced in his short story "The Call of Cthulhu",[2] published by the American pulp magazine Weird Tales in 1928. Considered a Great Old One within the pantheon of Lovecraftian cosmic entities, this creature has since been featured in numerous pop culture references. Lovecraft depicts it as a gigantic entity worshipped by cultists, in the shape of a green octopus, dragon, and a caricature of human form. It is the namesake of the Lovecraft-inspired Cthulhu Mythos.', 'description' : 'Changed logs'}
    ]

    data = {
        "user": user_mydetails,
        "sender": sender,
        "skills": skills,
        "admin" : admin,
    }

    return render_template('pages/my_profile.html', data=data)

@app.route('/logout')
def logout_view():
    session.clear()
    print("logout succesful")
    return redirect(url_for('login_view'))

@app.route('/leads', methods=["GET", "POST"])
def my_leads_view():
    lead = Lead_details.query.first()
    user = User_details.query.filter_by(firstname=session["user"]["first_name"], lastname=session["user"]["last_name"]).first()
    user_mydetails = {
        'id':user.id,
        'firstname':user.firstname,
        'lastname':user.lastname,
        'email':user.email,
        'job_title':user.job_title,
        'phone':user.phone,
        'addres':user.addres,
        'url_image':user.url_image,
        'datetime_update':user.datetime_update,
        'datetime_create':user.datetime_create,
    }
    lead_hisdetails = {
        'id':lead.id,
        'firstname':lead.firstname,
        'lastname':lead.lastname,
        'email':lead.email,
        'organization':lead.ORGANIZATION,
        'phone':lead.phone_number,
        'comments':lead.comments,
        'address':lead.addres,
        'url_image':lead.url_image,
        'datetime_update':lead.datetime_update,
        'datetime_create':lead.datetime_create,
    }

    data = {
        "lead" : lead_hisdetails,
        "user" : user_mydetails,
    }

    return render_template('pages/leads.html', data=data)

''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
'''   check DB is exist or create and insert DB start   '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''


def checkDBExist():
    # Create a connection to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        auth_plugin='mysql_native_password'
    )

    # Create a cursor object to execute SQL statements
    mycursor = conn.cursor()

    mycursor.execute("SHOW DATABASES")
    names_db = mycursor.fetchall()

    database_exists = False
    for name_db in names_db:
        if database in name_db:
            database_exists = True
            break
    
    conn.close()
    return database_exists

def createDefaultDB():
    # Create a connection to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        auth_plugin='mysql_native_password'
    )

    # Create a cursor object to execute SQL statements
    mycursor = conn.cursor()

    mycursor.execute("CREATE DATABASE tax_crm")
    names_db = mycursor.fetchall()
    conn.close()


def is_database_empty():
    tables_to_check = [User_details, Lead_details]
    for table in tables_to_check:
        if not db.session.query(table).first():
            return True
    return False

def check_or_create_DB():
    if not checkDBExist():
        createDefaultDB()
        db.create_all()
        
    if is_database_empty():
        print("FILLING DATABASE")
        insertToAllTables()
    else:
        print("DATABASE ALREADY FILLED")



''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
'''   check DB is exist or create and insert DB end   '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''



if __name__ == "__main__":
    with app.app_context():
       check_or_create_DB()
        

    app.run(debug=True, port=8080, host='0.0.0.0')

