import mysql.connector
import json
from flask import make_response
from datetime import datetime, timedelta
# import jwt

class customer_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
            self.cur=self.con.cursor(dictionary=True)
            self.con.autocommit=True
            print("Connection Successful")
        except:
            print("Some error")


    def customer_register_model(self, data):
        self.cur.execute(f"INSERT INTO customer(username, first_name, last_name, password, address, email_id) VALUES ('{data['username']}', '{data['first_name']}', '{data['last_name']}', '{data['password']}', '{data['address']}', '{data['email_id']}')")
        return make_response({"message":"Customer Registered Successfully"}, 201)

    def customer_update_model(self, data):
        self.cur.execute(f"UPDATE customer SET username='{data['username']}', first_name='{data['first_name']}', last_name='{data['last_name']}', address='{data['address']}', email_id='{data['email_id']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:                         ## some changes were made
            return make_response({"message":"Successfully Updated Customer"}, 201)
        else:                                          ## No changes were detected
            return make_response({"message":"Nothing to Update"}, 202)

    def customer_changepassword_model(self, data, id):

        self.cur.execute(f"UPDATE customer SET password='{data['password']}' WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"Password Updated Successfully"},201)
        else:
            return make_response({"message":"Nothing to Update"},202)

    def customer_getall_model(self):
        self.cur.execute("SELECT * FROM customer")
        result = self.cur.fetchall()
        # print(result)
        # the value retrieved in 'result' is a "List of Dictionaries"
        if len(result)>0:
            # return json.dumps(result)  ## to convert to strings
            res = make_response({"payload": result}, 200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res 
        else:
            return make_response({"message":"No Data Found"}, 204)



    def customer_delete_model(self, id):
        self.cur.execute(f"DELETE FROM customer WHERE id={id}")
        if self.cur.rowcount>0:                         ## some changes were made
            return make_response({"message":"Successfully Deleted User"}, 200)
        else:                                           ## No changes were detected
            return make_response({"message":"Nothing to Delete"}, 202)