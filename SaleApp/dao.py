import json
from model import Category, Product, User
from SaleApp import db, app
import hashlib

def load_categories():
    # with open("data/category.json", encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query

def load_products(q=None, cate_id=None):
    # with open("data/products.json", encoding="utf-8") as f:
    #     prods = json.load(f)
    #
    #     if q:
    #         prods = [p for p in prods if p["name"].find(q)>=0]
    #
    #     if cate_id:
    #         prods = [p for p in prods if p["cate_id"].__eq__(int(cate_id))]
    #     return prods

    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))

    if cate_id:
        query = query.filter(Product.cate_id.__eq__(int(cate_id)))

    return query.all()

def get_product_by_id(id):
    return Product.query.get(id)

def add_user(name, username, password):
    password = hashlib.md5(password.encode("utf-8")).hexdigest()
    u = User(name=name, username=username, password=password)
    db.session.add(u)
    db.session.commit()

def auth_user(username, password):
    password = hashlib.md5(password.encode("utf-8")).hexdigest()
    return User.query.filter(User.username==username, User.password==password).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)

if __name__=="__main__":
    with app.app_context():
        print(add_user(name="User2", username="user2", password="123"))
        #print(auth_user("user2", "123"))