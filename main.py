
from flask import Flask,render_template,request,redirect,flash,url_for,session,jsonify,make_response

import pdfkit

from flask import *
import urllib.request
import os
from werkzeug.utils import secure_filename
from form import RegistrationForm,InfoForm
from werkzeug.security import generate_password_hash, check_password_hash

# mail verification
from flask_mail import *
from random import *
from itsdangerous import URLSafeTimedSerializer

# chat
from flask_sqlalchemy import SQLAlchemy
import os
import json


# datepicker
# from flask_wtf import FlaskForm
# from wtforms.fields import DateField
# from wtforms.validators import DataRequired
# from wtforms import validators, SubmitField



import requests
# # blueprint code line1 (total 2 line)
# from profile import second




from flask_mysqldb import MySQL
from flask_session import Session
from datetime import datetime


app = Flask(__name__)






# chat
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/rental_services'
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = app.root_path + '/static/img/'

db = SQLAlchemy(app)

class Users(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(100),unique=False,nullable=False)
    last_name = db.Column(db.String(100),unique=False,nullable=False)
    email = db.Column(db.String(100),unique=False,nullable=False)
    address = db.Column(db.String(100),unique=False,nullable=False)
    district = db.Column(db.String(100),unique=False,nullable=False)
    phone_number = db.Column(db.String(100),unique=False,nullable=False)
    password = db.Column(db.String(300),unique=False,nullable=False)
    image_path=db.Column(db.String(100),unique=False,nullable=False)
    created_on = db.Column(db.String(100),unique=False,nullable=False)
    created_on_time = db.Column(db.String(100),unique=False,nullable=False)
    

class Contact(db.Model):
    Id = db.Column(db.Integer, primary_key = True)
    sender = db.Column(db.String(100), unique=False, nullable=False)
    reciver = db.Column(db.String(100), unique=False, nullable=False)

class Messages(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), unique=False, nullable=False)
    msg = db.Column(db.String(100), unique=False, nullable=False)
    reciver = db.Column(db.String(100), unique=False, nullable=False)
    dateTime = db.Column(db.String(100), unique=False, nullable=False)





# mail verificaion
with open('config.json','r') as f:
    params=json.load(f)['param']

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = params['gmail-user']
app.config['MAIL_PASSWORD'] = params['gmail-pass']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY']='secret'

mail = Mail(app)

s= URLSafeTimedSerializer(app.config['SECRET_KEY'])





# # blueprint code line2
# app.register_blueprint(second,url_prefix="")



# wtform secretkey
app.config['SECRET_KEY']='wtform_secret_key'


# UPLOAD_FOLDER ='static/img/'

# app.secret_key ="secret key"
# app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH']=16 * 1024 * 1024




ALLOWED_EXTENSIONS =set(['png','jpg','jpeg','gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


#database setting for mysql
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='rental_services'

mysql=MySQL(app)


# Session setting 
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)




@app.route("/")
@app.route("/home")
def home():
	# code for retrieving all flat
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM flat;''')
	allRoom =cursor.fetchmany(6)
	print(allRoom)
	print()
	print('...................................................')
	print()
	cursor.close()


	# code for retrieving all vehicle
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM vechile;''')
	allVehicle =cursor.fetchmany(6)
	print(allVehicle)
	print()
	print('...................................................')
	print()
	cursor.close()

	# code for retrieving all hall
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM hall;''')
	allHall =cursor.fetchmany(6)
	print(allHall)
	print()
	print('...................................................')
	print()
	cursor.close()


# //////////////////////////////
	
	# allVehicle=None
	loged_in_user=None
	if session.get('email'):
		loged_in_user=session['email']

		
		cursor =mysql.connection.cursor()
		#resp=cursor.execute('''SELECT * FROM user WHERE email=%s and password=%s;''',(email,password))
		resp=cursor.execute('''SELECT email,user_id,first_name,password,image_path FROM users WHERE email=%s;''',(loged_in_user,))
		
		user=cursor.fetchone()

		print(user)
		cursor.close()
		return render_template("home.html",result={'user':user,'allRoom':allRoom,'allVehicle':allVehicle,'allHall':allHall})
	else:
		user = None
		return render_template("home.html",result={'user':user,'allRoom':allRoom,'allVehicle':allVehicle,'allHall':allHall})

#here
@app.route("/register",methods=['GET','POST'])
def register():
	# check
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT email FROM users;''')
	emailList =cursor.fetchall()
	print(emailList)
	print(emailList[5])
	cursor.close()

	
	form=RegistrationForm()
	if form.validate_on_submit():
		print('.................................RegistrationForm..............')
		fname = form.firstname.data
		print(fname)
		lname = form.lastname.data
		print(lname)
		address = form.address.data
		print(print)
		district = form.district.data
		print(district)
		email = form.email.data
		print(email)
		password = form.password.data
		print('password')

		confirm_password= form.confirm_password.data
		print(confirm_password)
		hashed_password = generate_password_hash(password)
		img=None
		phone=request.form['phone_number']
		print(phone)
		# check
		cursor =mysql.connection.cursor()
		cursor.execute('''SELECT email FROM users WHERE email=%s;''',(email,))
		emailList =cursor.fetchone()
		print("____email list____ = ",emailList)
		cursor.close()

		if emailList:
			return render_template('alreadyRegisteredPage.html')
		else:
			date_time=datetime.now()
			date= date_time.date()
			time=date_time.time()
			print(date)
			print(time)
# ////////
			gmail=email
			print('mail send garda',gmail)
			token= s.dumps(gmail, salt='email-confirmation-key')
			msg=Message('confirmation',sender='canteenmeal4@gmail.com', recipients=[gmail])
			link= url_for('confirm',token=token,_external=True)
			msg.body='Your Confirmation link is' + link
			mail.send(msg)
# //////////////////

			cursor =mysql.connection.cursor()
			cursor.execute('''INSERT INTO users VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(fname,lname,email,address,district,phone,hashed_password,img,date,time))
			mysql.connection.commit()
			cursor.close()
			

			value=0
			print('confirm table ma pu ',gmail)
			cursor =mysql.connection.cursor()
			cursor.execute('''INSERT INTO email_confirm_table VALUES(null,%s,%s)''',(gmail,value))
			mysql.connection.commit()
			cursor.close()


			session['value']=gmail
			return render_template('login.html',result="Register sucessfully, please login to continue..")

		# print(firstname,lastname,address,district,email,password)
		# return redirect(url_for('login'))
	return render_template("register.html",form=form)


@app.route('/confirm/<token>')
def confirm(token):

    try:
    	print("confirmation done by emila")
    	email=session.get('value')
    	print("email before update",email)
    	value=1
    	cursor =mysql.connection.cursor()
    	cursor.execute("UPDATE `email_confirm_table` SET `value`=%s WHERE `email`=%s",(value,email)); 
    	mysql.connection.commit()
    	cursor.close()
    	print('after query')

    	s.loads(token,salt='email-confirmation-key',max_age=3600)
    except Exception:
        return "<h1>Link Expired</h1>"
    flash('Confirmation Done')        
    return render_template('login.html')
    # return "<h1>Confirmation Done</h1>"



@app.route("/login")
def login():
	return render_template("login.html")


@app.route('/doLogin',methods=['post'])
def doLogin():

	email=request.form['email']
	password=request.form['password']

	# code temporary for admin login
	if email=="admin@gmail.com" and password=="admin":
		print('admin loged in........................................................... ')
		session['email']=email  
		session['userId']= 1
		user=session.get('email')

		print(user)
		print('admin userid',session.get('userId'))
		count_user=getTotalUser()
		count_flat=getTotalFlat()
		count_vehicle=getTotalVehicle()
		count_hall=getTotalHall()
		sixFlat=getSixFlat()
		sixVehicle=getSixVehicle()
		sixHall=getSixHall()
		count_booked_vehicle=getTotalBookedVehicle()
		count_booked_hall=getTotalBookedHall()
		return render_template('adminDashboard.html',result={'user':user,'count_user':count_user,'count_flat':count_flat,'count_vehicle':count_vehicle,'count_hall':count_hall,'sixFlat':sixFlat,'sixVehicle':sixVehicle,'sixHall':sixHall,'count_booked_vehicle':count_booked_vehicle,'count_booked_hall':count_booked_hall}) 

	
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT value FROM email_confirm_table WHERE email=%s;''',(email,))
	user=cursor.fetchone()
	cursor.close()
	# print('user',user)
	# print('user[0]',user[0])
	
	if user[0] ==1:
		cursor =mysql.connection.cursor()
		#resp=cursor.execute('''SELECT * FROM user WHERE email=%s and password=%s;''',(email,password))
		# resp=cursor.execute('''SELECT email,user_id,first_name,password FROM users WHERE email=%s and password=%s;''',(email,password))
		# login wiht hashing pwd	
		resp=cursor.execute('''SELECT email,user_id,first_name,password,phone_number FROM users WHERE email=%s;''',(email,))


		user=cursor.fetchone()
		cursor.close()
		# print("here is the vlaue of ")
		print(user)
		

		# print(user[0])
		# print(hashed_password_form_db)
		# if resp==1:
		

		if resp:
			hashed_password_form_db= user[3]
			# result =check_password_hash(hashed_password_form_db,password)
			# print(result)
		
		# login with hashing pwd
			if check_password_hash(hashed_password_form_db,password):	 
				session['email']=email  
				session['userId']= user[1]
				session['phone_number']= str(user[4])
				print('contact number from session ',type(session.get('phone_number')))
				session['user_session']=email
				loged_in_user=session.get('email')
				userIDis=session.get('userId')
				print("value fo loged_in_user")
				print(loged_in_user)
				print("value of userid")
				print(userIDis)
				return redirect(url_for('home'))
				# return render_template('home.html',result={'user':user})
			else: 
				return render_template('login.html',result="Invalid password")

				# using dictionary > result={"email":email}  
				# and to get data in html >result.email
		else:
			return render_template('login.html',result="Invalid user")
	else:
		return render_template('login.html',result="check you email for confirmation")		


# code for admin dashboard to show total user,flat,vehicle,hall
def getTotalUser():
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT COUNT(user_id) FROM `users` ;''')
	count_user=cursor.fetchone()
	# count_room=count_room[0]
	cursor.close()
	print('no of user ',count_user)
	return count_user

def getTotalFlat():
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT COUNT(flat_id) FROM `flat` ;''')
	count_flat=cursor.fetchone()
	# count_room=count_room[0]
	cursor.close()
	print('no of flat ',count_flat)
	return count_flat


