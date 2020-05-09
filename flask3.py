from flask import Flask , render_template , redirect ,url_for , request
from flask_sqlalchemy import SQLAlchemy

name=" "
city=" "
passWord=" "
passWordC=" "
email=" "
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False 
db = SQLAlchemy(app)

__tablename__= "data_web"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)



@app.route('/')
@app.route('/h')
def login():
	return render_template('page1.html')

@app.route('/ch_account' , methods =['POST','GET'])
def login2():
	name_f=request.form['name']
	passWord=request.form['Password']
	try:
	  Ch=User.query.filter_by(name=name_f).first()
	  if Ch.password == passWord:
	  	print(passWord)
	  	return render_template('page3.html')
	  else:
	  	return render_template('page1.html', error_login="The Password Error")
	except:
		return render_template('page1.html', error_login="Something Error")

@app.route('/signin')
def first_signin():
	return render_template('page2.html')

@app.route('/signin2',  methods =['POST','GET'])
def signin():
	name=request.form['name']
	passWord=request.form['Password']
	passWordC=request.form['PasswordC']
	city=request.form['city']
	email=request.form['email']
	if name == "":
		error="Enter Username "
		return render_template('page2.html',error_u=error)
	elif passWord =="":
		error="Enter Your Password"
		return render_template('page2.html',error_p=error)
	elif passWord != passWordC:
		error="Passwords Don't Match"
		return render_template('page2.html',error_pc=error)
	elif email =="":
		error="Enter Your Email"
		return render_template('page2.html',error_e=error)
	elif city =="":
		error="Enter Your City"
		return render_template('page2.html',error_c=error)
	else:
		try:
			us=User(name=name, email=email,city=city,password=passWord)
			db.session.add(us)
			db.create_all()
			db.session.commit()
			return render_template('page3.html',n=name)
		except:
			error_find="The account exists"
			return render_template('page2.html',error_find=error_find)

@app.route('/home', methods =['POST','GET'])
def getvalue():
	name=request.form['name']
	return render_template('page3.html',n=name)


if __name__ == '__main__': 
	app.run(debug = True)