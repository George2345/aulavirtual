from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, SelectField, HiddenField#, DateField
from wtforms.validators import InputRequired, Length
from wtforms.fields.html5 import DateField, TimeField, DateTimeLocalField
import datetime

class TareaForm(FlaskForm): # class RegisterForm extends FlaskForm
    titulo = StringField('Titulo',validators=[InputRequired(),Length(min=1,max=30)])
    contenido = StringField('Contenido',validators=[InputRequired(),Length(min=1,max=255)])
    fecha = DateField('Fecha de entrega',format='%Y-%m-%d')