from flask import Flask, render_template, request, redirect
import dao
from SaleApp import app, login
from flask_login import login_user, logout_user, current_user



@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    return render_template("index.html", prods=dao.load_products(q=q, cate_id=cate_id))

@app.route("/product/<int:id>")
def details(id):
    return render_template("product-detail.html", prod = dao.get_product_by_id(id))

@app.route("/login", methods=['get', 'post'])
def login_my_user():
    err_msg = None
    if request.method.__eq__("POST"):
        username = request.form.get("username")
        password = request.form.get("password")

        user = dao.auth_user(username, password)

        if user:
            login_user(user)
            return redirect("/")
        else:
            err_msg = "Tài khoản hoặc mật khẩu không đúng!";
    return render_template("login.html", err_msg=err_msg)

@app.context_processor
def common_attribute():
    return {
        "cates":dao.load_categories()
    }

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__=="__main__":
    app.run(debug=True, port=5001)