from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from requests.auth import HTTPBasicAuth
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
import praw
from flask import Flask, jsonify, render_template,Blueprint
from wtforms.validators import DataRequired, ValidationError,Email
import requests
import json
import os
# Create flask instance and flask_restful instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