def getTotalVehicle():
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT COUNT(id) FROM `vechile` ;''')
	count_vehicle=cursor.fetchone()
	# count_room=count_room[0]
	cursor.close()
	print('no of flat ',count_vehicle)
	return count_vehicle


def getTotalHall():
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT COUNT(hall_id) FROM `hall` ;''')
	count_hall=cursor.fetchone()
	# count_room=count_room[0]
	cursor.close()
	print('no of flat ',count_hall)
	return count_hall

# end code

# total no. of booked vehicle
def getTotalBookedVehicle():
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT COUNT(booked_id) FROM `booked_vehicle_table` ;''')
	count_booked_vehicle=cursor.fetchone()
	cursor.close()
	print('no of booked vehicle ',count_booked_vehicle)
	return count_booked_vehicle

# total no. of booked hall
def getTotalBookedHall():
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT COUNT(booked_id) FROM `booked_hall_table` ;''')
	count_booked_hall=cursor.fetchone()
	cursor.close()
	print('no of booked hall',count_booked_hall)
	return count_booked_hall




# code for retrieving 6 flat to show in admin home page i.e. admin dashboard

def getSixFlat():
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM flat;''')
	sixFlat =cursor.fetchmany(6)
	print(sixFlat)
	print()
	print('...................................................')
	print()
	cursor.close()
	return sixFlat


# code for retrieving 6 vehicle to show in admin home page i.e. admin dashboard
def getSixVehicle():
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM vechile;''')
	sixVehicle =cursor.fetchmany(6)
	print(sixVehicle)
	print()
	print('...................................................')
	print()
	cursor.close()
	return sixVehicle 

# code for retrieving 6 hall to show in admin home page i.e. admin dashboard
def getSixHall():
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM hall;''')
	sixHall =cursor.fetchmany(6)
	print(sixHall)
	print()
	print('...................................................')
	print()
	cursor.close()
	return sixHall

# forget password...................................................................
otp= randint(100000, 999999)

@app.route('/forgetPassword')
def verify():
    return render_template('emailOTPVerify.html')

@app.route('/doVerifyEmail', methods=['GET','POST'])
def doVerify():
    gmail=request.form['gmail']
    # token= s.dumps(gmail, salt='email-confirmation-key')
    msg=Message('OTP',sender='canteenmeal4@gmail.com', recipients=[gmail])
    # link= url_for('confirm',token=token,_external=True)
    msg.body = str(otp)
    mail.send(msg)

    session['mail_for_change_pw']=gmail

    # return '<h1>Check Your Email for Confirmation Link</h1>'
    return render_template('emailOTPValidate.html')

@app.route('/doValidate', methods=['POST'])
def doValidate():
    userOTP=request.form['OTP']
    if otp == int(userOTP):
    	# update password
    	new_pw=request.form['new_pw']
    	email=session.get('mail_for_change_pw')
    	hashed_password = generate_password_hash(new_pw)
    	cursor =mysql.connection.cursor()
    	cursor.execute("UPDATE `users` SET `password`=%s WHERE `email`=%s",(hashed_password,email));
    	mysql.connection.commit()
    	cursor.close()
    	flash('password sucessfully updated')
    	return render_template('login.html')
    return render_template('emailOTPVerify.html',msg="Otp Not Verified Try Again!!")


# @app.route('/changePasswordSucessfully', methods=['POST'])
# def changePasswordSucessfully():
#     new_pw=request.form['new_pw']


#     email=session.get('mail_for_change_pw')
#     hashed_password = generate_password_hash(new_pw)


#     cursor =mysql.connection.cursor()
#     cursor.execute("UPDATE `users` SET `password`=%s WHERE `email`=%s",(hashed_password,email)); 
#     mysql.connection.commit()
#     cursor.close()
#     flash('password sucessfully updated')	
	

#     return render_template('login.html')
    
# ..........................................................................................





@app.route("/fname", methods=['POST'])
def changefname():
	fname=request.form['fname']
	print(fname)
		
	cursor =mysql.connection.cursor()
	cursor.execute("UPDATE `users` SET `first_name`=%s WHERE `email`=%s",(fname,session['email'],)); 
	mysql.connection.commit()
	cursor.close()
	flash('First name sucessfully updated')	
	

	return redirect("profile")


@app.route("/lname", methods=['POST'])
def changelname():
	lname=request.form['lname']
	print(lname)
		
	cursor =mysql.connection.cursor()
	cursor.execute("UPDATE `users` SET `last_name`=%s WHERE `email`=%s",(lname,session['email'],)); 
	mysql.connection.commit()
	cursor.close()
	flash('Lastname sucessfully updated')	
	

	return redirect("profile")
	

@app.route("/address", methods=['POST'])
def changeAddress():
	address=request.form['address']
	print(address)
		
	cursor =mysql.connection.cursor()
	cursor.execute("UPDATE `users` SET `address`=%s WHERE `email`=%s",(address,session['email'],)); 
	mysql.connection.commit()
	cursor.close()
	flash('Phonenumber sucessfully updated')	
	

	return redirect("profile")

@app.route("/district", methods=['POST'])
def changeDistrict():
	district=request.form['district']
	print(district)
		
	cursor =mysql.connection.cursor()
	cursor.execute("UPDATE `users` SET `district`=%s WHERE `email`=%s",(district,session['email'],)); 
	mysql.connection.commit()
	cursor.close()
	flash('District sucessfully updated')	
	

	return redirect("profile")

@app.route("/phonenumber", methods=['POST'])
def changePhonenumber():
	phonenumber=request.form['phonenumber']
	print(phonenumber)
		
	cursor =mysql.connection.cursor()
	cursor.execute("UPDATE `users` SET `phone_number`=%s WHERE `email`=%s",(phonenumber,session['email'],)); 
	mysql.connection.commit()
	cursor.close()
	flash('Phonenumber sucessfully updated')	
		

	return redirect("profile")
	
	



@app.route('/logout')
def logout():
	session["email"]=None
	session["userId"]=None

	return redirect("/")

@app.route("/myProfilePage")
def myProfilePage():
	userId=getUserIdFromSession()
	# selecting user details
	cursor=mysql.connection.cursor()
	cursor.execute('''SELECT * FROM `users` where `user_id`=%s;''',(userId,))	
	userInfo=cursor.fetchall()
	print("userInfo")
	print(userInfo)
	cursor.close()
	
	# selecting flat whishlist of user
	cursor=mysql.connection.cursor()
	cursor.execute('''SELECT wf.id ,wf.user_id ,f.flat_id,f.flat_title,f.address,f.flat_district ,f.price,f.img1_path FROM `wishlist_flat` as wf join `flat` as f on wf.flat_id = f.flat_id WHERE wf.user_id=%s;''',(userId,))
	savedFlat=cursor.fetchall()
	print("saved hall list by user with user id",userId)
	print(savedFlat)
	cursor.close()
	


	# selecting hall whishlist of user
	cursor=mysql.connection.cursor()
	cursor.execute('''SELECT wh.id ,wh.user_id ,h.hall_id,h.hall_name,h.hall_address,h.hall_district ,h.hall_price,h.img1 FROM `wishlist_hall` as wh join `hall` as h on wh.hall_id = h.hall_id WHERE wh.user_id=%s;''',(userId,))
	savedHall=cursor.fetchall()
	print("saved hall list by user with user id",userId)
	print(savedHall)
	cursor.close()
	
	# selecting vehicle whishlist of user
	cursor=mysql.connection.cursor()
	cursor.execute('''SELECT wh.id ,wh.user_id ,v.id,v.Location,v.district ,v.vehicle_price,v.img1 FROM `wishlist_vehicle` as wh join `vechile` as v on wh.vehicle_id = v.id WHERE wh.user_id=%s;''',(userId,))
	savedVehicle=cursor.fetchall()
	print("saved hall list by user with user id",userId)
	print(savedVehicle)
	cursor.close()

	user=getUserEmailFromSession()
	return render_template('myProfilePage.html',result={'user':user,'userInfo':userInfo,'savedHall':savedHall,'savedVehicle':savedVehicle,'savedFlat':savedFlat})



@app.route("/profile")
def profile():
	loged_in_user=None
	if session.get('userId'):
		loged_in_user=session["userId"]
		cursor=mysql.connection.cursor()
		cursor.execute('''SELECT user_id,first_name,last_name,email,address,district,phone_number,image_path FROM `users` where `user_id`=%s;''',(loged_in_user,))
		user=cursor.fetchone()
		#print(user,title, difficulty,total_cost)
		print(user)
		cursor.close()
		print(loged_in_user)
	return render_template('profile.html',result={'loged_in_user':user})

	# return render_template("profile.html")



@app.route("/changeProfile", methods=['POST'])
def changePic():

	UPLOAD_FOLDER ='static/img/profile/'

	#UPLOAD_FOLDER ='static/'
	app.secret_key ="secret key"
	app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
	app.config['MAX_CONTENT_LENGTH']=16 * 1024 * 1024

	ALLOWED_EXTENSIONS =set(['png','jpg','jpeg','gif','JFIF'])
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file=request.files['file']
	if file.filename == '':
		flash("no image selected for uploading")
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename =secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('image sucessfully uploaded')	
		
		path="static/img/profile/"+str(filename)
		print(path)
		cursor =mysql.connection.cursor()
		cursor.execute("UPDATE `users` SET `image_path`=%s WHERE `email`=%s",(path,session['email'],)); 
		mysql.connection.commit()
		cursor.close()


		return redirect("profile")
	else:
		flash('Allowed image type are png, jpg,gif,jpeg')
		return redirect("profile")	

	return render_template("profile.html")


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/myRoom")
def myRoom():
	# continue from here
	# mark
	loged_in_user=getUserEmailFromSession()
	userId=getUserIdFromSession()
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM flat  WHERE user_id=%s;''',(userId,)) 
	room =cursor.fetchall()
	print("room of loged_in_user")
	print(room)
	cursor.close()
	return render_template('myRoom.html', result={'room':room,'loged_in_user':loged_in_user})


@app.route("/myHall")
def myHall():
	# continue from here
	# mark
	loged_in_user=getUserEmailFromSession()
	userId=getUserIdFromSession()
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM hall  WHERE user_id=%s;''',(userId,)) 
	allHall =cursor.fetchall()
	print("room of loged_in_user")
	print(allHall)
	cursor.close()
	return render_template('myHall.html', result={'allHall':allHall,'loged_in_user':loged_in_user})



@app.route("/myVehicle")
def myVehicle():
	# continue from here
	# mark
	loged_in_user=getUserEmailFromSession()
	userId=getUserIdFromSession()
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM vechile  WHERE user_id=%s;''',(userId,)) 
	vehicle =cursor.fetchall()
	print("room of loged_in_user")
	print(vehicle)
	cursor.close()
	return render_template('myVehicle.html', result={'vehicle':vehicle,'loged_in_user':loged_in_user})


