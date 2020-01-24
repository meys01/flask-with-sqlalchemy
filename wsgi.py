# wsgi.py
from flask import Flask, request, make_response, render_template
from config import Config
import os
import sys
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # Order is important here!


app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
from schemas import products_schema, product_schema

@app.route('/products')
def products():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return products_schema.jsonify(products)
"""
@app.route('/products/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def product(id):
    product = db.session.query(Product)
    if request.method == 'GET':
        return product_schema.jsonify(product.get(id))

    if request.method == 'DELETE':
        db.session.delete(product.get(id))
        db.session.commit()
        return make_response("Deleted",204)

    if request.method == 'PATCH':
        content = request.get_json()
        item = product.get(id)
        print(f"Item: [{item}] type is [{type(item)}]", file=sys.stderr)
        print(f"Content: [{content}] type is [{type(content)}]", file=sys.stderr)
        item.name = content["name"]
        db.session.commit()
        return make_response("Updated",204)
"""
@app.route('/<int:id>')
def product_html(id):
    product = db.session.query(Product).get(id)
    return render_template('product.html', product=product)

@app.route('/')
def home():
    products = db.session.query(Product).all()
    return render_template('home.html', products=products)

"""
@app.route('/hello')
def hello():
    return "Hello World!"
"""
