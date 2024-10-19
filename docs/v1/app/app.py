from flask import Flask, render_template, jsonify, redirect, flash, session
from models import *

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

@app.route('/')
@app.route('/components')
def componentsView():
    return render_template('pages/components.html')


@app.route('/base')
def baseView():
    return render_template('pages/base.html')

@app.route('/users')
def users_view():
    user = User.query.all()
    lead = Lead.query.all()
    activity = Activity.query.all()
    communication = Communication.query.all()
    skils = Skills.query.all()
    tags = Tags.query.all()
    
    users_details = User_details.query.all()
    leads_details = Lead_details.query.all()
    activities_details = Activity_details.query.all()
    skills_details = Skills_details.query.all()
    tags_details = Tags_details.query.all()

    return render_template('pages/database_testing.html', 
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
    with  app.app_context():
        db.create_all()
    app.run(debug=True, port=8080, host='0.0.0.0')
    
    