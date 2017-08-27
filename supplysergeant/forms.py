from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import Email, DataRequired

class SignupForm(Form):
    email = StringField('email', 
                validators=[DataRequired(),Email()])
    password = PasswordField(
                'password', 
                validators=[DataRequired()])
    submit = SubmitField("Sign In")
    
class AddItemForm(Form):
    name = StringField('name', 
                validators=[DataRequired()])
    assignee = StringField(
                'assignee', 
                validators=[DataRequired()])
    cost = DecimalField(
                'cost', places=2, rounding=None, use_locale=False,
                validators=[DataRequired()])
    submit = SubmitField("Add Item")