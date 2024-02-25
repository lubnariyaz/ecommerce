from app import app
from flask import request, send_file
from model.category_model import category_model
from datetime import datetime

obj = category_model()

@app.route("/category/viewall")
def category_viewall_controller():
    return obj.category_viewall_model()

@app.route("/category/addone", methods=["POST"])
def category_addone_controller():
    return obj.category_addone_model(request.form)

@app.route("/category/update", methods=["PUT"])
def category_update_controller():
    return obj.category_update_model(request.form)

@app.route("/category/delete/<id>", methods=["DELETE"])
def category_delete_controller(id):
    return obj.category_delete_model(id)