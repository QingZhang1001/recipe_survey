from flask_wtf import FlaskForm as Form
from wtforms import StringField,HiddenField
from wtforms.validators import DataRequired,Length

class myForm(Form):
    user = StringField('user',validators=[Length(min=4,max=25),DataRequired()])
    user_id= HiddenField()