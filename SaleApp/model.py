import json

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from SaleApp import app, db
from enum import Enum as UserEnum
from flask_login import UserMixin


class RoleEnum(UserEnum):
    USER = 1
    ADMIN = 2

class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=True, unique=True)
    active =  Column(Boolean, default=True)

    def __str__(self):
        return self.name

class User(Base, UserMixin):
    username = Column(String(200), nullable=False)
    password = Column(String(150), nullable=False)
    avatar = Column(String(300), default="https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg")
    role = Column(Enum(RoleEnum), default=RoleEnum.USER, nullable=False)

class Category(Base):
    products = relationship('Product', backref='category', lazy=True)


class Product(Base):
    price = Column(Float, default=0.0)
    image = Column(String(300), default="https://cdn2.cellphones.com.vn/insecure/rs:fill:0:0/q:100/plain/https://cellphones.com.vn/media/wysiwyg/Phone/Apple/iPhone-16/iphone-16-2_2.jpg")
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=True)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        c1 = Category(name="Mobile")
        c2 = Category(name="Laptop")
        c3 = Category(name="Tablet")

        db.session.add_all([c1, c2, c3])
        db.session.commit()
        print(c1)

        u = User(name="User", username="user", password="123")
        db.session.add(u)

        with open("data/products.json", encoding="utf-8") as f:
            prods = json.load(f)

            for p in prods:
                db.session.add(Product(**p))
        db.session.commit()