from flask import Flask, render_template, jsonify, redirect, flash, session
from models import *

app = Flask(__name__)
username='root'
password='0000'
host='localhost'
port='3306'
database='tax_crm'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
app.secret_key = 'Asdasd@E!d121'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

db.init_app(app)

@app.route('/')
@app.route('/components')
def components_view():
    return render_template('pages/components.html')

@app.route('/base')
def base_view():
    return render_template('pages/base.html')

@app.route('/users')
def users_view():
    users = UserDetails.query.all()
    return render_template('pages/database_testing.html', users=users)


'''@app.route('/create-lead')
def create_lead_view():
     leads = UserDetails.query.all()
     return render_template('pages/Checking_Database.html', leads=leads)'''

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')  