@app.route("/room")
def room():
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM flat;''')
	room =cursor.fetchall()
	loged_in_user=None
	if session.get('email'):
		loged_in_user=session['email']

	print(room)
	cursor.close()
	return render_template("room.html",result={'room':room,'loged_in_user':loged_in_user})


# room details data form id for room details
@app.route('/roomDetails/<int:flatId>')
def getRoomId(flatId):
	# code for getting flat details of id = flatId 
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT f.flat_id ,f.flat_title ,f.address ,f.flat_district,f.upload_date, f.upload_time ,f.price ,f.area ,f.no_room ,f.floor ,f.parking_car ,f.parking_bike ,f.description ,f.img1_path,f.img2_path,f.img3_path, u.first_name , u.phone_number,u.email  FROM `flat` as f join `users` as u on f.user_id = u.user_id WHERE f.flat_id=%s;''',(flatId,))
	room = cursor.fetchone()
	print("value of room")
	print(room)
	cursor.close()

	# code for getting flat similar to above flat  
	room_address=room[2]
	room_district=room[3]
	room_price=room[6]
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `flat` WHERE address=%s or flat_district=%s or price=%s;''',(room_address,room_district,room_price,))
	other_similar_flat = cursor.fetchmany(6)
	print("other similar flat to show in roomDetails page")
	print(other_similar_flat)
	cursor.close()
	


	# code for getting flat location map 
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `flat_map` WHERE flat_id=%s;''',(flatId,))
	mapValue = cursor.fetchone()
	print("location of flat is here")
	print(mapValue)
	cursor.close()
	

	loged_in_user=getUserEmailFromSession()
	return render_template('roomDetails.html', result={"room":room,"loged_in_user":loged_in_user,'mapValue':mapValue,'other_similar_flat':other_similar_flat})

# my room details
@app.route('/myRoomDetails/<int:flatId>')
def myRoomDeatailsId(flatId):
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT f.flat_id ,f.flat_title ,f.address ,f.flat_district,f.upload_date, f.upload_time ,f.price ,f.area ,f.no_room ,f.floor ,f.parking_car ,f.parking_bike ,f.description ,f.img1_path,f.img2_path,f.img3_path, u.first_name , u.phone_number  FROM `flat` as f join `users` as u on f.user_id = u.user_id WHERE f.flat_id=%s;''',(flatId,))
	room = cursor.fetchone()
	print("value of room")
	print(room)
	cursor.close()

# code for getting flat location map 
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `flat_map` WHERE flat_id=%s;''',(flatId,))
	mapValue = cursor.fetchone()
	print("location of flat is here")
	print(mapValue)
	cursor.close()

	user=getUserIdFromSession()
	
	# cursor = mysql.connection.cursor()
	# cursor.execute('''SELECT * FROM `flat` WHERE flat_id=%s;''',(flatId,))
	# roomomdetails = cursor.fetchall()
	# # print("value of roomdetails")
	# print(roomdetails)
	# cursor.close()
	# return render_template('roomDetails.html', result={"room":room,"roomdetails":roomdetails})
	return render_template('myRoomDetails.html', result={"room":room,'mapValue':mapValue,'user':user})


# my hall details   z
@app.route('/myHallDetails/<int:hallId>')
def myHallDetailsId(hallId):
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT h.hall_id ,h.hall_name ,h.hall_address,h.hall_district ,h.hall_price,h.contact_number,h.person_capacity ,h.parking_2wheel,h.parking_4wheel,h.hall_description,h.meeting_hall ,h.conference_hall ,h.party_palace,h.upload_date ,h.upload_time ,h.img1,h.img2,h.img3, u.first_name , u.phone_number  FROM `hall` as h join `users` as u on h.user_id = u.user_id WHERE h.hall_id=%s;''',(hallId,))
	hall = cursor.fetchone()
	print("value of room")
	print(hall)
	cursor.close()


	# code for getting vehicle location map 
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `hall_map` WHERE hall_id=%s;''',(hallId,))
	mapValue = cursor.fetchone()
	print("location of flat is here")
	print(mapValue)
	cursor.close()
	user=getUserIdFromSession()
	return render_template('myHallDetails.html', result={"hall":hall,'mapValue':mapValue,'user':user})


# my hall details   
@app.route('/myVehicleDetails/<int:vehicleId>')
def myVehicleDetailsId(vehicleId):
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT v.id ,v.vehicle_number ,v.Location ,v.district,v.vehicle_company,v.vehicle_model ,v.vehicle_color ,v.vehicle_engine,v.vehicle_mileage ,v.vehicle_personCapacity ,v.vehicle_price ,v.vehicle_category ,v.fuel_type ,v.description,v.upload_date,v.img1,v.img2,v.img3 , u.first_name , u.phone_number  FROM `vechile` as v join `users` as u on v.user_id = u.user_id WHERE v.id=%s;''',(vehicleId,))
	vehicle = cursor.fetchone()
	print("value of room")
	print(vehicle)
	cursor.close()


# code for getting vehicle location map 
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `vehicle_map` WHERE vehicle_id=%s;''',(vehicleId,))
	mapValue = cursor.fetchone()
	print("location of flat is here")
	print(mapValue)
	cursor.close()
	user=getUserIdFromSession()
	return render_template('myVehicleDetails.html', result={"vehicle":vehicle,'mapValue':mapValue,'user':user})


#  code for saving flat in whishlist
@app.route('/saveFlat/<int:roomId>')
def saveFlat(roomId):
	userId=getUserIdFromSession()

	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT * FROM `wishlist_flat` WHERE user_id=%s  and flat_id=%s ;''',(userId,roomId,))
	value = cursor.fetchone()
	cursor.close()
	if value:
		flash('Already Saved in wishlist')
	else:	
		cursor = mysql.connection.cursor()  
		cursor.execute('''INSERT INTO wishlist_flat VALUES(null,%s,%s)''',(userId,roomId)) 
		mysql.connection.commit()
		cursor.close()
		flash('Saved in wishlist')
	return redirect(url_for('getRoomId',flatId=roomId))

#  code for saving flat in whishlist
@app.route('/saveVehicle/<int:vehicleId>')
def saveVehicle(vehicleId):
	userId=getUserIdFromSession()
	print("userId ",userId)
	print("vehicleId ",vehicleId)


	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT * FROM `wishlist_vehicle` WHERE user_id=%s  and vehicle_id=%s ;''',(userId,vehicleId,))
	value = cursor.fetchone()
	cursor.close()
	print("value in database ",value)
	if value:
		flash('Already Saved in wishlist')
	else:	
		cursor = mysql.connection.cursor()  
		cursor.execute('''INSERT INTO `wishlist_vehicle` VALUES(null,%s,%s)''',(userId,vehicleId)) 
		mysql.connection.commit()
		cursor.close()
		flash('Saved in wishlist')
	return redirect(url_for('getVehicleId',vehicleId=vehicleId))

#  code for saving hall in whishlist
@app.route('/saveHall/<int:hallId>')
def saveHall(hallId):
	userId=getUserIdFromSession()

	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT * FROM `wishlist_hall` WHERE user_id=%s  and hall_id=%s ;''',(userId,hallId,))
	value = cursor.fetchone()
	cursor.close()
	if value:
		flash('Already Saved in wishlist')
	else:	
		cursor = mysql.connection.cursor()  
		cursor.execute('''INSERT INTO wishlist_hall VALUES(null,%s,%s)''',(userId,hallId)) 
		mysql.connection.commit()
		cursor.close()
		flash('Saved in wishlist')
	return redirect(url_for('getHallId',hallId=hallId))



@app.route("/addRoom")
def addRoom():
	loged_in_user=getUserEmailFromSession()

	return render_template("addRoom.html",result={'loged_in_user':loged_in_user})

@app.route("/editRoom/<int:flatId>")
def editRoom(flatId):
		# roomrsor.execute('''SELECT * FROM `flat` WHERE flat_id=%s;''',(flatId,))
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT * FROM `flat` WHERE flat_id=%s;''',(flatId,))
	room = cursor.fetchone()
	print("value of vehicle")
	print(room)
	cursor.close()
	loged_in_user=getUserEmailFromSession()

	return render_template("editRoom.html",result={'loged_in_user':loged_in_user,'room':room})


@app.route("/editVehicle/<int:vehicleId>")
def editVehicle(vehicleId):
		# roomrsor.execute('''SELECT * FROM `flat` WHERE flat_id=%s;''',(flatId,))
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT * FROM `vechile` WHERE id=%s;''',(vehicleId,))
	vehicle = cursor.fetchone()
	print("value of vehicle")
	print(vehicle)
	cursor.close()
	loged_in_user=getUserEmailFromSession()

	return render_template("editVehicle.html",result={'loged_in_user':loged_in_user,'vehicle':vehicle})





@app.route("/editHall/<int:hallId>")
def editHall(hallId):
		# roomrsor.execute('''SELECT * FROM `flat` WHERE flat_id=%s;''',(flatId,))
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT * FROM `hall` WHERE hall_id=%s;''',(hallId,))
	hall = cursor.fetchone()
	print("value of vehicle")
	print(hall)
	cursor.close()
	loged_in_user=getUserEmailFromSession()

	return render_template("editHall.html",result={'loged_in_user':loged_in_user,'hall':hall})






@app.route("/updateRoom/<int:flatId>",methods=['POST'])
def updateRoom(flatId):
	print("geting id")
	print(flatId)
	room_title=request.form['room_title']

	room_address=request.form['room_address']
	room_district=request.form['room_district']
	
	room_area=request.form['room_area']
	room_price=request.form['room_price']
	room_no=request.form['room_no']
	room_floor=request.form['room_floor']
	room_2wheel=request.form['room_2wheel']
	room_4wheel=request.form['room_4wheel']
	room_description=request.form['room_description']
	print(room_address)
	cursor =mysql.connection.cursor()
	cursor.execute("UPDATE `flat` SET `flat_title`=%s, `address`=%s,`flat_district`=%s,`price`=%s,`area`=%s,`no_room`=%s,`floor`=%s,`parking_car`=%s,`parking_bike`=%s,`description`=%s WHERE `flat_id`=%s",(room_title,room_address,room_district,room_price,room_area,room_no,room_floor,room_4wheel,room_2wheel,room_description,flatId,)); 
	mysql.connection.commit()
	cursor.close()

	flash('updated sucessfully...')
	return redirect(url_for('myRoomDeatailsId',flatId=flatId))		


