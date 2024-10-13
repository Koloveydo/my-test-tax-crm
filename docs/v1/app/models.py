from flask import Flask, render_template, jsonify, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Vladkondrun1210@localhost:3306/Data_base'
app.secret_key = 'Asdasd@E!d121'
db = SQLAlchemy(app)

class User(db.Model): 
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_basic_details = db.Column(db.Integer, db.ForeignKey('user_details.id'), nullable=False)
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  
    user_details = db.relationship('UserDetails', backref='user')
    
    def __repr__(self):
        return f"<User {self.id}, {self.user_basic_details} >"
   
class UserDetails(db.Model):
    __tablename__ = 'user_details'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    email = db.Column(db.String(40), unique=True)
    job_title = db.Column(db.String(60))
    phone_number = db.Column(db.String(14))
    address = db.Column(db.String(50))
    url_image = db.Column(db.Text)
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<UserDetails {self.id}, {self.first_name} {self.last_name}, {self.email}, {self.phone_number}>"
   
class Lead(db.Model):
    __tablename__ = 'lead'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    lead_details = db.Column(db.Integer, db.ForeignKey('lead_details.id'), nullable=False)
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    lead_details_rel = db.relationship('LeadDetails', backref='lead', uselist=False)

    def __repr__(self):
        return f"<Lead {self.id}, {self.first_name}, {self.lead_details}>"

class LeadDetails(db.Model):
    __tablename__ = 'lead_details'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    organization = db.Column(db.String(100))
    email = db.Column(db.String(40), unique=True)
    phone_number = db.Column(db.String(14))
    address = db.Column(db.String(50))
    url_image = db.Column(db.Text)
    comments = db.Column(db.Text)
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<LeadDetails {self.id}, {self.first_name}, {self.email}, {self.organization}, {self.phone_number}, {self.address}>"
    
class Activity(db.Model): 
    __tablename__ = 'activity'
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    activity_details_id = db.Column(db.Integer, db.ForeignKey('activity_details.id'), nullable=False)
    lead = db.relationship('Lead', backref='activities')
    activity_details = db.relationship('ActivityDetails', backref='activities')

    def __repr__(self):
        return f"<Activity {self.id}, {self.lead_id}, {self.activity_details_id}>"

class ActivityDetails(db.Model):
    __tablename__ = 'activity_details'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    activity_type = db.Column(db.String(40))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user = db.relationship('User', backref='activity_details')

    def __repr__(self):
        return f"<ActivityDetails {self.id}, {self.title}, {self.activity_type}>"

class Communication(db.Model):
    __tablename__ = 'communication'
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    communication_details_id = db.Column(db.Integer, db.ForeignKey('communication_details.id'), nullable=False)
    lead = db.relationship('Lead', backref='communications')
    communication_details = db.relationship('CommunicationDetails', backref='communications')

    def __repr__(self):
        return f"<Communication {self.id}, {self.lead_id}, {self.communication_details_id}>"

class CommunicationDetails(db.Model):
    __tablename__ = 'communication_details'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(60))
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user = db.relationship('User', backref='communication_details')

    def __repr__(self):
        return f"<CommunicationDetails {self.id}, {self.subject}, {self.user_id}>"

class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    lead = db.relationship('Lead', backref='skills')
    skill_details_id = db.Column(db.Integer, db.ForeignKey('skills_details.id'), nullable=False)
    skill_details = db.relationship('SkillDetails', backref='skills')

    def __repr__(self):
        return f"<Skill {self.id}, {self.lead_id}, {self.skill_details_id}>"

class SkillDetails(db.Model):
    __tablename__ = 'skills_details'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<SkillDetails {self.id}, {self.title}>"

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag_detail_id = db.Column(db.Integer, db.ForeignKey('tags_details.id'), nullable=False)
    tag_detail = db.relationship('TagDetails', backref='tags')
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    lead = db.relationship('Lead', backref='tags')

    def __repr__(self):
        return f"<Tag {self.id}, {self.tag_detail_id}, {self.lead_id}>"

class TagDetails(db.Model):
    __tablename__ = 'tags_details'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<TagDetails {self.id}, {self.title}>"

