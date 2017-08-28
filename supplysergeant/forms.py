from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, DecimalField, SelectField
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
    inventory_name = SelectField('Inventory Name', choices=[
        ('laptops', 'Laptops'), ('desktops', 'Desktops'), ('phones', 'Phones'), 
        ('monitors', 'Monitors')])
    submit = SubmitField("Add Item")