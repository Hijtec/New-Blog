from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
    name=TextField("Your name");
    email=TextField("Email",[validators.Required("Please enter your email adress."), validators.Email("Please enter proper email adress")]);
    message=TextAreaField("Your message");
    submit=SubmitField("Send")