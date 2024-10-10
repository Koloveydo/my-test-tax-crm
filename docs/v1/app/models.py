from flask import Flask, render_template, jsonify, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
db = SQLAlchemy()

class User(db.Model): 
    __tablename__ = 'user'

    id = db.Column("id",db.Integer, primary_key=True)
    user_basic_details = db.Column(db.Integer, db.ForeignKey('user_details.id'), nullable=False)
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  

    user_details = db.relationship('Userdetails', backref='user')
    def __repr__(self):
        return f"<User {self.id}, {self.user_basic_details} >"
   
class UserDetails(db.Model):
    __tablename__ = 'user_details' 

    id = db.Column("id",db.Integer, primary_key=True)
    first_name =db.Column(db.string(40))
    last_name =db.Column(db.string(40))
    email =db.Column(db.string(40), unique=True)
    job_title =db.Column(db.string(60))
    phone_number =db.Column(db.string(14))
    address =db.Column(db.string(50))
    url_image =db.Column(db.Text)
    datetime_update =db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create =db.Column(db.DateTime, default= datetime.utcnow, nullable= False)

    def __repr__(self):
     return f"<UserDetails {self.id}, {self.first_name} {self.last_name}, {self.email},  {self.phone_number}>"
   
class Leads(db.Model):
    __tablename__= 'lead'

    id = db.Column("id", db.Integer, primary_key=True)
    first_name= db.Column(db.string(40))
    lead_details= db.Column(db.Integer, db.ForeignKey('lead_details.id'), nullable=False)
    datetime_update =db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create =db.Column(db.DateTime, default= datetime.utcnow, nullable= False)
  
    LeadsDetails = db.relationship('Leads_Details', backref='lead', uselist=False)
    def __repr__(self):
       return f"<Leads {self.id}, {self.first_name}, {self.lead_details}>"

class LeadsDetails(db.Model):
    __tablename__= 'lead_details'

    id = db.mColumn("id", db.Integer, primary_key=True)
    first_name= db.Column(db.string(40))
    ORGANIZATION= db.Column(db.string(100))
    email =db.Column(db.string(40), unique=True)
    phone_number =db.Column(db.string(14))
    address =db.Column(db.string(50))
    url_image =db.Column(db.Text)
    comments= db.Column(db.Text)
    datetime_update =db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create =db.Column(db.DateTime, default= datetime.utcnow, nullable= False)
  
    def __repr__(self):
       return f"<lead_details {self.id}, {self.first_name}, {self.email}, {self.ORGANIZATION} {self.phone_number} {self.address}>"
    
class Activity(db.Model): 
    __tablename__= 'activity' 

    id = db.Column("id", db.Integer, primary_key=True)
    lead= db.Column(db.Integer, db.ForeignKey('lead_details.id'), nullable=False))
    lead = db.relationship('lead', backref='activity')

    activity_details= db.Column(db.integer, db.ForeignKey('activity_details.id'), nullable=False)
    activity_details = db.relationship('Activity_details', backref='activity', lazy=True)
   

    def __repr__(self):
       return f"<activity {self.id},{self.id},{self.activity_details}>"

class ActivityDetails(db.Model):
    __tablename__= 'activity_details'

    id = db.Column("id", db.Integer, primary_key=True)
    title= db.Column(db.string(40))
    activity_type= db.Column(db.string(40))
    user = db.Column(db.string, db.ForeignKey('user.id'), nullable=False)
    datetime_update =db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create =db.Column(db.DateTime, default= datetime.utcnow, nullable= False)
    
    user = db.relationship('User', backref='activity_details', lazy=True)

    def __repr__(self):
       return f"<activity_details {self.id},{self.title}, {self.activity_type} >"


class Communication(db.Model):
    __tablename__= 'communication'

    id= db.Column(db.Integer, primary_key=True)

    lead= db.Column(db.ForeignKey('lead.id'), nullable=False)
    lead = db.relationship('lead', backref='communication', lazy=True)
    
    communication_details= db.Column(db.ForeignKey('communication_details.id'), nullable=False)
    communication_details = db.relationship('communication_details', backref='communication', lazy=True)

    def __repr__(self):
       return f"<comuunicaton {self.id},{self.lead},{self. communication_details} >"


class CommunicationDetails(db.Model):
    __tablename__= 'communication_details'

    id = db.Column("id", db.Integer, primary_key=True)
    subject= db.Column(db.string(60))
    text= db.Column(db.text)
    user= db.Column(db.integer, db.ForeignKey('user.id'), nullable=False)
    datetime_update =db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create =db.Column(db.DateTime, default= datetime.utcnow, nullable= False)
   
    user = db.relationship('user', backref='CommunicationDetails', lazy=True)
    def __repr__(self):
       return f"<communication_details {self.id},{self.subject},{self.user}>"


class Skills(db.Model):
    __tablename__= 'skills'

    id = db.Column("id", db.Integer, primary_key=True)
    lead= db.Column(db.string, db.ForeignKey('lead.id'), nullable=False)
    lead = db.relationship('lead', backref='skill', lazy=True)

    skills_details= db.Column(db.Integer, db.ForeignKey('skills_details.id'), nullable=False)
    skills_details = db.relationship('skills_details', backref='skills', lazy=True)
    def __repr__(self):
       return f"<activity {self.id}{self.lead},{self.skills_details}>"

class SkillsDetails(db.Model):
    __tablename__= 'skills_details'

    id = db.Column("id", db.Integer, primary_key=True)
    title= db.Column(db.string)
    datetime_update =db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create =db.Column(db.DateTime, default= datetime.utcnow, nullable= False)
  
    def __repr__(self):
       return f"<activity {self.id},{self.title} >"
    

class Tags(db.Model):
    __tablename__= 'tags'

    id = db.Column("id", db.Integer, primary_key=True)
    tags_details= db.Column(db.string(100))
    tags_details = db.relationship('tags_details', backref='tags', lazy=True)

    lead= db.Column(db.ForeignKey('lead.id'), nullable=False)
    lead = db.relationship('communication_details', backref='tags', lazy=True)

    def __repr__(self):
       return f"<activity {self.id},{self.tags_details},{self.lead}>"
    

class TagsDetails(db.Model):
    __tablename__= 'tags_details'

    id = db.Column("id", db.Integer, primary_key=True)
    title= db.Column(db.string(60))
    datetime_update =db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create =db.Column(db.DateTime, default= datetime.utcnow, nullable= False)
  
    def __repr__(self):
       return f"<activity {self.id}, {self.title}>"