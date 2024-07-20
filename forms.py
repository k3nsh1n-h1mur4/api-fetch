from flask_wtf import FlaskForm

from wtforms import IntegerField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from tools import PyMYSQL

class newUserForm(FlaskForm):
    username = StringField('Usuario:', validators=[DataRequired(), Length(5, 10)])
    password = PasswordField('Contraseña:', validators=[DataRequired(), Length(8, 20)])
    submit = SubmitField('Enviar')
    
    @classmethod
    def saveUser(cls, username, password):
        cn = PyMYSQL.Connection()
        print(cn)
        