from app import app, db
from models import *

def insertToAllTables():
    try:
        with app.app_context():
            user_details_1 = UserDetails(firstname='John', lastname='Doe',   email='2@email.com', job_title='Manager',   phone='1234567890', addres='123 Main St')
            user_details_2 = UserDetails(firstname='Jane', lastname='Smith', email='1@email.com', job_title='Developer', phone='0987654321', addres='456 Second St')

            db.session.add(user_details_1)
            db.session.add(user_details_2)
            db.session.commit()
            
            user_1 = User(user_basic_details=user_details_1.id)

            db.session.add(user_1)
            db.session.commit()
            
            lead_details_1 = LeadDetails(firstname='Alice', lastname='Johnson', ORGANIZATION='Company A', email='alice@company.com', phone_number='1234567890', addres='789 Third St')
            lead_details_2 = LeadDetails(firstname='Bob',   lastname='Smith',   ORGANIZATION='Company B', email='bob@company.com',   phone_number='0987654321', addres='123 Fourth St')

            db.session.add(lead_details_1)
            db.session.add(lead_details_2)
            db.session.commit()
            
            lead_1 = Lead(firstname='Alice', lead_details=lead_details_1.id)
            lead_2 = Lead(firstname='Bob',   lead_details=lead_details_2.id)

            db.session.add(lead_1)
            db.session.add(lead_2)
            
            db.session.commit()
            
            activity_details_1 = ActivityDetails(title='Meeting',  activity_type='Call', user=user_1.id)
            activity_details_2 = ActivityDetails(title='Sleeping', activity_type='Rest', user=user_1.id)

            db.session.add(activity_details_1)
            db.session.add(activity_details_2)
            db.session.commit()
            
            activity_1 = Activity(lead=lead_details_1.id, activity_details=activity_details_1.id)
            activity_2 = Activity(lead=lead_details_2.id, activity_details=activity_details_2.id)

            db.session.add(activity_1)
            db.session.add(activity_2)
            db.session.commit()
            
            communication_details = CommunicationDetails(subject='Follow up', text='Following up', user=user_details_1.id)

            db.session.add(communication_details)
            db.session.commit()
            
            communication_1 = Communication(lead=lead_1.id, communication_details=communication_details.id)

            db.session.add(communication_1)
            db.session.commit()
            
            skills_details = SkillDetails(title='Python')

            db.session.add(skills_details)
            db.session.commit()
            
            skills_1 = Skill(lead=lead_1.id, skills_details=skills_details.id)

            db.session.add(skills_1)
            db.session.commit()
            
            tags_details = TagDetails(title='EXPERT')

            db.session.add(tags_details)
            db.session.commit()

            tags_1 = Tag(lead=lead_1.id, tags_details=tags_details.id)

            db.session.add(tags_1)
            db.session.commit()

    except Exception as e:
        print(f'Inserting data error.\nError: {e}')
