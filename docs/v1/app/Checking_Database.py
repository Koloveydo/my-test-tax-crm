from app import app, db
from models import *

with app.app_context():
    
    new_user_details = UserDetails(first_name='John', last_name='Doe', email='john@email.com', job_title='Manager', phone='1234567890', address='123 Main St', url_image='https/hshygyawgds')
    db.session.add(new_user_details)
    
    user = UserDetails(first_name='Jane', last_name='Smith', email='jane@email.com', job_title='Developer', phone='0987654321', address='456 Second St')
    db.session.add(user)
    
    user1 = UserDetails(first_name='Obama', last_name='Bumson', email='obama@email.com', job_title='Developer', phone='0987654321', address='456 Second St')
    db.session.add(user1)
    
    db.session.commit()
    print("DATA ADED")