@app.route("/updateHall/<int:hallId>",methods=['POST'])
def updateHall(hallId):
	print("geting id")
	print(hallId)
	


	hall_name=request.form['hall_name']
	hall_address=request.form['hall_address']
	hall_district=request.form['hall_district']

	hall_price=request.form['hall_price']
	contact_number=request.form['contact_number']
	person_capacity=request.form['person_capacity']
	parking_2wheel=request.form['parking_2wheel']
	parking_4wheel=request.form['parking_4wheel']
	hall_description=request.form['hall_description']
	
	category=request.form.getlist('category')
	if 'Meeting Hall' in category:
		cat1="Meeting Hall"
	else: 
		cat1="No" 	
	if 'Conference Hall' in category:
		cat2="Conference Hall"
	else: 
		cat2="No" 	
	if 'Party Palace' in category:
		cat3="Party Palace"
	else: 
		cat3="No" 	

	cursor =mysql.connection.cursor()
	cursor.execute("UPDATE `hall` SET `hall_name`=%s, `hall_address`=%s,`hall_district`=%s,`hall_price`=%s,`contact_number`=%s,`person_capacity`=%s,`parking_2wheel`=%s,`parking_4wheel`=%s,`hall_description`=%s,`meeting_hall`=%s,`conference_hall`=%s,`party_palace`=%s WHERE `hall_id`=%s",
		(hall_name,hall_address,hall_district,hall_price,contact_number,person_capacity,parking_2wheel,parking_4wheel,hall_description,cat1,cat2,cat3,hallId,)); 
	mysql.connection.commit()
	cursor.close()

	flash('updated sucessfully...')
	return redirect(url_for('myHallDetailsId',hallId=hallId))		


@app.route("/updateVehicle/<int:vehicleId>",methods=['POST'])
def updateVehicle(vehicleId):
	print("geting id")

	vehicle_no=request.form['vehicle_no']
	print(vehicle_no)

	vehicle_location=request.form['vehicle_location']
	print(vehicle_location)

	vehicle_district=request.form['vehicle_district']
	print(vehicle_district)

	vehicle_company=request.form['vehicle_company']
	print(vehicle_company)

	vehicle_model=request.form['vehicle_model']
	print(vehicle_model)
	vehicle_milage=request.form['vehicle_milage']
	print(vehicle_milage)
	vehicle_color=request.form['vehicle_color']
	print(vehicle_color)
	vehicle_engineCapacity=request.form['vehicle_engineCapacity']
	print(vehicle_engineCapacity)
	vehicle_personCapacity=request.form['vehicle_personCapacity']
	print(vehicle_personCapacity)
	vehicle_price=request.form['vehicle_price']
	print(vehicle_price)
	
	vehicle_description=request.form['vehicle_description']
	print(vehicle_description)
	fuel_type=request.form['fuel']
	print(fuel_type)
	category=request.form.get('vehicle_category')
	print(category)


	cursor =mysql.connection.cursor()
	cursor.execute("UPDATE `vechile` SET `vehicle_number`=%s, `Location`=%s,`district`=%s,`vehicle_company`=%s,`vehicle_model`=%s,`vehicle_color`=%s,`vehicle_engine`=%s,`vehicle_mileage`=%s,`vehicle_personCapacity`=%s,`vehicle_price`=%s,`vehicle_category`=%s,`fuel_type`=%s,`description`=%s WHERE `id`=%s",(vehicle_no,vehicle_location,vehicle_district,vehicle_company,vehicle_model,vehicle_color,                                         vehicle_engineCapacity,   vehicle_milage,vehicle_personCapacity,vehicle_price,category,fuel_type,vehicle_description,vehicleId,)); 
	mysql.connection.commit()
	cursor.close()

	flash('updated sucessfully...')
	return redirect(url_for('myVehicleDetailsId',vehicleId=vehicleId))		



@app.route("/addRoom",methods=['POST'])
def addsRoom():
	UPLOAD_FOLDER ='static/img/flat/'

	#UPLOAD_FOLDER ='static/'
	app.secret_key ="secret key"
	app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
	app.config['MAX_CONTENT_LENGTH']=16 * 1024 * 1024

	ALLOWED_EXTENSIONS =set(['png','jpg','jpeg','gif','JFIF'])

	room_title=request.form['room_title']

	room_address=request.form['room_address']
	room_district=request.form['room_district']
	
	room_area=request.form['room_area']
	room_price=request.form['room_price']
	room_no=request.form['room_no']
	room_floor=request.form['room_floor']
	room_2wheel=request.form['room_2wheel']
	room_4wheel=request.form['room_4wheel']
	room_description=request.form['room_description']
	
	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)
	files=request.files.getlist('files[]')
	file_names =[]
	for file in files:
		if file and allowed_file(file.filename):
			filename =secure_filename(file.filename)
			file_names.append("static/img/flat/"+filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			# return render_template("multiple_image.html")
		else:
			flash('Allowed image type are png, jpg,gif,jpeg')
			return redirect(request.url)	
	flash('flat sucessfully uploaded')
	# print("final list")
	# print(file_names)
	img0=file_names[0]
	# img1=file_names[1]
	# img2=file_names[2]
	length=len(file_names)
	print(len(file_names))
	if length>1:
		img1=file_names[1]
	else:
		img1= None
	if length>2:	
		img2=file_names[2]
	else:
		img2= None
	print(img1)
	print(img2)	
	
	date_time=datetime.now()
	date= date_time.date()
	time=date_time.time()
	print(date)
	print(time)

	userId=getUserIdFromSession()
	print("user id is")
	print(userId)

	cursor =mysql.connection.cursor()
	cursor.execute('''INSERT INTO flat VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(room_title,room_address,room_district,date,time,room_price,room_area,room_no,room_floor,room_4wheel,room_2wheel,room_description,img0,img1,img2,userId))
	mysql.connection.commit()
	cursor.close()
	loged_in_user=getUserEmailFromSession()
	return render_template("addRoom.html",result={'loged_in_user':loged_in_user})

# //////////////////////////////////////////////////////////////////////////////
@app.route("/roomDetails")
def roomDetails():
	return render_template("roomDetails.html")

@app.route("/vehicleDetails")
def vehicleDetails():
	value=None
	return render_template("vehicleDetails.html", result={'key':value})

# /////////////////////////////////////////////////////////////////////////////


@app.route("/vehicle")
def vehicle():
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM vechile;''')
	vehicle =cursor.fetchall()
	loged_in_user=None
	if session.get('email'):
		loged_in_user=session['email']
	print("here os the daata")
	print(vehicle)
	cursor.close()
	
	return render_template("vehicle.html",result={'vehicle':vehicle,'loged_in_user':loged_in_user})

@app.route("/addVehicle")
def addVehicle():
	loged_in_user=getUserEmailFromSession()

	return render_template("addVehicle.html",result={'loged_in_user':loged_in_user})


@app.route("/addVehicle",methods=['POST'])
def addsVehicle():
	UPLOAD_FOLDER ='static/img/vehicle/'

	#UPLOAD_FOLDER ='static/'
	app.secret_key ="secret key"
	app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
	app.config['MAX_CONTENT_LENGTH']=16 * 1024 * 1024

	ALLOWED_EXTENSIONS =set(['png','jpg','jpeg','gif','JFIF'])

	vehicle_no=request.form['vehicle_no']
	print(vehicle_no)

	vehicle_location=request.form['vehicle_location']
	print(vehicle_location)

	vehicle_district=request.form['vehicle_district']
	print(vehicle_district)

	vehicle_company=request.form['vehicle_company']
	print(vehicle_company)

	vehicle_model=request.form['vehicle_model']
	print(vehicle_model)

	vehicle_milage=request.form['vehicle_milage']
	print(vehicle_milage)

	vehicle_color=request.form['vehicle_color']
	print(vehicle_color)

	vehicle_engineCapacity=request.form['vehicle_engineCapacity']
	print(vehicle_engineCapacity)

	vehicle_personCapacity=request.form['vehicle_personCapacity']
	print(vehicle_personCapacity)

	vehicle_price=request.form['vehicle_price']
	
	print(vehicle_price)

	vehicle_description=request.form['vehicle_description']
	
	print(vehicle_description)


	fuel_type=request.form['fuel']
	print(fuel_type)



	category=request.form.get('vehicle_category')
	print(category)

	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)
	files=request.files.getlist('files[]')
	file_names =[]
	for file in files:
		if file and allowed_file(file.filename):
			filename =secure_filename(file.filename)
			file_names.append("static/img/vehicle/"+filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			# return render_template("multiple_image.html")
		else:
			flash('Allowed image type are png, jpg,gif,jpeg')
			return redirect(request.url)	
	flash('vehicle sucessfully uploaded')
	# print("final list")
	print(file_names)
	img0=file_names[0]
	# img1=file_names[1]
	# img2=file_names[2]
	length=len(file_names)
	print(len(file_names))
	if length>1:
		img1=file_names[1]
	else:
		img1= None
	if length>2:	
		img2=file_names[2]
	else:
		img2= None
	print(img1)
	print(img2)	
	
	date_time=datetime.now()
	date= date_time.date()
	time=date_time.time()
	print(date)
	print(time)
	userId=getUserIdFromSession()
	property_type ="vehicle"

	cursor =mysql.connection.cursor()
	cursor.execute('''INSERT INTO vechile VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(vehicle_no,vehicle_location,vehicle_district,vehicle_company,vehicle_model,vehicle_color,vehicle_engineCapacity,vehicle_milage,vehicle_personCapacity,vehicle_price,category,fuel_type,vehicle_description,date,time,img0,img1,img2,userId,property_type))
	mysql.connection.commit()
	cursor.close()
	loged_in_user=getUserEmailFromSession()

	return render_template("addVehicle.html",result={'loged_in_user':loged_in_user})

@app.route('/vehicleDetails/<int:vehicleId>')
def getVehicleId(vehicleId):
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT v.id ,v.vehicle_number ,v.Location ,v.district,v.vehicle_company,v.vehicle_model ,v.vehicle_color ,v.vehicle_engine,v.vehicle_mileage ,v.vehicle_personCapacity ,v.vehicle_price ,v.vehicle_category ,v.fuel_type ,v.description,v.upload_date,v.img1,v.img2,v.img3 , u.first_name , u.phone_number,u.email  FROM `vechile` as v join `users` as u on v.user_id = u.user_id WHERE v.id=%s;''',(vehicleId,))
	vehicle = cursor.fetchone()
	print("value of vehicle")
	print(vehicle)
	cursor.close()


	# code for getting vechicle similar to above vehicle  
	vehicle_address=vehicle[2]
	vehicle_district=vehicle[3]
	vehicle_company=vehicle[4]
	vehicle_price=vehicle[7]
	vehicle_category=vehicle[11]
	
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `vechile` WHERE Location=%s or district=%s or vehicle_company=%s or vehicle_price=%s or vehicle_category=%s;''',(vehicle_address,vehicle_district,vehicle_company,vehicle_price,vehicle_category,))
	other_similar_vehicle = cursor.fetchmany(6)
	print("other similar flat to show in vehicleDetails page")
	print(other_similar_vehicle)
	cursor.close()
	



	# code for getting vehicle location map 
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `vehicle_map` WHERE vehicle_id=%s;''',(vehicleId,))
	mapValue = cursor.fetchone()
	print("location of flat is here")
	print(mapValue)
	cursor.close()

	loged_in_user=getUserEmailFromSession()
	return render_template('vehicleDetails.html', result={'loged_in_user':loged_in_user,"vehicle":vehicle,'mapValue':mapValue,'other_similar_vehicle':other_similar_vehicle})

