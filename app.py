import os
from pathlib import Path
from issues.issuesPwd import PwdBD

from dotenv import dotenv_values

config = dotenv_values('.env') 

from flask import Flask, url_for, render_template, request, jsonify

from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from forms import newUserForm
from tools import PyMYSQL

pure = Path.cwd()

app = Flask(__name__, template_folder='templates', static_folder='static', instance_path=pure)
app.config['SECRET_KEY'] = os.urandom(16)

Bootstrap5(app)
csrf = CSRFProtect(app)

@app.get('/')
def index():
    return 'Index de la página'

@app.route('/user', methods=['GET', 'POST'])
def user():
    form = newUserForm()
    #print(dir(form))
    if request.method == 'GET':
        form = newUserForm()
    elif request.method == 'POST':
        data = form.data
        username = data['username']
        password = data['password']
        print(username,password)
    return render_template('user.html', form=form) 

@app.route('/newUser', methods=['GET', 'POST'])
def newUser():
    if request.method == 'GET':
        return render_template('index.html', title='Crear Usurio')
    elif request.method == 'POST':
        username = request.form['username'] 
        print(username)
    return 'sdfsdf'

@app.route('/getUsersAll', methods=['GET', 'POST'])
def getUsersAll():
    if request.method == 'GET':
        py = PyMYSQL()
        ctx = py.getUsers()
        if ctx == None:
            return jsonify({'message': 'No se encontraron Registros'})
        print(type(ctx))
    return render_template('list.html', ctx=ctx)


        

app.run(debug=True)