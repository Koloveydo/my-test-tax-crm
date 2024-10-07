from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from datetime import datetime

class user(db.Model):
    __tablename__ = 'user'
    id=db.Column(db.Integer, primary_key=True)
    user_basic_details=db.Column(db.ForeignKey('user_details.id'), nullable=False)
    datetime_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    datetime_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('user', backref='user_detail', lazy=True)

    def __repr__(self):
        return f"user('{self.id}','{self.user_basic_details}', '{self.datetime_update}')"

class user_details(db.Model):
    __tablename__ = 'user_details'
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(40), nullable=False)
    last_name=db.Column(db.String(40), nullable=False)
    email=db.Column(db.String(40), nullable=False, unique=True)
    job_title=db.Column(db.String(60))
    phone_number=db.Column(db.String(14), nullable=False, unique=True)
    address=db.Column(db.String(50))
    url_image=db.Column(db.Text)
    datetime_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    datetime_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"user_details('{self.first_name}', '{self.last_name}', '{self.email}', '{self.job_title}', '{self.phone_number}', '{self.url_image}', '{self.datetime_update}')"

class lead(db.Model):
    __tablename__ = 'lead'
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(40), nullable=False)
    lead_details=db.Column(db.ForeignKey('lead_details.id'), nullable=False)
    datetime_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    datetime_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    lead = db.relationship('lead', backref='lead_details', lazy=True)

    def __repr__(self):
        return f"lead('{self.first_name}', '{self.lead_details}'), '{self.datetime_update}'"

class lead_details(db.Model):
    __tablename__ = 'leads_details'
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(40), nullable=False)
    last_name=db.Column(db.String(40), nullable=False)
    ORGANIZATION=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(40), nullable=False, unique=True)
    phone_number=db.Column(db.String(14), nullable=False, unique=True)
    address=db.Column(db.String(50))
    url_image=db.Column(db.Text)
    comments=db.Column(db.Taxt)
    datetime_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    datetime_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"user_details('{self.first_name}', '{self.last_name}', '{self.email}', '{self.job_title}', '{self.phone_number}', '{self.url_image}', '{self.datetime_update}')" 

class activity(db.Model):
    __tablename__ = 'activity'
    id=db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.ForeignKey('lead.id'), nullable=False)
    lead = db.relationship('lead', backref='activities', lazy=True)

    activity_details_id=db.Column(db.ForeignKey('activity_details.id'), nullable=False)
    activity_details = db.relationship('activity_details', backref='activities', lazy=True)

    def __repr__(self):
        return f"activity('{self.id}', Lead: '{self.lead}', Details: '{self.activity_details}')"

class activity_details(db.Model):
    __tablename__ = 'activity_details'
    title = db.Column(db.String(40), nullable=False)
    activity_type = db.Column(db.String(40), nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    datetime_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    datetime_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    activity_details = db.relationship('activity_details', backref='users', lazy=True)

    def __repr__(self):
        return f"activite_details('{self.title}', '{self.activity_type}', '{self.user}', '{self.datetime_update}')"

class communication(db.Model):
    __tablename__ = 'communication'
    id=db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.ForeignKey('lead.id'), nullable=False)
    lead = db.relationship('lead', backref='communications', lazy=True)

    communication_details_id=db.Column(db.ForeignKey('communication_details.id'), nullable=False)
    communication_details = db.relationship('communication_details', backref='communications', lazy=True)

    def __repr__(self):
        return f"activity('{self.id}', Lead: '{self.lead}', Details: '{self.communication_details}')"
    
class communication_details(db.Model):
    __tablename__ = 'communication_details'
    id = db.Column(db.Intager, ptimary_key=True)
    subject = db.Column(db.String(60), nullable=False)
    text = db.Column(db.Text)
    user=db.Column(db.ForeignKey('user.id'), nullable=False)
    datetime_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    datetime_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    communication_details = db.relationship('communication_details', backref='users', lazy=True)

    def __repr__(self):
        return f"communication_details('{self.id}', '{self.subject}', '{self.user}', '{self.text}', '{self.datetime_update}')"

class skills(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.ForeignKey('lead.id'), nullable=False)
    lead = db.relationship('lead', backref='skills', lazy=True)

    skils_details_id=db.Column(db.ForeignKey('skills_details.id'), nullable=False)
    skills_details = db.relationship('skills_details', backref='skills', lazy=True)

    def __repr__(self):
        return f"activity('{self.id}', Lead: '{self.lead}', Details: '{self.skills_details}')"

class skills_details(db.Model):
    __tablename__ = 'skills_details'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    datetime_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    datetime_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"activity('{self.id}', '{self.title}', '{self.datetime_update}')"

class tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.ForeignKey('lead.id'), nullable=False)
    lead = db.relationship('lead', backref='tags', lazy=True)

    tags_details_id=db.Column(db.ForeignKey('tags_details.id'), nullable=False)
    tags_details = db.relationship('tags_details', backref='tags', lazy=True)

    def __repr__(self):
        return f"activity('{self.id}', Lead: '{self.lead}', Details: '{self.tags_details}')"
    
class tags_details(db.Model):
    __tablename__ = 'tags_details'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    datetime_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    datetime_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"activity('{self.id}', '{self.title}', '{self.datetime_update}')"
