from flask import Flask, render_template, jsonify, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy 
from models import *

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

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/components')
def components_view():
    return render_template('pages/components.html')

@app.route('/base')
def base_view():
    return render_template('pages/base.html')

# test information for db
@app.route('/create-user')
def create_user_view():

    return render_template('pages/components.html')


# @app.route('/plus_button')
# def plus_button_view():
#     return render_template('components/plus_button.html')

if __name__ == "__main__":
    app.run(debug=True, port=8088, host='0.0.0.0')