# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:58:50 2023

@author: Shivani_SB
"""
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
        print("The Educvation Qualification is : ",  dictionary["EDUCATION QUALIFICATION"])
        print("The Email is : ", dictionary["EMAIL"])
        print("The Moblie no is : ",  dictionary["MOBILE NO"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,username,password,confirm_password,gender,date_of_birth,education_qualification,email,mobile_no):
    sql= "INSERT into USER VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(username,password,confirm_password,gender,date_of_birth,education_qualification,email,mobile_no)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=rqy41363;PWD=9ozyrz3LXNz0Fwhv",'','')
    print(conn)
    print("connection successful...")
    #insertdb(conn,"Hari","Hari@gmail.com",'1234567890','Adarsh nagar','Faculty','Civil','1234567')
    getdetails("Hari@gmail.com",'1234567')
    #showall()

except:
    print("Error connecting to the database")