@app.route('/hallDetails/<int:hallId>')
def getHallId(hallId):
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT h.hall_id ,h.hall_name ,h.hall_address,h.hall_district ,h.hall_price,h.contact_number,h.person_capacity ,h.parking_2wheel,h.parking_4wheel,h.hall_description,h.meeting_hall ,h.conference_hall ,h.party_palace,h.upload_date ,h.upload_time ,h.img1,h.img2,h.img3, u.first_name , u.phone_number,u.email  FROM `hall` as h join `users` as u on h.user_id = u.user_id WHERE h.hall_id=%s;''',(hallId,))
	hall = cursor.fetchone()
	print("value of vehicle for vehicle details")
	print(hall)
	cursor.close()


	# code for getting vechicle similar to above vehicle  
	hall_address=hall[2]
	hall_district=hall[3]
	hall_price=hall[4]
	
	
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `hall` WHERE hall_address=%s or hall_district=%s or hall_price =%s ;''',(
		hall_address,hall_district,hall_price,))
	other_similar_hall = cursor.fetchmany(6)
	print("other similar flat to show in vehicleDetails page..................")
	print(other_similar_hall)
	cursor.close()

	# code for getting hall location map 
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `hall_map` WHERE hall_id=%s;''',(hallId,))
	mapValue = cursor.fetchone()
	print("location of flat is here")
	print(mapValue)
	cursor.close()
	


	loged_in_user=getUserEmailFromSession()
	return render_template('hallDetails.html', result={'loged_in_user':loged_in_user,"hall":hall,'mapValue':mapValue,'other_similar_hall':other_similar_hall})


@app.route('/deleteHall/<int:hallId>')
def getHallIdDelete(hallId):
	print(hallId)
	cursor = mysql.connection.cursor()  
	cursor.execute('''DELETE FROM `hall`  WHERE hall_id = %s;''',(hallId,))
	mysql.connection.commit()
	flash("Deleted sucessfully..")
	cursor.close()
	# return "delete sucessfullys"
	return redirect(url_for('myHall'))


@app.route('/deleteVehicle/<int:vehicleId>')
def getVehicleIdDelete(vehicleId):
	print(vehicleId)
	cursor = mysql.connection.cursor()  
	cursor.execute('''DELETE FROM `vechile`  WHERE id = %s;''',(vehicleId,))
	mysql.connection.commit()
	flash("Deleted sucessfully..")
	cursor.close()
	# return "delete sucessfullys"
	return redirect(url_for('myVehicle'))



@app.route('/deleteFlat/<int:flatId>')
def getFlatIdDelete(flatId):
	print(flatId)
	cursor = mysql.connection.cursor()  
	cursor.execute('''DELETE FROM `flat`  WHERE flat_id = %s;''',(flatId,))
	mysql.connection.commit()
	flash("Deleted sucessfully..")
	cursor.close()
	# return "delete sucessfullys"
	return redirect(url_for('myRoom'))


# @app.route('/deleteVehicle/<int:vehicleId>')
# def getVehicleIdDelete(vehicleId):
# 	print(vehicleId)
# 	cursor = mysql.connection.cursor()  
# 	cursor.execute('''DELETE FROM `vechile`  WHERE id = %s;''',(vehicleId,))
# 	mysql.connection.commit()
# 	flash("Deleted sucessfully..")
# 	cursor.close()
# 	# return "delete sucessfullys"
# 	return redirect(url_for('vehicle'))



@app.route("/hall")
def hall():
	cursor =mysql.connection.cursor()
	cursor.execute('''SELECT * FROM hall;''')
	allHall =cursor.fetchall()
	cursor.close()
	print(allHall)
	loged_in_user=None
	if session.get('email'):
		loged_in_user=session['email']

	return render_template("hall.html",result={'allHall':allHall,'loged_in_user':loged_in_user})

	# return render_template("hall.html")
	 
@app.route("/addHall")
def addHall():
	loged_in_user=getUserEmailFromSession()

	return render_template("addHall.html",result={'loged_in_user':loged_in_user})


# @app.route('/registerHall',methods=['POST'])
@app.route('/addHall',methods=['POST'])
def addsHall():

	UPLOAD_FOLDER ='static/img/hall/'

	#UPLOAD_FOLDER ='static/'
	app.secret_key ="secret key"
	app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
	app.config['MAX_CONTENT_LENGTH']=16 * 1024 * 1024

	ALLOWED_EXTENSIONS =set(['png','jpg','jpeg','gif','JFIF'])
	

	hall_name=request.form['hall_name']
	hall_address=request.form['hall_address']
	hall_district=request.form['hall_district']

	hall_price=request.form['hall_price']
	contact_number=request.form['contact_number']
	person_capacity=request.form['person_capacity']
	parking_2wheel=request.form['parking_2wheel']
	parking_4wheel=request.form['parking_4wheel']
	hall_description=request.form['hall_description']
	# hall_description=hall_description.split('\n')
	print(hall_description)	
	category=request.form.getlist('category')
	if 'Meeting Hall' in category:
		cat1="Meeting Hall"
	else: 
		cat1="No" 	
	if 'Conference Hall' in category:
		cat2="Conference Hall"
	else: 
		cat2="No" 	
	if 'Party Palace' in category:
		cat3="Party Palace"
	else: 
		cat3="No" 	

	# cat1=category[0]
	# cat2=category[1]
	# cat3=category[2]
	
	# print(cat1 ,cat2 ,cat3)

	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)
	files=request.files.getlist('files[]')
	file_names =[]
	for file in files:
		if file and allowed_file(file.filename):
			filename =secure_filename(file.filename)
			file_names.append("static/img/hall/"+filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			# return render_template("multiple_image.html")
		else:
			flash('Allowed image type are png, jpg,gif,jpeg')
			return redirect(request.url)	
	flash('hall sucessfully uploaded')
	# print("final list")
	print(file_names)
	img0=file_names[0]
	length=len(file_names)
	print(len(file_names))
	if length>1:
		img1=file_names[1]
	else:
		img1= None
		img2=None
	if length>2:	
		img2=file_names[2]
	else:
		img2= None
	print(img1)
	print(img2)	
		
	date_time=datetime.now()
	date= date_time.date()
	time=date_time.time()
	loged_in_user=getUserEmailFromSession()
	userId=getUserIdFromSession()

	print(date)
	print(time)
	property_type="hall"
	print(property_type)

	cursor =mysql.connection.cursor()
	cursor.execute('''INSERT INTO hall VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(hall_name,hall_address,hall_district,hall_price,contact_number,person_capacity,parking_2wheel,parking_4wheel,hall_description,cat1,cat2,cat3,date,time,img0,img1,img2,userId,property_type))
	mysql.connection.commit()
	cursor.close()
	# cursor =mysql.connection.cursor()
	# cursor.execute('''INSERT INTO hall VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(hall_name,hall_address,hall_district,hall_price,contact_number,person_capacity,parking_2wheel,parking_4wheel,hall_description,cat1,cat2,cat3,date,time,img0,img1,img2,userId))
	# mysql.connection.commit()
	# cursor.close()
	loged_in_user=getUserEmailFromSession()

	return render_template('addHall.html',result={'loged_in_user':loged_in_user})


# admin section

@app.route("/user")
def user():
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT user_id,first_name,last_name,email,address,district,phone_number FROM users''')

	userList=cursor.fetchall()
	cursor.close()
	# print("here is the vlaue of ")
	print(userList)


	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT COUNT(user_id) FROM `users` ;''')
	count_user=cursor.fetchone()
	# count_room=count_room[0]
	cursor.close()
	print('no of user ',count_user)

	loged_in_user=getUserIdFromSession()



	
	# return "user"
	return render_template('user.html',result={'loged_in_user':loged_in_user,'userList':userList,'count_user':count_user})

# link
@app.route("/adminDashboard")
def adminDashboard():
	if session.get('email'):
		user=session['email']

		count_user=getTotalUser()
		count_flat=getTotalFlat()
		count_vehicle=getTotalVehicle()
		count_hall=getTotalHall()
		sixFlat=getSixFlat()
		sixVehicle=getSixVehicle()
		sixHall=getSixHall()
		count_booked_vehicle=getTotalBookedVehicle()
		count_booked_hall=getTotalBookedHall()
		

	return render_template('adminDashboard.html',result={'user':user,'count_user':count_user,'count_flat':count_flat,'count_vehicle':count_vehicle,'count_hall':count_hall,'sixFlat':sixFlat,'sixVehicle':sixVehicle,'sixHall':sixHall,'count_booked_vehicle':count_booked_vehicle,'count_booked_hall':count_booked_hall})

@app.route("/searchPage")
def searchPage():
	return render_template('searchPage.html',result={'user':user})


