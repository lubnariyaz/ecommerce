from app import app
from flask import request, send_file
from model.customer_model import customer_model
from datetime import datetime

obj = customer_model()

@app.route("/customer/register", methods=["POST"])
def customer_register_controller():
    return obj.customer_register_model(request.form)

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