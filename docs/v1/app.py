from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "shftbcgei227654ft22876"

@app.route('/')
def IndexView():
   return render_template('pages/index.html')


@app.route('/company')
def CompanyView():
   return render_template('pages/company.html')


@app.route('/contacts')
def ContactsView():
   return render_template('pages/contacts.html')


@app.route('/global_profile')
def GlobalProfileView():
   return render_template('pages/globalprofile.html')


@app.route('/team_administartion')
def AdministrationView():
   return render_template('pages/teamadministration.html')


@app.route('/user_activity')
def ActivityView():
   return render_template('pages/useractivity.html')


@app.route('/user_profile')
def ProfileView():
   return render_template('pages/userprofile.html')


@app.route('/user_profile_notes')
def ProfileNotesView():
   return render_template('pages/userprofilenotes.html')


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8080)