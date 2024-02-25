import mysql.connector
import json
from flask import make_response
from datetime import datetime, timedelta

class category_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
            self.cur=self.con.cursor(dictionary=True)
            self.con.autocommit=True
            print("Connection Successful")
        except:
            print("Some error")


    def category_viewall_model(self):
        self.cur.execute("SELECT * FROM category")
        result = self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)  ## to convert to strings
            res = make_response({"payload": result}, 200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res 
        else:
            return make_response({"message":"No Data Found"}, 204)


    def category_addone_model(self, data):
        self.cur.execute(f"INSERT INTO category(category_name) VALUES ('{data['category_name']}')")
        return make_response({"message":"Successfully Added Category"}, 201)


    def category_update_model(self, data):
        self.cur.execute(f"UPDATE category SET category_name='{data['category_name']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:                         ## some changes were made
            return make_response({"message":"Successfully Updated Category"}, 201)
        else:                                          ## No changes were detected
            return make_response({"message":"Nothing to Update"}, 202)


    def category_delete_model(self, id):
        self.cur.execute(f"DELETE FROM category WHERE id={id}")
        if self.cur.rowcount>0:                         ## some changes were made
            return make_response({"message":"Successfully Deleted Category"}, 200)
        else:                                           ## No changes were detected
            return make_response({"message":"Nothing to Delete"}, 202)