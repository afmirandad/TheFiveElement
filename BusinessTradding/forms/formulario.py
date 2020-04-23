from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormInicio(FlaskForm):
    nombre = StringField('Usuario', validators=[DataRequired(message='Se requiere que completes este campo')])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message='Se requiere que completes este campo')])
    recordar = BooleanField('Recordar Usuario')
    enviar = SubmitField('Iniciar Sesión')
