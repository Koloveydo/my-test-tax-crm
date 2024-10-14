from flask import Flask, render_template, jsonify, redirect, flash, session

from models import *

app = Flask(__name__)
app.secret_key = 'Asdasd@E!d121'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tax-crm.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

db.init_app(app)

@app.route('/')
@app.route('/components')
def componentsView():
    return render_template('pages/components.html')


@app.route('/base')
def baseView():
    return render_template('pages/base.html')

@app.route('/users')
def users_view():
    users = User_details.query.all()
    return render_template('pages/database_testing.html', users=users)



if __name__ == "__main__":
    with  app.app_context():
        db.create_all()
    app.run(debug=True, port=8080, host='0.0.0.0')