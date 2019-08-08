from flask import Flask , render_template , flash , url_for , redirect , request
from content_management import Content
from dbconnect import connection
from wtforms import Form,BooleanField,TextField,PasswordField,validators
from passlib.hash import sha256_crypt




TOPIC_DICT = Content()

app = Flask(__name__)

app.secret_key = 'super secret key'

@app.route('/')
def home():
	return render_template('main.html')

@app.route('/dashboard/')
def dashboard():
	flash("Welcome Python user")
	return render_template('dashboard.html', TOPIC_DICT = TOPIC_DICT)

# Handling errors in flask below method

@app.errorhandler(404)
def page_not_found(e):
	return "No Page found"


@app.route('/introduction-to-python-programming/')
def intro_to_python_programming():
	return "<h1>Success</h1>"


@app.route('/login/',methods=['GET','POST'])
def login_page():
	error = None
	try:
		if request.method == 'POST':
			attempted_username = request.form['username']
			attempted_password = request.form['password']

			#flash(attempted_username) 
			#flash(attempted_password)

			if attempted_username == 'admin' and attempted_password == 'admin':
				return redirect(url_for('dashboard'))
			else :
				error = "Invalid Credentials Try Again"

		return render_template('login.html',error=error)
	

	except Exception as e:
		return render_template("login.html",error=error)
	

class RegistrationForm(Form):
	username = TextField('Username', [validators.Length(min=4,max=20)])
	email = TextField('Email Address', [validators.Length(min=6,max=50)])
	password = PasswordField('Password', [validators.Required(),validators.EqualTo('confirm',message="Passwords must match")])
	confirm = PasswordField('Retype Password')
	accept_tos = BooleanField('I accept the <a href ="/tos/">terms and conditions </a> and <a href="/privacy/">the Privacy and Security Notice(Last update April 2019)',[validators.Required()])


@app.route('/register/',methods=['GET','POST'])
def register_page():
	try:
		form = RegistrationForm(request.form)
		if request.method == "POST" and form.validate():
			username = form.username.data
			email=form.email.data
			password=sha256_crypt.encrypt(str(form.password.data))
			c , conn = connection()

			




	except Exception as e:
		raise e












	


if __name__ == '__main__':
	app.run(debug=True)
	