# search code
@app.route("/searchText",methods=['GET','POST'])
def searchText():

	hall_name=request.form['hall_name']+'%'
	print(hall_name)
	hall_name=hall_name.strip()
	# code for flat searching
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `flat` where flat_title like %s or address like %s or flat_district like %s or price like %s or no_room like %s   ;''',(hall_name,hall_name,hall_name,hall_name,hall_name,))
	flatList=cursor.fetchall()
	cursor.close()
	
	print(flatList)
	
	# code for flat searching
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `vechile` where vehicle_company like %s;''',(hall_name,))
	vehicleList=cursor.fetchall()
	cursor.close()
	print(vehicleList)
	
	# code for flat searching
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `hall` where hall_name like %s or hall_address like %s or hall_district like %s or hall_price like %s or meeting_hall like %s or conference_hall like %s or party_palace  like %s;''',(hall_name,hall_name,hall_name,hall_name,hall_name,hall_name,hall_name,))
	hallList=cursor.fetchall()
	cursor.close()
	print(vehicleList)
	
	searchResult=None
	user=getUserEmailFromSession()
	# return "searh page"
	return render_template('searchPage.html',result={'user':user,'flatList':flatList,'vehicleList':vehicleList,'hallList':hallList})


# code to display search page for room
@app.route("/searchRoomPage")
def searchRoomPage():
	user=getUserEmailFromSession()
	return render_template('searchRoomPage.html' ,result={'user':user}) 

# code to display search page for vehicle
@app.route("/searchVehiclePage")
def searchVehiclePage():
	user=getUserEmailFromSession()
	return render_template('searchVehiclePage.html' ,result={'user':user}) 

# code to display search page for hall
@app.route("/searchHallPage")
def searchHallPage():
	user=getUserEmailFromSession()	
	return render_template('searchHallPage.html' ,result={'user':user}) 

# search code for room
@app.route("/searchFlat",methods=['GET','POST'])
def searchFlat():

	hall_name='%'+request.form['hall_name']+'%'
	print(hall_name)
	hall_name=hall_name.strip()
	# code for flat searching
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `flat` where flat_title like %s or address like %s or flat_district like %s or price like %s or no_room like %s   ;''',(hall_name,hall_name,hall_name,hall_name,hall_name,))
	flatList=cursor.fetchall()
	cursor.close()
	user=getUserEmailFromSession()
	return render_template('searchRoomPage.html',result={'user':user,'flatList':flatList})


# filter search code for room
@app.route("/filterSearchFlat",methods=['GET','POST'])
def filterSearchFlat():

	address='%'+request.form['address']+'%'
	district='%'+request.form['district']+'%'
	no_room='%'+request.form['no_room']+'%'
	price_from=request.form['price_from']+'%'
	price_to=request.form['price_to']+'%'
	
	# address=request.form['address']+'%'
	# district=request.form['district']
	# no_room=request.form['no_room']	
	# price_from=request.form['price_from']+'%'
	# price_to=request.form['price_to']+'%'
	

	address=address.strip()
	district=district.strip()
	no_room=no_room.strip()
	price_from=price_from.strip()
	price_to=price_to.strip()

	print(address) 
	print(district) 

	print(no_room) 

	print(price_from) 
	print(price_to) 

	# hall_name=hall_name.strip()
	# # code for flat searching
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `flat` where address like %s and flat_district like %s and  no_room like %s and price between  %s and %s;''',(address,district,no_room,price_from,price_to,))
	flatList=cursor.fetchall()
	print(flatList)
	cursor.close()
	user=getUserEmailFromSession()
	return render_template('searchRoomPage.html',result={'user':user,'flatList':flatList})



# search code for vehicle
@app.route("/searchVehicle",methods=['GET','POST'])
def searchVehicle():

	hall_name='%'+request.form['hall_name']+'%'
	print(hall_name)
	hall_name=hall_name.strip()
	
 	# code for flat searching
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `vechile` where vehicle_company like %s;''',(hall_name,))
	vehicleList=cursor.fetchall()
	cursor.close()
	print(vehicleList)	
	user=getUserEmailFromSession()
	return render_template('searchVehiclePage.html',result={'user':user,'vehicleList':vehicleList})






# filter search code for vehicle
@app.route("/filterSearchVehicle",methods=['GET','POST'])
def filterSearchVehicle():

	# address district vehicle_category vehicle_company vehicle_engineCapacity vehicle_milage  price_from price_to
	address='%'+request.form['address']+'%'
	district='%'+request.form['district']+'%'
	vehicle_category='%'+request.form['vehicle_category']+'%'
	vehicle_company='%'+request.form['vehicle_company']+'%'
	vehicle_engineCapacity='%'+request.form['vehicle_engineCapacity']+'%' 
	vehicle_milage='%'+request.form['vehicle_milage']+'%'  
	price_from=request.form['price_from'] 
	price_to=request.form['price_to']

	
	address=address.strip()
	district=district.strip()
	vehicle_category=vehicle_category.strip()
	vehicle_company=vehicle_company.strip()
	vehicle_engineCapacity=vehicle_engineCapacity.strip()
	vehicle_milage=vehicle_milage.strip()
	price_from=price_from.strip()
	price_to=price_to.strip()


	print(address) 
	print(district) 
	print(vehicle_category) 
	print(vehicle_company) 
	print(vehicle_engineCapacity) 
	print(vehicle_milage) 
	print(price_from) 
	print(price_to) 

	# hall_name=hall_name.strip()
	# # code for flat searching
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `vechile` where Location like %s and district like %s and vehicle_category = %s and vehicle_company like %s and vehicle_engine like %s and vehicle_mileage like %s and vehicle_price between  %s and %s;''',(address, district, vehicle_category, vehicle_company, vehicle_engineCapacity, vehicle_milage, price_from, price_to,))
	vehicleList=cursor.fetchall()
	print(vehicleList)
	cursor.close()
	user=getUserEmailFromSession()
	return render_template('searchVehiclePage.html',result={'user':user,'vehicleList':vehicleList})









# search code for hall
@app.route("/userSearch",methods=['GET','POST'])
def userSearch():

	user='%'+request.form['hall_name']+'%'
	print(user)
	user=user.strip()
	
 	
	# code for flat searching
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `users` where user_id like %s or first_name like %s or last_name like %s or email like %s or address like %s or district like %s or phone_number like %s ;''',(user,user,user,user,user,user,user,))
	userList=cursor.fetchall()
	cursor.close()
	print(userList)
	
# 	searchResult=None
# 	user=getUserEmailFromSession()
# 	# return "searh page"
	return render_template('searchUserPage.html',result={'user':user,'userList':userList})








# search code for hall
@app.route("/searchHall",methods=['GET','POST'])
def searchHall():

	hall_name='%'+request.form['hall_name']+'%'
	print(hall_name)
	hall_name=hall_name.strip()
	
 	
	# code for flat searching
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `hall` where hall_name like %s or hall_address like %s or hall_district like %s or hall_price like %s or meeting_hall like %s or conference_hall like %s or party_palace  like %s;''',(hall_name,hall_name,hall_name,hall_name,hall_name,hall_name,hall_name,))
	hallList=cursor.fetchall()
	cursor.close()
	print(hallList)
	
# 	searchResult=None
	user=getUserEmailFromSession()
# 	# return "searh page"
	return render_template('searchHallPage.html',result={'user':user,'hallList':hallList})


# filter search code for vehicle
@app.route("/filterSearchHall",methods=['GET','POST'])
def filterSearchHall():

	# address district vehicle_category vehicle_company vehicle_engineCapacity vehicle_milage  price_from price_to
	name='%'+request.form['name']+'%'
	address='%'+request.form['address']+'%'
	district='%'+request.form['district']+'%'
	hall_category='%'+request.form.get('hall_category')+'%'
	price_from=request.form['price_from'] 
	price_to=request.form['price_to']

	name=name.strip()
	address=address.strip()
	district=district.strip()
	hall_category=hall_category.strip()
	price_from=price_from.strip()
	price_to=price_to.strip()


	# # code for flat searching
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `hall` where hall_name like %s and meeting_hall like %s or conference_hall like %s or party_palace like %s and hall_address like %s and hall_district like %s and hall_price between  %s and %s;''',(name, hall_category, hall_category, hall_category,address, district, price_from, price_to,))
	hallList=cursor.fetchall()
	print(hallList)
	cursor.close()
	user=getUserEmailFromSession()
	return render_template('searchHallPage.html',result={'user':user,'hallList':hallList})






