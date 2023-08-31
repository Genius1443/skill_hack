from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
def showall():
    sql= "SELECT * from SKILL_HACK"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Username is : ",  dictionary["NAME"])
        print("The Password is : ",  dictionary["PASSWORD"])
        print("The Confirm Password is : ",  dictionary["CONFIRM_PASSWORD"])
        print("The Gender is : ",  dictionary["GENDER"])
        print("The Date Of Birth is : ",  dictionary["DATE_OF_BIRTH"])
        print("The Educvation Qualification is : ",  dictionary["EDUCATION_QUALIFICATION"])
        print("The Email is : ", dictionary["EMAIL"])
        print("The Moblie no is : ",  dictionary["MOBILE_NO"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql= "select * from SKILL_HACK where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Username is : ",  dictionary["NAME"])
        print("The Password is : ",  dictionary["PASSWORD"])
        print("The Confirm Password is : ",  dictionary["CONFIRM_PASSWORD"])
        print("The Gender is : ",  dictionary["GENDER"])
        print("The Date Of Birth is : ",  dictionary["DATE_OF_BIRTH"])
        print("The Educvation Qualification is : ",  dictionary["EDUCATION_QUALIFICATION"])
        print("The Email is : ", dictionary["EMAIL"])
        print("The Moblie no is : ",  dictionary["MOBILE_NO"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,username,password,confirm_password,gender,date_of_birth,education_qualification,email,mobile_no):
    sql= "INSERT into USER VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(username,password,confirm_password,gender,date_of_birth,education_qualification,email,mobile_no)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
    
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=wxy42262;PWD=QgeqHqdxW7MWmqc8",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index1')
def index1():
    return render_template('index.html')
@app.route('/apply')
def apply12():
    return render_template('registrationpage.html')
@app.route('/cont')
def cont():
    return render_template('contact.html')
@app.route('/abt')
def abt():
    return render_template('about.html')
@app.route('/login')
def price():
    return render_template('login.html')
@app.route('/confirm')
def serv():
    return render_template('confirm.html')
@app.route('/myprofile')
def team():
    return render_template('myprofile.html')
@app.route('/doubts')
def test():
    return render_template('doubts.html')





@app.route('/apply', methods=['POST','GET'])
def apply():
    if request.method == "POST":
        username = request.form['username']
        password=request.form['password']
        confirm_password=request.form['confirm_password']
        gender = request.form['gender']
        date_of_birth = request.form['date_of_birth']
        email = request.form['email']
        mobile_no = request.form['mobile_no']
        
        #inp=[name,email,contact,address,role,branch,password]
        insertdb(conn,username,password,confirm_password,gender,date_of_birth,email,mobile_no)
    return render_template('index.html')




@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['msg']
        insertdb1(conn,name,email,subject,msg)
    return render_template('index.html')




@app.route('/doc', methods=['POST','GET'])
def doc():
    if request.method == "POST":
        date = request.form['date']
        service= request.form['service']
        
        insertdb2(conn,date,service)
    return render_template('team.html')




@app.route('/sign', methods=['POST','GET'])
def sign():
    if request.method == "POST":
        email = request.form['email']
        
        
        insertdb6(conn,email)
    return render_template('index.html')




@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        sql= "select * from APP where email='{}'".format(email)
        stmt = ibm_db.exec_immediate(conn, sql)
        userdetails = ibm_db.fetch_both(stmt)
        print(userdetails)
        if userdetails:
            session['register'] =userdetails["EMAIL"]
            return render_template('userprofile.html',name=userdetails["NAME"],email= userdetails["EMAIL"],contact= userdetails["CONTACT"],address=userdetails["ADDRESS"],role=userdetails["ROLE"],branch=userdetails["BRANCH"])
        else:
            msg = "Incorrect Email id or Password"
            return render_template("login.html", msg=msg)
    return render_template('login.html')


if _name_ =='_main_':
    app.run( debug = True)
