from flask import Flask, jsonify, request, render_template, Blueprint, session, redirect, url_for
from app import db

main = Blueprint('main', __name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')

@main.route('/')
def index():
    return render_template('index.html')