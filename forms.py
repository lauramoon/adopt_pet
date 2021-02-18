from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms import validators
from wtforms.fields.core import BooleanField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, NumberRange, Optional

class PetAddForm(FlaskForm):
    """Form for adding a pet to the database"""
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Name cannot be blank")])
    species = SelectField('Species', choices=['cat', 'dog', 'porcupine'])
    photo_url = URLField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional(), 
                       NumberRange(min=0, max=30, message='Please enter a whole number between 0 and 30')])
    notes = StringField("Notes")

class PetEditForm(FlaskForm):
    """Form for updating pet fields that can be edited"""
    photo_url = URLField("Photo URL", validators=[Optional()])
    notes = StringField("Notes")
    available = BooleanField("Available")