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
from reddit import app
from reddit.form import search_sub_form,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
base_url = 'https://www.reddit.com/'
reddit_username = 'saidazimovaziza'
reddit_password = 'odulim11'
app_id = 'sYvOOFwIN4QbSw'
app_secret ='yMJIcKL8d-69aehR3mp9MyoWEho'
data = {'grant_type': 'password', 'username': reddit_username, 'password': reddit_password}
client_auth = requests.auth.HTTPBasicAuth(app_id, app_secret)
response = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'puppy-parser by alpscode'},
                  auth=client_auth)
print(response.status_code)
values = response.json()

token = 'bearer {}'.format(values['access_token'])
print(token)
api_url = 'https://oauth.reddit.com'
url='https://oauth.reddit.com/r/all/'
headers = {'Authorization': token, 'User-Agent': 'puppy-parser by alpscode'}
response = requests.get(api_url + '/api/v1/me', headers=headers)
posts=[]
reddit = praw.Reddit(client_id='sYvOOFwIN4QbSw',client_secret='yMJIcKL8d-69aehR3mp9MyoWEho',user_agent='Reddit', username='saidazimovaziza')


@app.route("/")
@app.route("/home")
def about():
	# allp=requests.post('https://www.reddit.com/r/all',headers={'User_agent':'Safari'})
	payload = {'limit': 1, 'sort': 'relevance'}
	response = requests.get(url, headers=headers, params=payload)
	
	posts = response.json()
	
	return render_template("home.html", posts=posts['data']['children'])


@app.route("/search/subreddit", methods=['GET', 'POST'])
def search_for_subreddit():
    form = search_sub_form()
    if form.validate_on_submit():
    	payload = {'q':form.search.data+'','limit': 10, 'sort': 'relevance'}
    	response = requests.get(url, headers=headers, params=payload)
    	posts = response.json()
    	return render_template("home.html",posts=posts['data']['children'])
    else:   
    	return render_template('search.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():# do not work as login
    form = LoginForm()
    if form.validate_on_submit():
    	response = requests.get('https://oauth.reddit.com/https://www.reddit.com'
    authorizePath: '/api/v1/authorize', auth=HTTPBasicAuth('saidazimovaziza', 'odulim11'))
    	if response.status_code == 200:
    		return render_template("home.html")
    	else: 
    		return render_template('login.html', form=form)
    else:   
    	return render_template('login.html', form=form)




@app.route("/comments")
def comments():
	postss=[]
	posts = reddit.subreddit('news').hot(limit=10)
	for sub in postss:
		sub.comments.replace_more(limit=0)
		comments=[]
		for comment in sub.comments.list():
			comments.append(comment.body)
		postss.append(Post(sub.title,comments))
	return render_template("comments.html", posts=postss)


@app.route("/history")
def user_history():
	payload = {'limit': 10, 'sort': 'relevance'}
	response = requests.get('https://oauth.reddit.com/u/saidazimovaziza/', headers=headers, params=payload)
	
	posts = response.json()
	# print(posts)
	return render_template("profile.html", posts=posts['data']['children'])


@app.route("/collections")
def collections():
	payload = {'limit': 10, 'sort': 'relevance'}
	response = requests.get('https://oauth.reddit.com/user/saidazimovaziza/saved.json', headers=headers, params=payload)
	
	posts = response.json()
	# print(posts)
	return render_template("home.html", posts=posts['data']['children'])

