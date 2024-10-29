from flask import Flask, render_template, jsonify, redirect, flash, session
"""from models import *
'from testing_db import *"""

app = Flask(__name__)
"""app.secret_key = 'Asdasd@E!d121

user = 'root'
password = '0000'
host = 'localhost'
port = '3306'
database = 'tax_crm'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False"""

"""db.init_app(app)

@app.route('/')
@app.route('/components')
def componentsView():
    return render_template('pages/components.html')

@app.route('/base')
def baseView():
 " return render_template('pages/base.html')"""
    
@app.route('/')
def contacts_view():
    return render_template('pages/Contacts_page.html')

if __name__ == "__main__":
 app.run(debug=True, port=8080, host='0.0.0.0')