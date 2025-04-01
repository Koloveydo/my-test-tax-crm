from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Enum

db = SQLAlchemy()

class User(db.Model): 
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    user_basic_details = db.Column(db.Integer, db.ForeignKey('user_details.id'), nullable=False)
    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    details = db.relationship('User_details', back_populates='user', uselist=False)

    leads = db.relationship('Lead', back_populates='user')


class User_details(db.Model):
    __tablename__ = 'user_details'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    email = db.Column(db.String(40), unique=True)
    job_title = db.Column(db.String(60))
    phone = db.Column(db.String(14))
    addres = db.Column(db.String(50))
    url_image = db.Column(db.Text)
    password = db.Column(db.String(30))
    
    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship('User', back_populates='details', uselist=False)


class Lead(db.Model):
    __tablename__ = 'lead'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lead_details = db.Column(db.Integer, db.ForeignKey('lead_details.id'), nullable=False)
    
    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship('User', back_populates='leads')

    details = db.relationship('Lead_details', back_populates='lead', uselist=False)
   # client_projects = db.relationship('Clients_project', backref='lead_ref', lazy=True)


class Lead_details(db.Model):
    __tablename__ = 'lead_details'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    ORGANIZATION = db.Column(db.String(100))
    email = db.Column(db.String(40), unique=True)
    phone_number = db.Column(db.String(14), unique=True)
    addres = db.Column(db.String(50))
    url_image = db.Column(db.Text)
    comments = db.Column(db.Text)
    password = db.Column(db.String(30))

    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    lead = db.relationship('Lead', back_populates='details', uselist=False)
        
    
class Activity(db.Model): 
    __tablename__    = 'activity'  
    
    id               = db.Column(db.Integer, primary_key=True)
    lead             = db.Column(db.Integer, db.ForeignKey('lead_details.id'), nullable=False)
    activity_details = db.Column(db.Integer, db.ForeignKey('activity_details.id'), nullable=False)
   

class Activity_details(db.Model):
    __tablename__   = 'activity_details'
    
    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(40))
    activity_type   = db.Column(db.String(40))
    user            = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable= False)
 


class Communication(db.Model):
    __tablename__         = 'communication'
    
    id                    = db.Column(db.Integer, primary_key=True)
    lead                  = db.Column(db.ForeignKey('lead.id'), nullable=False)
    communication_details = db.Column(db.ForeignKey('communication_details.id'),)

    

class Communication_details(db.Model):
    __tablename__   = 'communication_details'
    
    id              = db.Column(db.Integer, primary_key=True)
    subject         = db.Column(db.String(60))
    text            = db.Column(db.Text)
    user            = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable= False)
   


class Skills(db.Model):
    __tablename__   = 'skills'
    
    id              = db.Column(db.Integer, primary_key=True)
    lead            = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    skills_details  = db.Column(db.Integer, db.ForeignKey('skills_details.id'))
        
class Skills_details(db.Model):
    __tablename__   = 'skills_details'
    
    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(60))
    
    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable= False)
  
class Tags(db.Model):
    __tablename__ = 'tags'
    
    id            = db.Column(db.Integer, primary_key=True)
    lead          = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    tags_details  = db.Column(db.Integer, db.ForeignKey('tags_details.id'), nullable=False)
   
class Tags_details(db.Model):
    __tablename__   = 'tags_details'
    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(60))
    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable= False)

#class Client_projects (db.Model):
#    __tablename__           = 'client_projects'
#    id                      = db.Column(db.Integer, primary_key=True)
#    lead                    = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
#    client_project_details  = db.Column(db.Integer, db.ForeignKey('clients_project_details.id'), nullable=False)
#    project_details = db.relationship('Clients_project_details', backref='project_ref', lazy=True)
#
#class Clients_project_details (db.Model) :
#    __tablename__           = 'client_projects_details'
#    id                      = db.Column(db.Integer, primary_key=True)
#    title                   = db.Column(db.String(60))
#    priority = db.Column(Enum('low', 'medium', 'high', name='priority_enum'), nullable=False)
#    status = db.Column(Enum('open', 'in_progress', 'closed', name='status_enum'), nullable=False)
#    datetime_update         = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
#    datetime_create         = db.Column(db.DateTime, default=datetime.utcnow, nullable= False)


