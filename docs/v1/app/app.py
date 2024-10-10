from flask import Flask, render_template, jsonify, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.secret_key = 'Asdasd@E!d121'
with app.app_context():
 db.create_all()

@app.route('/')
@app.route('/components')
def componentsView():
    return render_template('pages/components.html')


@app.route('/base')
def baseView():
    return render_template('pages/base.html')

# @app.route('/plus_button')
# def plus_buttonView():
#     return render_template('components/plus_button.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')