from flask import Flask, render_template, jsonify, redirect, flash, session
from models import *
from Checking_Database import *

app = Flask(__name__)
app.secret_key = 'Asdasd@E!d121'

username='root'
password='0000'
host='localhost'
port='3306'
database='tax_crm'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
user = 'root'

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
    user = User.query.all()
    lead = Lead.query.all()
    activity = Activity.query.all()
    communication = Communication.query.all()
    skils = Skill.query.all()
    tags = Tag.query.all()
    
    users_details = UserDetails.query.all()
    leads_details = LeadDetails.query.all()
    activities_details = ActivityDetails.query.all()
    skills_details = SkillDetails.query.all()
    tags_details = TagDetails.query.all()

    return render_template('pages/Checking_Database.html', 
                           user=user,
                           lead=lead,
                           activity=activity,
                           communication=communication,
                           skils=skils,
                           tags=tags,
                           
                           users_details=users_details, 
                           leads_details=leads_details, 
                           activities_details=activities_details, 
                           skills_details=skills_details, 
                           tags_details=tags_details)




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    insertToAllTables()

    app.run(debug=True, port=8080, host='0.0.0.0')
