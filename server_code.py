#
#   Author  : Anjani Suresh Bhat
#   Date    : August 2016
#
#   This file implements functionality for each url route
#
#


from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_base import Base, Items

app = Flask(__name__)

engine = create_engine('sqlite:///item_list.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/items/')
def show_items():
    """
    This function queries database and renders the required information through the HTML page
    :return: HTML page which returns all the items as a list
    """
        dict_items = {}
        item_list_clothes = session.query(Items).filter_by(type_item="Clothes")
        item_list_electronics = session.query(Items).filter_by(type_item="Electronics")
        item_list_books = session.query(Items).filter_by(type_item="Books")
        item_list_sports = session.query(Items).filter_by(type_item="Sports")
        dict_items.update({"Clothes": item_list_clothes})
        dict_items.update({"Electronics": item_list_electronics})
        dict_items.update({"Books": item_list_books})
        dict_items.update({"Sports": item_list_sports})
        return render_template('homepage.html', items=dict_items)


@app.route('/items/<int:item_id>')
def show_each_item(item_id):
    """
    To display each item as a HTML page
    :param item_id: ID of each item
    :return: HTML page which is template for displaying each item
    """
    single_item = session.query(Items).filter_by(id=item_id).one()
    # for i in single_item:
    print(single_item.price)
    return render_template('individual.html', itemx=single_item)


@app.route('/items/new', methods=["GET", "POST"])
def newItem():
    """
    This is an API to create new item and update it to database
    :return: HTML page to enter details of new item
    """
    if request.method == "POST":
        new_item = Items(name=request.form['name'], picture=request.form['picurl'], price=request.form['price'],
                         type_item=request.form['type'], description=request.form['desc'],
                         brand_name=request.form['brand'])
        session.add(new_item)
        session.commit()
        return redirect(url_for('show_items'))
    else:
        return render_template('newItem.html')


@app.route('/items/<int:item_id>/edit', methods=["GET", "POST"])
def editItem(item_id):
    """
    This is an API to edit an existing item and update it to database
    :param item_id: ID of item to be edited
    :return: HTML page to enter details of item go be edited
    """
    if request.method == "POST":
        itemx = session.query(Items).filter_by(id=item_id).one()
        if request.form['name'] != "":
            itemx.name = request.form['name']
        if request.form['picurl'] != "":
            itemx.picture = request.form['picurl']
        if request.form['price'] != "":
            itemx.price = request.form['price']
        if request.form['type'] != "":
            itemx.type_item = request.form['type']
        if request.form['desc'] != "":
            itemx.description = request.form['desc']
        if request.form['brand'] != "":
            itemx.brand_name = request.form['brand']
        session.commit()
        return redirect(url_for('show_items'))
    else:
        return render_template('edit_item.html')


@app.route('/items/<int:item_id>/delete')
def deleteItem(item_id):
    """
    This is an API to delete an existing item and update it to database
    :param item_id: ID of item to be deleted
    :return: HTML page to show all elements after deleting the entered item
    """
    session.query(Items).filter_by(id=item_id).delete()
    session.commit()
    return redirect(url_for('show_items'))


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
