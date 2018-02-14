from flask import render_template
from app.auth import auth

@auth.app_errorhandler(404)
def page_not_found(e):
    return '404 not found'