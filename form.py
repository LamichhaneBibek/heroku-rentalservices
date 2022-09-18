from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,PasswordField,IntegerField
from wtforms.validators import DataRequired, Length,Email,EqualTo,DataRequired


# from flask_wtf import FlaskForm
from wtforms.fields import DateField
# from wtforms.validators import DataRequired
from wtforms import validators, SubmitField




class RegistrationForm(FlaskForm):
	# firstname = StringField('First Name')
	firstname =StringField('Firstname',
	 					validators=[DataRequired(),Length(min=2,max=10)])
	lastname =StringField('Lastname',
	 					validators=[DataRequired(),Length(min=2,max=10)])
	address =StringField('Address',
					validators=[DataRequired(),Length(min=3,max=20)])
	district =StringField('District',
					validators=[DataRequired(),Length(min=3,max=20)])

    


	email =StringField('Email',validators=[DataRequired(),Email()])
	password =PasswordField('Password',validators=[DataRequired(),Length(min=5,max=20)])

	confirm_password =PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit =SubmitField('Register') 




class InfoForm(FlaskForm):
    startdate = DateField('Booked for Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    submit = SubmitField('Proceed')
	