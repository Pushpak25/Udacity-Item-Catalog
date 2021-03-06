#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web'
                                                                ]['client_id']
APPLICATION_NAME = 'Item Catalog'

# Connect to Database and create database session

engine = create_engine('sqlite:///itemcatalog_final_withusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase
                                  + string.digits) for x in range(32))
    login_session['state'] = state

    # return "The current session state is %s" % login_session['state']

    return render_template('login.html', STATE=state)


# Google sign-in

@app.route('/gconnect', methods=['POST'])
def gconnect():

    # Validate state token

    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'
                                            ), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Obtain authorization code, now compatible with Python3

    request.get_data()
    code = request.data.decode('utf-8')

    try:

        # Upgrade the authorization code into a credentials object

        oauth_flow = flow_from_clientsecrets('client_secrets.json',
                                             scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.

    access_token = credentials.access_token
    url = \
        'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' \
        % access_token

    # Submit request, parse response - Python3 compatible

    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.

    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.

    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.

    if result['issued_to'] != CLIENT_ID:
        response = \
            make_response(json.dumps("Token's client ID does not match app's."
                                     ), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        login_session['credentials'] = credentials
        response = \
            make_response(json.dumps('Current user is already connected.'
                                     ), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.

    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    # Get user info

    userinfo_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += \
        ''' " style = "width: 300px; height: 300px;border-radius: 
        150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '''
    flash('you are now logged in as %s' % login_session['username'])
    return output


# User Helper Functions

def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email'
                                                             ]).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except BaseException:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session

@app.route('/gdisconnect')
def gdisconnect():

        # Only disconnect a connected user.

    access_token = login_session.get('access_token')
    if access_token is None:
        response = \
            make_response(json.dumps('Current user not connected.'),
                          401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' \
        % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':

        # Reset the user's sesson.

        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = redirect(url_for('showCategories'))
        return response
    else:

        # For whatever reason, the given token was invalid.

        response = make_response(
            json.dumps(
                'Failed to revoke token for given user.',
                400))
        response.headers['Content-Type'] = 'application/json'
        return response


# JSON APIs to view category Information

@app.route('/category/JSON')
def showCategoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[category.serialize for category in
                               categories])


@app.route('/category/<int:category_id>/JSON')
@app.route('/category/<int:category_id>/items/JSON')
def showCategoryItemsJSON(category_id):
    categoryItems = \
        session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(categoryItems=[item.serialize for item in
                                  categoryItems])


# Show all categories with latest items

@app.route('/')
@app.route('/category/')
def showCategories():
    categories = session.query(Category).all()
    latestItems = session.query(Item).limit(10)
    return render_template('categories.html', categories=categories,
                           items=latestItems)


# Show all items for a category

@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/items/')
def showItems(category_id):
    categories = session.query(Category).all()
    items = session.query(Item).filter_by(category_id=category_id).all()

    if 'username' not in login_session:
        return render_template('publicitems.html',
                               categories=categories, items=items)
    else:
        return render_template('items.html', categories=categories,
                               items=items)


# Show selected item description

@app.route('/category/<int:category_id>/items/<int:item_id>')
def showItemDescription(category_id, item_id):
    items = session.query(Item).filter_by(category_id=category_id).all()
    categoryItem = session.query(Item).filter_by(id=item_id).first()

    if 'username' not in login_session:
        return render_template('publicitemdescription.html',
                               items=items, categoryItem=categoryItem)
    else:
        return render_template('itemdescription.html', items=items,
                               categoryItem=categoryItem)


# Add a category item

@app.route('/category/new', methods=['GET', 'POST'])
def newCategoryItem():

    # Check if user is logged in

    if 'username' not in login_session:
        return redirect('/login')

    if request.method == 'POST':

        # Add category item

        newCategoryItem = Item(title=request.form['name'],
                               description=request.form['description'],
                               category_id=request.form['category'],
                               user_id=login_session['user_id'])
        session.add(newCategoryItem)
        flash('New Item %s Successfully Created'
              % newCategoryItem.title)
        session.commit()
        return redirect(url_for('showCategories'))
    else:

        # Get all categories

        categories = session.query(Category).all()
        return render_template('newCategoryItem.html',
                               categories=categories)


# Edit an item

@app.route('/category/<int:category_id>/items/<int:item_id>/edit',
           methods=['GET', 'POST'])
def editCategoryItem(category_id, item_id):
    categories = session.query(Category).all()
    editedItem = session.query(Item).filter_by(id=item_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedItem.user_id != login_session['user_id']:
        flash('You are not authorized to edit this Item. Please create your own item in order to edit.')
        return redirect(url_for('showCategories'))

    if request.method == 'POST':
        if request.form['name']:
            editedItem.title = request.form['name']
            editedItem.description = request.form['description']
            editedItem.category_id = request.form['category']
            flash('Item Successfully Edited %s' % editedItem.title)
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategoryItem.html',
                               item=editedItem, categories=categories)


# Delete an item

@app.route('/category/<int:category_id>/items/<int:item_id>/delete',
           methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    categories = session.query(Category).all()
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if itemToDelete.user_id != login_session['user_id']:
        flash('You are not authorized to edit this Item. Please create your own item in order to edit.')
        return redirect(url_for('showCategories'))
    if request.method == 'POST':
        session.delete(itemToDelete)
        flash('%s Successfully Deleted' % itemToDelete.title)
        session.commit()
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('deleteCategoryItem.html',
                               item=itemToDelete, categories=categories)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
