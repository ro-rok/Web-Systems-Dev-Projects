from flask import Blueprint, request
from flask import redirect
hello = Blueprint('hello', __name__, url_prefix='/')


@hello.route('/')
def index():
    return redirect('/login')
