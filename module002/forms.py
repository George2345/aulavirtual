from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length

class EntradaForm(FlaskForm): # class RegisterForm extends FlaskForm
    titulo = StringField('Titulo',validators=[InputRequired(),Length(min=1,max=50)])
    cuerpo = StringField('Cuerpo',validators=[InputRequired(),Length(min=10,max=10000)])

class ComentarioForm(FlaskForm): # class RegisterForm extends FlaskForm
    cuerpo = StringField('Cuerpo',validators=[InputRequired(),Length(min=10,max=10000)])