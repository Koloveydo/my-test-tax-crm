from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model): 
    __tablename__       = 'user'
    
    id                  = db.Column(db.Integer, primary_key=True)
    user_basic_details  = db.Column(db.Integer, db.ForeignKey('user_details.id'), nullable=False)
    datetime_update     = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create     = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)        
   
class User_details(db.Model):
    __tablename__   = 'user_details' 
    
    id              = db.Column(db.Integer, primary_key=True)
    firstname       = db.Column(db.String(40))
    lastname        = db.Column(db.String(40))
    email           = db.Column(db.String(40), unique=True)
    job_title       = db.Column(db.String(60))
    phone           = db.Column(db.String(14))
    addres          = db.Column(db.String(50))
    url_image       = db.Column(db.Text)
    
    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default= datetime.utcnow, nullable= False)
       
   
class Lead(db.Model):
    __tablename__   = 'lead'
    
    id              = db.Column(db.Integer, primary_key=True)
    firstname       = db.Column(db.String(40))
    lead_details    = db.Column(db.Integer, db.ForeignKey('lead_details.id'), nullable=False)
    
    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default= datetime.utcnow, nullable= False)


class Lead_details(db.Model):
    __tablename__   = 'lead_details'
    
    id              = db.Column(db.Integer, primary_key=True)
    firstname       = db.Column(db.String(40))
    lastname        = db.Column(db.String(40))
    ORGANIZATION    = db.Column(db.String(100))
    email           = db.Column(db.String(40), unique=True)
    phone_number    = db.Column(db.String(14), unique=True)
    addres          = db.Column(db.String(50))
    url_image       = db.Column(db.Text)
    comments        = db.Column(db.Text)
    
    datetime_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable= False)
  
        
    
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
    user            = db.Column(db.ForeignKey('user.id'), nullable=False)
    
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
    