from flask import Flask, render_template, jsonify, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy 
from models import db, User, UserDetails, Lead, LeadDetails, Activity, ActivityDetails, Communication, CommunicationDetails, Skill, SkillDetails, Tag, TagDetails

app = Flask(__name__)
app.secret_key = 'Asdasd@E!d121'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0000@localhost:3306/tax_crm'
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

@app.route('/create-user')
def create_user_view():
    ### create all for user model and user model
    ### print some informations of user
    
    ### create all for Lead model and Lead model
    ### print some informations of Lead
    
    ### ...
    ### ...
    
    
    return render_template('pages/components.html')


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')  