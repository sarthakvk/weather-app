from wtforms import StringField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import data_required


class myform(FlaskForm):

    location = StringField("Enter location",validators=[data_required()])
    submit = SubmitField("Submit")
