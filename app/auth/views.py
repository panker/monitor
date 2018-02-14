from datetime import datetime
from flask import render_template, session, redirect, url_for
from app.auth import auth

@auth.route('/index' , methods=['GET', 'POST'])
def index():
    return 'index'