from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
tracks = Blueprint('tracks', __name__, url_prefix='/tracks', template_folder='templates')