# search code
@app.route('/user_info_for_admin_page/<int:userId>')
def userInfoForAdminPage(userId):
	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT * FROM `users` where user_id = %s;''',(userId,))
	userInfo=cursor.fetchone()
	cursor.close()
	print(userInfo)


	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT COUNT(flat_id) FROM `flat` where user_id = %s;''',(userId,))
	count_room=cursor.fetchone()
	count_room=count_room[0]
	cursor.close()
	print('no of room ',count_room)


	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT COUNT(id) FROM `vechile` where user_id = %s;''',(userId,))
	count_vehicle=cursor.fetchone()
	count_vehicle=count_vehicle[0]
	cursor.close()
	print('no of vehicle ',count_vehicle)

	cursor =mysql.connection.cursor()
	resp=cursor.execute('''SELECT COUNT(hall_id) FROM `hall` where user_id = %s;''',(userId,))
	count_hall=cursor.fetchone()
	count_hall=count_hall[0]
	cursor.close()
	print('no of hall ',count_hall)
# SELECT COUNT(column_name)
# FROM table_name
# WHERE condition;	
	loged_in_user=getUserEmailFromSession()
	

	return render_template('userProfileInfoPage.html',result={'loged_in_user':loged_in_user,'userInfo':userInfo,'count_room':count_room,'count_vehicle':count_vehicle,'count_hall':count_hall})	



# function to get user id  from session

def getUserIdFromSession():
	loged_in_user=None
	if session.get('userId'):
		loged_in_user=session["userId"]
	return loged_in_user			

# function to get user email from session 

def getUserEmailFromSession():
	loged_in_user=None
	if session.get('email'):
		loged_in_user=session['email']
	return loged_in_user			




#  new section



@app.route('/khalti-requestH/<int:hallId>')
def khaltiRequestH(hallId):
    # f_name = request.form['fname']
    # l_name = request.form['lname']
    # email = request.form['email']
    # phone = request.form['phone']
    # address = request.form['address']
    booking_total = 150
    # print(f_name, l_name, phone, email, address, booking_total)
    print(hallId)
    cursor =mysql.connection.cursor()
    resp=cursor.execute('''SELECT hall_id,hall_address,hall_district,hall_price,hall_name,user_id,property_type FROM `hall` where hall_id = %s;''',(hallId,))
    booking_total=cursor.fetchone()
    print(booking_total)
    customerId=getUserIdFromSession()   
    print(customerId)
    cursor.close()

    # getC('hall')
    return render_template('khaltirequest.html',result={'booking_total':booking_total,'customerId':customerId})


@app.route('/khalti-requestV/<int:vehicleId>')
def khaltiRequestV(vehicleId):
    # f_name = request.form['fname']
    # l_name = request.form['lname']
    # email = request.form['email']
    # phone = request.form['phone']
    # address = request.form['address']
    booking_total = 150
    # print(f_name, l_name, phone, email, address, booking_total)
    print(vehicleId)
    cursor =mysql.connection.cursor()
    resp=cursor.execute('''SELECT id,Location,district,vehicle_price,vehicle_category,user_id,property_type FROM `vechile` where id = %s;''',(vehicleId,))
    booking_total=cursor.fetchone()
    print('some information  ',booking_total)
    customerId=session.get('userId')   
    print(customerId)
    cursor.close()

    return render_template('khaltirequest.html',result={'booking_total':booking_total,'customerId':customerId})

@app.route('/khaltiVerify/')
def khaltiVerifyView():
    token = request.args.get("token")
    amount = request.args.get("amount")
    b_id = request.args.get("product_identity")
    print(token, amount, b_id)

    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
        "token": token,
        "amount": amount
    }
    headers = {
        "Authorization": "Key test_secret_key_5cb619c5baea4a74be3ffdd69f10ad31"
        }

   # order_obj = Order.objects.get(id=o_id)

    response = requests.post(url, payload, headers=headers)
    resp_dict = response.json()
    print(resp_dict)
    if resp_dict.get("idx"):
        success = True
        #order_obj.payment_completed = True
        #order_obj.save()
    else:
        success = False
    data = {
        "success": success
        }
    return jsonify(data)


# @ app.route('/book')
# def checkout():
# 	print(x)
#     return render_template('checkout.html')


@ app.route('/bill/<string:value>')
def bill(value):
	print(value)
	category=value[0]
	idValue=value[1:]
	print('___category___ ',category)
	print('___idValue____  ',idValue)

	booked_date=session.get('startdate')
		
	if category=='v': 

	# vehcile ko code
			
		
		cursor =mysql.connection.cursor()
		resp=cursor.execute('''SELECT * FROM `vechile` where id = %s;''',(idValue,))
		details=cursor.fetchone()
		cursor.close()

		print('...................................................................')
		print('vehicle details',details)

		print(' assigning value in varialbe varialble section ')
		vehicle_id=details[0]
		vehicle_number=details[1]
		vehicle_address=details[2]
		vehicle_district=details[3]
		vehicle_company=details[4]
		vehicle_price=details[7]
		vehicle_category=details[11]
		owner_id=details[19]


		# gettin owner details form owner_id
		cursor =mysql.connection.cursor()
		resp=cursor.execute('''SELECT * FROM `users` where user_id = %s;''',(owner_id,))
		owner_detail=cursor.fetchone()
		cursor.close()

		print('...................................................................')
		print('owner details',owner_detail)

		onwer_fname=owner_detail[1]
		onwer_lname=owner_detail[2]
		onwer_address=owner_detail[4]
		onwer_district=owner_detail[5]
		owner_contact=owner_detail[6]
		owner_email=owner_detail[3]

		customer_id=getUserIdFromSession()
		print(customer_id)

		# gettin customer details form customer_id
		cursor =mysql.connection.cursor()
		resp=cursor.execute('''SELECT * FROM `users` where user_id = %s;''',(customer_id,))
		customer_detail=cursor.fetchone()
		cursor.close()
		print('...................................................................')
		print('customer details',customer_detail)

		customer_fname=customer_detail[1]
		customer_lname=customer_detail[2]
		customer_address=customer_detail[4]
		customer_district=customer_detail[5]
		customer_contact=customer_detail[6]
		customer_email=customer_detail[3]

		

		date_time=datetime.now()
		booked_on_date= date_time.date()
		print('date form system',booked_on_date)
		

		print('storing those value in varialbe in database')
		


		cursor =mysql.connection.cursor()
		cursor.execute('''INSERT INTO booked_vehicle_table VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(vehicle_id,vehicle_category,vehicle_number,vehicle_address,vehicle_district,vehicle_company,vehicle_price,owner_id,onwer_fname,onwer_lname,owner_contact,owner_email,customer_id,customer_fname,customer_lname,customer_contact,customer_email,booked_date,booked_on_date)) 
		mysql.connection.commit()
		cursor.close()
		
		print('inserted in table booked vehicle............................................')
		cursor =mysql.connection.cursor()
		resp=cursor.execute('''SELECT id,Location,district,vehicle_price,vehicle_category,user_id,property_type FROM `vechile` where id = %s;''',(idValue,))
		details_to_show_in_billPage=cursor.fetchone()
		print('some information  ',details_to_show_in_billPage)
		cursor.close()


	elif category=='h':
		print('inside h case')

	# hall ko code
		cursor =mysql.connection.cursor()
		resp=cursor.execute('''SELECT * FROM `hall` where hall_id = %s;''',(idValue,))
		details=cursor.fetchone()
		cursor.close()

		print('got details')

		hall_id=details[0]
		hall_name=details[1]
		hall_address=details[2]
		hall_district=details[3]
		hall_price=details[4]
		contact_number=details[5]
		owner_id=details[18]

		# gettin owner details form owner_id
		cursor =mysql.connection.cursor()
		resp=cursor.execute('''SELECT * FROM `users` where user_id = %s;''',(owner_id,))
		owner_detail=cursor.fetchone()
		cursor.close()

		print('...................................................................')
		print('owner details',owner_detail)


		onwer_fname=owner_detail[1]
		onwer_lname=owner_detail[2]
		onwer_address=owner_detail[4]
		onwer_district=owner_detail[5]
		owner_contact=owner_detail[6]
		owner_email=owner_detail[3]


		customer_id=getUserIdFromSession()
		print(customer_id)

		print('got customerId ',customer_id)

		# gettin customer details form customer_id
		cursor =mysql.connection.cursor()
		resp=cursor.execute('''SELECT * FROM `users` where user_id = %s;''',(customer_id,))
		customer_detail=cursor.fetchone()
		cursor.close()
		print('...................................................................')
		print('customer details',customer_detail)

		customer_fname=customer_detail[1]
		customer_lname=customer_detail[2]
		customer_address=customer_detail[4]
		customer_district=customer_detail[5]
		customer_contact=customer_detail[6]
		customer_email=customer_detail[3]

		


		# bookedon
		date_time=datetime.now()
		booked_on_date= date_time.date()
		print('date form system',booked_on_date)
		

		cursor =mysql.connection.cursor()
		cursor.execute('''INSERT INTO booked_hall_table VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(hall_id,hall_name,hall_address,hall_district,hall_price,owner_id,onwer_fname,onwer_lname,owner_contact,owner_email,customer_id,customer_fname,customer_lname,customer_contact,customer_email,booked_date,booked_on_date)) 
		mysql.connection.commit()
		cursor.close()
				
		print("section of last query")		
		cursor =mysql.connection.cursor()
		resp=cursor.execute('''SELECT hall_id,hall_address,hall_district,hall_price,hall_name,user_id,property_type FROM `hall` where hall_id = %s;''',(idValue,))
		details_to_show_in_billPage=cursor.fetchone()
		cursor.close()


	loged_in_user=getUserIdFromSession()



	return render_template('bill.html',result={'details_to_show_in_billPage':details_to_show_in_billPage,'loged_in_user':loged_in_user,'booked_date':booked_date})








@app.route('/dateV/<int:vehicleId>', methods=['GET','POST'])
def dateV(vehicleId):
	form = InfoForm()
	if form.validate_on_submit():
		session['startdate']=form.startdate.data

		# check booked date ........................................................
		cursor =mysql.connection.cursor()
		resp=cursor.execute('''SELECT * FROM `booked_vehicle_table` where booked_for = %s;''',(session.get('startdate'),))
		date_in_db=cursor.fetchone()
		cursor.close()

		if date_in_db:
			flash('Already Booked',session.get('startdate'))
			return render_template('datePage.html',form=form)
		else:	
			return redirect(url_for("khaltiRequestV",vehicleId=vehicleId))
	return render_template('datePage.html',form=form)



@app.route('/dateH//<int:hallId>', methods=['GET','POST'])
def dateH(hallId):
	form = InfoForm()
	if form.validate_on_submit():
		session['startdate']=form.startdate.data
		# check booked date ........................................................
		cursor =mysql.connection.cursor()
		resp=cursor.execute('''SELECT * FROM `booked_hall_table` where booked_for = %s;''',(session.get('startdate'),))
		date_in_db=cursor.fetchone()
		cursor.close()
		
		if date_in_db:
			flash('Already Booked',session.get('startdate'))
			return render_template('datePage.html',form=form)
		else:
			return redirect(url_for("khaltiRequestH",hallId=hallId))
	return render_template('datePage.html',form=form)



# map work from here
@ app.route('/showFlatMap/<int:roomId>')
def showFlatMap(roomId):

	# code for getting flat location map 
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `flat_map` WHERE flat_id=%s;''',(roomId,))
	mapValue = cursor.fetchone()
	print("location of flat is here")
	print(mapValue)
	cursor.close()
		
	lat=mapValue[1]
	lng=mapValue[2]
	print(lat)
	print(lng)
	return render_template('mapBox.html',result={'lat':lat,'lng':lng})


