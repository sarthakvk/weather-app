from wtforms import StringField,SubmitField
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import data_required


class myform(FlaskForm):

    location = StringField("Enter location",validators=[data_required()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")
