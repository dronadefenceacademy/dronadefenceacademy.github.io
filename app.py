from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sendgrid
import os
import logging

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
logging.basicConfig(filename='usage.log',level=logging.DEBUG)


class ReusableForm(Form):
	name = TextField('Full Name', validators=[validators.DataRequired()])
	email = TextField('Email ID')
	phone = TextField('Phone Number', validators=[validators.DataRequired()])
	choice = TextField('Parent or Student?')

@app.route("/", methods=['GET', 'POST'])
def index():
	form = ReusableForm(request.form)
	if(request.method == 'POST'):
		if(form.validate()):
			print("\""+ request.form['name'] + "\"")
			return render_template("index.html", form=form)

	return render_template("index.html", form=form)

@app.errorhandler(404)
def not_found(e):
	return 'Sorry, unexpected error: {}'.format(e), 404


@app.errorhandler(500)
def application_error(e):
	return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == "__main__":
	app.run(debug=True)
