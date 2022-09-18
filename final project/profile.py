from flask import Flask,current_app,render_template,request,redirect,flash,url_for,Blueprint,session


from flask_mysqldb import MySQL
from flask_session import Session

from main import app


second =Blueprint("second",__name__,static_folder="static",template_folder="templates")


#database setting for mysql
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
second.config['MYSQL_PASSWORD']=''
second.config['MYSQL_DB']='rental_services'

mysql=MySQL(second)


# Session setting 
second.config["SESSION_PERMANENT"]=False
second.config["SESSION_TYPE"]="filesystem"
Session(second)



@second.route("/fname", methods=['POST'])
def changefname():
	fname=request.form['fname']
	print(fname)
		
	cursor =mysql.connection.cursor()
	cursor.execute("UPDATE `users` SET `image_path`=%s WHERE `email`=%s",(path,session['email'],)); 
	mysql.connection.commit()
	cursor.close()


	return redirect("profile")
	