@ app.route('/showVehicleMap/<int:vehicleId>')
def showVehicleMap(vehicleId):

	# code for getting flat location map 
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `vehicle_map` WHERE vehicle_id=%s;''',(vehicleId,))
	mapValue = cursor.fetchone()
	print("location of flat is here")
	print(mapValue)
	cursor.close()
		
	lat=mapValue[1]
	lng=mapValue[2]
	print(lat)
	print(lng)
	return render_template('mapBox.html',result={'lat':lat,'lng':lng})



@ app.route('/showHallMap/<int:hallId>')
def showHallMap(hallId):

	# code for getting flat location map 
	cursor = mysql.connection.cursor()  
	cursor.execute('''SELECT  * FROM `hall_map` WHERE hall_id=%s;''',(hallId,))
	mapValue = cursor.fetchone()
	print("location of flat is here")
	print(mapValue)
	cursor.close()
		
	lat=mapValue[1]
	lng=mapValue[2]
	print(lat)
	print(lng)
	return render_template('mapBox.html',result={'lat':lat,'lng':lng})



@ app.route('/inputMap/<int:id>/<string:itemType>')
def inputMap(id,itemType):
	print('ID ==', id)
	print('type == ', itemType)
	return render_template('inputMap.html',id=id,itemType=itemType)

@ app.route('/saveInputMap/<int:id>/<string:itemType>',methods=['GET', 'POST'])
def saveInputMap(id,itemType):

	longitude=float(request.form['long'])
	latitude=float(request.form['lat'])
	print('longitude is =',longitude)
	print('latitude is =',latitude)
	if itemType=='flat':
		cursor =mysql.connection.cursor()
		cursor.execute('''INSERT INTO flat_map VALUES(NULL,%s,%s,%s)''',(latitude,longitude,id)) 
		mysql.connection.commit()
		cursor.close()
		return redirect(url_for("myRoomDeatailsId",flatId=id))

	elif itemType=='vehicle':
		cursor =mysql.connection.cursor()
		cursor.execute('''INSERT INTO vehicle_map VALUES(NULL,%s,%s,%s)''',(latitude,longitude,id)) 
		mysql.connection.commit()
		cursor.close()
		return redirect(url_for("myVehicleDetailsId",vehicleId=id))
		
	elif itemType=='hall':
		cursor =mysql.connection.cursor()
		cursor.execute('''INSERT INTO hall_map VALUES(NULL,%s,%s,%s)''',(latitude,longitude,id)) 
		mysql.connection.commit()
		cursor.close()
		return redirect(url_for("myHallDetailsId",hallId=id))



@app.route("/lat_lon_save/<int:roomId>", methods=['POST'])
def lat_lon_save(roomId):
	latitude=request.form['latitude']
	print(latitude)
	
	longitude=request.form['longitude']
	print(longitude)
	

	
	cursor =mysql.connection.cursor()
	cursor.execute('''INSERT INTO flat_map VALUES(null,%s,%s,%s)''',(latitude,longitude,roomId)) 
	mysql.connection.commit()
	cursor.close()
	flash('location sucessfully uploaded')	
	

	return redirect(url_for("myRoomDeatailsId",flatId=roomId))



#  booking details page (my booking).....................................
@app.route("/myBooking//<int:userId>")
def myBooking(userId):

	cursor = mysql.connection.cursor()  
	# cursor.execute('''SELECT f.flat_id ,f.flat_title ,f.address ,ar , u.first_name , u.phone_number,u.email  FROM `flat` as f join `users` as u on f.user_id = u.user_id WHERE f.flat_id=%s;''',(flatId,))	
	cursor.execute('''SELECT * FROM `booked_vehicle_table`  WHERE customer_id=%s;''',(userId,))
	valuesVehicle = cursor.fetchall()
	print("location of flat is here")
	print(valuesVehicle)
	cursor.close()

	cursor = mysql.connection.cursor()  
	# cursor.execute('''SELECT f.flat_id ,f.flat_title ,f.address ,ar , u.first_name , u.phone_number,u.email  FROM `flat` as f join `users` as u on f.user_id = u.user_id WHERE f.flat_id=%s;''',(flatId,))	
	cursor.execute('''SELECT * FROM `booked_hall_table`  WHERE customer_id=%s;''',(userId,))
	valuesHall = cursor.fetchall()
	print("location of flat is here")
	print(valuesHall)
	cursor.close()


	
	# return render_template('example.html',valuesVehicle=valuesVehicle,valuesHall=valuesHall)

	return render_template('myBooking.html',valuesVehicle=valuesVehicle,valuesHall=valuesHall)

#  end of my booking


#  booking details page (other booking).....................................
@app.route("/othtersBooking/<int:userId>")
def othtersBooking(userId):
	
	cursor = mysql.connection.cursor()  
	# cursor.execute('''SELECT f.flat_id ,f.flat_title ,f.address ,ar , u.first_name , u.phone_number,u.email  FROM `flat` as f join `users` as u on f.user_id = u.user_id WHERE f.flat_id=%s;''',(flatId,))	
	cursor.execute('''SELECT * FROM `booked_vehicle_table`  WHERE owner_id=%s;''',(userId,))
	valuesVehicle = cursor.fetchall()
	print("location of flat is here")
	print(valuesVehicle)
	cursor.close()

	cursor = mysql.connection.cursor()  
	# cursor.execute('''SELECT f.flat_id ,f.flat_title ,f.address ,ar , u.first_name , u.phone_number,u.email  FROM `flat` as f join `users` as u on f.user_id = u.user_id WHERE f.flat_id=%s;''',(flatId,))	
	cursor.execute('''SELECT * FROM `booked_hall_table`  WHERE owner_id=%s;''',(userId,))
	valuesHall = cursor.fetchall()
	print("location of flat is here")
	print(valuesHall)
	cursor.close()

	return render_template('booked_item_by_other.html',valuesVehicle=valuesVehicle,valuesHall=valuesHall)

#  end of other booking


# remove saved wishlist of user 
@app.route("/removeWishlist/<int:itemId>/<string:category>")
def removeWishlist(itemId,category):
	userId=getUserIdFromSession()

	if category=="flat":
		cursor = mysql.connection.cursor()  
		cursor.execute('''DELETE FROM `wishlist_flat`  WHERE flat_id = %s and user_id =%s;''',(itemId,userId,))
		mysql.connection.commit()
		flash("Removed sucessfully..")
		cursor.close()
	elif category=="vehicle":
		cursor = mysql.connection.cursor()  
		cursor.execute('''DELETE FROM `wishlist_vehicle`  WHERE vehicle_id = %s and user_id =%s;''',(itemId,userId,))
		mysql.connection.commit()
		flash("Removed sucessfully..")
		cursor.close()
	elif category=="hall":
		cursor = mysql.connection.cursor()  
		cursor.execute('''DELETE FROM `wishlist_hall`  WHERE hall_id = %s and user_id =%s;''',(itemId,userId,))
		mysql.connection.commit()
		flash("Removed sucessfully..")
		cursor.close()
	return redirect(url_for('myProfilePage'))
#  end  remove saved wishlist of user 


# # edit image of vehicle 
# @app.route("/changeVehicleImage/<int:vehicleId>/<int:imgNo>")
# def removeWishlist(vehicleId,imgNo):
# 	if imgNo == 1:
	
# 	elif imgNo == 2:
# 	elif imgNo == 3:
# 	flash('sucessfully edited..!')
# 	return redirect(url_for('myVehicleDetailsId',vehicleId))	



# ##############chat starts headers###################


@app.route('/chat', methods=['GET', 'POST'])
def index():
    if 'user_session' in session:
        pass
    else:
        return redirect('/login')
    print(os.path.isdir(app.config['UPLOAD_FOLDER']))
    print(app.root_path)
    if request.method == 'POST':
        newFriend = request.form.get('newFriend').lower().strip()

        select = Contact.query.filter_by(
            sender=session['user_session'], reciver=newFriend).first()
        if select != None or newFriend == session['user_session']:
            errorMsg = newFriend + ' is already in your contact list.'
            # ('<h1>Error</h1>')
            return render_template('error.html', errorMsg=errorMsg)

        select = Users.query.filter_by(email=newFriend).first()
        if select == None:
            errorMsg = 'No user available. Kindly check your friends username.'
            # ('<h1>Error</h1>')
            return render_template('error.html', errorMsg=errorMsg)

        entry = Contact(
            sender=session['user_session'],
            reciver=newFriend
        )
        entry1 = Contact(
            sender=newFriend,
            reciver=session['user_session']
        )

        db.session.add(entry)
        db.session.add(entry1)
        db.session.commit()

    checkImg = os.path.isfile(
        './static/img/' + session['phone_number'] + '.jpg')
    select2 =session.get('phone_number')
    select = Contact.query.filter_by(sender=session['user_session']).all()
    if not checkImg:
        return render_template('contact.html', select=select, user=session['user_session'], checkImg=checkImg, phone_number= select2)

    return render_template('contact.html', select=select, user=session['user_session'],phone_number=select2)


@app.route('/chat/<string:sender>/<string:reciver>', methods=['GET', 'POST'])
def chat(sender, reciver):
    if 'user_session' in session:
        pass
    else:
        return redirect('/login')

    if request.method == 'POST':
        msg = request.form.get('msg')

        DateTime = datetime.now().strftime("%d.%m.%y %H:%M")
        entry = Messages(
            sender=session['user_session'],
            msg=msg,
            reciver=reciver,
            dateTime=DateTime
        )
        db.session.add(entry)
        db.session.commit()

    select = Contact.query.filter_by(sender=session['user_session']).all()
    selectMsg = Messages.query.filter(
        sender == session['user_session'] or sender == reciver,
        reciver == reciver or reciver == session['user_session'],
    ).all()
    select2 = Users.query.filter_by(phone_number=session['phone_number']).first()

    return render_template(
        'chat.html',
        select=select,
        selectMsg=selectMsg,
        sender=sender,
        reciver=reciver,
        phone_number=select2
    )


@app.route('/chat/@<string:sender>/<string:reciver>')
def dataProvider(sender, reciver):
    selectMsg = Messages.query.filter(
        sender == session['user_session'] or sender == reciver,
        reciver == reciver or reciver == session['user_session'],
    ).all()
    senderD = []
    msgD = []
    reciverD = []
    dateTimeD = []
    jsonP = {}
    for n in selectMsg:
        if n.reciver in [sender, reciver] and n.sender in [sender, reciver]:
            senderD.append(n.sender)
            msgD.append(n.msg)
            reciverD.append(n.reciver)
            dateTimeD.append(n.dateTime)
    jsonP['sender'] = senderD
    jsonP['msg'] = msgD
    jsonP['reciver'] = reciverD
    jsonP['dateTime'] = dateTimeD
    return json.dumps(jsonP)


@app.route('/chat/<string:sender>', methods=['GET', 'POST'])
def edit(sender):
    if 'user_session' in session:
        pass
    else:
        return redirect('/login')

    if request.method == 'POST':
        fileImg = request.files['fileImg']
        fileImg.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(
            session['phone_number']+'.jpg')))
        # print('not sir',session['user_session'])
        # print('sir wala',session.get('user_session'))
        select = Users.query.filter_by(
            email=session['user_session']).first()
        select2 = Users.query.filter_by(phone_number=session['phone_number']).first()

        return render_template("edit.html", user=select,phone_number=select2)

    select = Users.query.filter_by(email=session['user_session']).first()
    select2 = Users.query.filter_by(phone_number=session['phone_number']).first()

    return render_template("edit.html", user=select,phone_number=select2)


@app.route('/chat/view/<string:reciver>')
def view(reciver):
    select = Users.query.filter_by(email=reciver).first()
    return render_template("view.html", user=select)




@app.route('/error')
def error():
    return redirect('/login')

#################chat ends here #####################



if __name__=='__main__':
	app.run()
