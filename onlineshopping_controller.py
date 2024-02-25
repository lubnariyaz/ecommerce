from app import app
from flask import request, send_file
from model.onlineshopping_model import onlineshopping_model
from datetime import datetime

obj = onlineshopping_model()

@app.route("/onlineshopping/add/<custid>", methods=["POST"])
def onlineshopping_add_controller(custid):
    return obj.onlineshopping_add_model(request.form, custid)

@app.route("/customer/update", methods=["PUT"])
def customer_update_controller():
    return obj.customer_update_model(request.form)

@app.route("/customer/changepassword/<id>", methods=["PATCH"])
def customer_changepassword_controller(id):
    return obj.customer_changepassword_model(request.form, id)

@app.route("/customer/getall")
def customer_getall_controller():
    return obj.customer_getall_model()

@app.route("/customer/delete/<id>", methods=["DELETE"])
def customer_delete_controller(id):
    return obj.customer_delete_model(id)