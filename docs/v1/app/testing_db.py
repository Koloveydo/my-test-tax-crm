from app import app, db
from models import *

with app.app_context():

    new_user_details = User_details(firstname='John', lastname='Doe', email='john@email.com', job_title='Manager', phone='1234567890', addres='123 Main St', url_image='https/hshygyawgds')
    db.session.add(new_user_details)
    
    user = User_details(firstname='Jane', lastname='Smith', email='jane@email.com', job_title='Developer', phone='0987654321', addres='456 Second St')
    db.session.add(user)
    
    user1 = User_details(firstname='Obama', lastname='Bumson', email='obama@email.com', job_title='Developer', phone='0987654321', addres='456 Second St')
    db.session.add(user1)
    
    db.session.commit()
    print("DATA ADED")