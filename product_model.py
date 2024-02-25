import mysql.connector
import json
from flask import make_response
from datetime import datetime, timedelta

class product_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
            self.cur=self.con.cursor(dictionary=True)
            self.con.autocommit=True
            print("Connection Successful")
        except:
            print("Some error")


    def product_viewall_model(self):
        self.cur.execute("SELECT * FROM products")
        result = self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)  ## to convert to strings
            res = make_response({"payload": result}, 200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res 
        else:
            return make_response({"message":"No Data Found"}, 204)


    def product_addone_model(self, data):
        self.cur.execute(f"INSERT INTO customer(username, first_name, last_name, password, address, email_id) VALUES ('{data['username']}', '{data['first_name']}', '{data['last_name']}', '{data['password']}', '{data['address']}', '{data['email_id']}')")
        return make_response({"message":"Successfully created customer"}, 201)


    def product_update_model(self, data):
        self.cur.execute(f"UPDATE customer SET username='{data['username']}', first_name='{data['first_name']}', last_name='{data['last_name']}', password='{data['password']}', address='{data['address']}', email_id='{data['email_id']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:                         ## some changes were made
            return make_response({"message":"Successfully Updated user"}, 201)
        else:                                          ## No changes were detected
            return make_response({"message":"Nothing to Update"}, 202)


    def product_delete_model(self, id):
        self.cur.execute(f"DELETE FROM customer WHERE id={id}")
        if self.cur.rowcount>0:                         ## some changes were made
            return make_response({"message":"Successfully Deleted User"}, 200)
        else:                                           ## No changes were detected
            return make_response({"message":"Nothing to Delete"}, 202)