from flask import Flask, render_template, jsonify, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'Asdasd@E!d121'

@app.route('/')
@app.route('/components')
def componentsView():
    return render_template('pages/components.html')


@app.route('/base')
def baseView():
    return render_template('pages/base.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')