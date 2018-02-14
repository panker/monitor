from flask import Blueprint

app_main = Blueprint('main',__name__)

from . import views