<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy 
=======
from flask_sqlalchemy import SQLAlchemy
>>>>>>> dd396cf805fb55f6be0cb6b763fd160755089736
from datetime import datetime

db = SQLAlchemy()

class User(db.Model): 
<<<<<<< HEAD
    __tablename__ = 'user'

    id                 = db.Column(db.Integer, primary_key=True)
    user_basic_details = db.Column(db.Integer, db.ForeignKey('user_details.id'))
    datetime_update    = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create    = db.Column(db.DateTime, default=datetime.utcnow)  
   
class UserDetails(db.Model):
    __tablename__ = 'user_details'

    id              = db.Column(db.Integer, primary_key=True)
    first_name      = db.Column(db.String(40))
    last_name       = db.Column(db.String(40))
    email           = db.Column(db.String(40), unique=True)
    job_title       = db.Column(db.String(60))
    phone_number    = db.Column(db.String(14))
    address         = db.Column(db.String(50))
    url_image       = db.Column(db.Text)
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): return f" {self.first_name}, {self.last_name}, {self.email},{self.phone_number}"
   
class Lead(db.Model):
    __tablename__ = 'lead'

    id              = db.Column(db.Integer, primary_key=True)
    lead_details    = db.Column(db.Integer, db.ForeignKey('lead_details.id'))
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow)

class LeadDetails(db.Model):
    __tablename__ = 'lead_details'
    
    id              = db.Column(db.Integer, primary_key=True)
    first_name      = db.Column(db.String(40))           
    organization    = db.Column(db.String(100))
    email           = db.Column(db.String(40), unique=True)
    phone_number    = db.Column(db.String(14))
    address         = db.Column(db.String(50))
    url_image       = db.Column(db.Text)
    comments        = db.Column(db.Text)
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): return f"{self.first_name} | {self.email} | {self.organization}"
    
class Activity(db.Model): 
    __tablename__ = 'activity'

    id                  = db.Column(db.Integer, primary_key=True)
    lead_id             = db.Column(db.Integer, db.ForeignKey('lead.id'))
    activity_details_id = db.Column(db.Integer, db.ForeignKey('activity_details.id'))
    lead                = db.relationship('Lead', backref='activities')
    activity_details    = db.relationship('ActivityDetails', backref='activities')

class ActivityDetails(db.Model):
    __tablename__   = 'activity_details'

    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(40))
    activity_type   = db.Column(db.String(40))
    user_id         = db.Column(db.Integer, db.ForeignKey('user.id'))
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow)

class Communication(db.Model):
    __tablename__ = 'communication'

    id                       = db.Column(db.Integer, primary_key=True)
    lead_id                  = db.Column(db.Integer, db.ForeignKey('lead.id'))
    communication_details_id = db.Column(db.Integer, db.ForeignKey('communication_details.id'))

class CommunicationDetails(db.Model):
    __tablename__ = 'communication_details'

    id              = db.Column(db.Integer, primary_key=True)
    subject         = db.Column(db.String(60))
    text            = db.Column(db.Text)
    user_id         = db.Column(db.Integer, db.ForeignKey('user.id'))
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):return f"{self.text}"

class Skill(db.Model):
    __tablename__ = 'skills'

    id               = db.Column(db.Integer, primary_key=True)
    lead_id          = db.Column(db.Integer, db.ForeignKey('lead.id'))
    skill_details_id = db.Column(db.Integer, db.ForeignKey('skills_details.id'))


class SkillDetails(db.Model):
    __tablename__ = 'skills_details'

    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(60))
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):return f" {self.title}"

class Tag(db.Model):
    __tablename__ = 'tags'

    id            = db.Column(db.Integer, primary_key=True)
    tag_detail_id = db.Column(db.Integer, db.ForeignKey('tags_details.id'))
    lead_id       = db.Column(db.Integer, db.ForeignKey('lead.id'))

class TagDetails(db.Model):
    __tablename__ = 'tags_details'

    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(60))
    datetime_update = db.Column(db.DateTime, onupdate=datetime.utcnow) 
    datetime_create = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):return f" {self.title}"

=======
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
    
>>>>>>> dd396cf805fb55f6be0cb6b763fd160755089736
