from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "1294726udfhaibio"

@app.route('/')
def home():
    return render_template('templates/home.html')

@app.route('/activity')
def activity():
    return render_template('templates/Activity.html')

@app.route('/communication')
def communication():
    return render_template('templates/communication.html')

@app.route('/company')
def company():
    return render_template('templates/Company.html')

@app.route('/contacts')
def contacts():
    return render_template('templates/Contacts.html')

@app.route('/contacts-clients')
def contacts_clients():
    return render_template('templates/ContactsClients.html')

@app.route('/details')
def details():
    return render_template('templates/Details.html')

@app.route('/team-administration')
def team_administration():
    return render_template('templates/TEAM_Administration.html')

@app.route('/user-profile')
def user_profile():
    return render_template('templates/user_profile.html')

if __name__ == "__main__":
 app.run(debug=True, host='0.0.0.0', port=8080)