from flask import Flask,render_template,request
import cx_Oracle
app=Flask(__name__)
@app.route('/loginpage.html',methods=['GET','POST'])
def loginpage():
	return render_template("loginpage.html")
@app.route('/loginsuccess.html',methods=['GET','POST'])
def loginsuccess():
	return render_template("loginsuccess.html")
@app.route('/logincheck',methods=['GET','POST'])
def logincheck():
	sun=request.form['un']
	spw=request.form['pw']
	conn=cx_Oracle.connect('system','240662')
	curs=conn.cursor()
	curs.execute("select * from login where username='%s' and password='%s'" %(sun,spw))
	rows=curs.fetchall()
	count=curs.rowcount
	if count==1:
		return render_template("loginsuccess.html")
	else:
		return render_template("loginfail.html")
@app.route('/insertpage.html',methods=['GET','POST'])
def insertbackend():
	ID = request.form['patientID']
	patient_name=request.form['patientname']
	age=request.form['age']
	gender=request.form['gender']
	disease=request.form['disease']
	phone_no = request.form['PhoneNo']
	conn=cx_Oracle.connect('system','240662')
	cur=conn.cursor()
	curs.execute("insert into patient_details values('%d','%s','%d',%s,'%s','%d')" %(int(ID),patient_name,int(age),gender,disease,int(phone_no)))
	conn.commit()
	curs.close()
	conn.close()
	return render_template("insertsuccess.html")
@app.route('/insertpage.html',methods=['GET','POST'])
def insertpage():
	return render_template("insertpage.html")
@app.route('/display.html',methods=['GET','POST'])
def displayfrombackend():
	conn=cx_Oracle.connect('system','240662')
	curs=conn.cursor()
	curs.execute("select * from patient_details")
	rows=curs.fetchall()
	return render_template("display.html",hrows=rows)
@app.route('/deletepage.html',methods=['GET','POST'])
def deletepage():
	return render_template("deletepage.html")
@app.route('/delete',methods=['GET','POST'])
def deletefrombackend():
	patient_ID=request.form['Patient_ID']
	conn=cx_Oracle.connect('system','240662')
	curs=conn.cursor()
	curs.execute("delete from patient_details where usn='%s'" %(patient_ID))
	conn.commit()
	curs.close()
	conn.close()
	return render_template("deletesuccess.html")
app.run(debug=True)