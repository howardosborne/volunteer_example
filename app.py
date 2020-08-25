import os, subprocess, glob
from flask import Flask, flash, render_template, abort, redirect, url_for, request, make_response, jsonify, session
import requests
from werkzeug.utils import secure_filename
import random, string

app = Flask(__name__)
app.secret_key = b'sdvsdkdsfdaw4ttgsdvzdgwtasq242'

@app.route('/')
def root(token=None):
    session['one_time_tokens'] = ""
    token = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    session['one_time_tokens'] = token
    return render_template('index.html', token=token)

@app.route('/details/<id>')
def details(id=None):
    return render_template('project_details.html',id=id)

@app.route('/apply/<id>')
def apply(id=None):
    return render_template('apply.html',id=id)

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/submit_donation', methods=['POST'])
def submit_donation():
    firstName = request.form['firstName']
    return render_template('thanks.html',firstName=firstName)

@app.route('/submit_application', methods=['POST'])
def submit_application():
    firstName = request.form['firstName']
    return render_template('thanks.html',firstName=firstName)

@app.route('/api/projects')
def projects():
    return """
    [
        {"id":1,
        "image":"/static/project_1.jpg",
        "title":"Rurigrow",
        "full_details":"This project based in Eastern Ruritania has been running for 12 years and is ideal for those who are new to tree planting and want to work on a project with well established practices.",
        "duration":"4 weeks"
        },
        {"id":2,
        "image":"/static/project_2.jpg",
        "title":"RuthTree",
        "full_details":"This project based in Southern Ruthenia has been running for 6 years and is ideal for those who want to improve their western slavic language skills whilst digging holes",
        "duration":"2 weeks"
        },        
        {"id":3,
        "image":"/static/project_3.jpg",
        "title":"Make Silesia Green",
        "full_details":"This project based in Western Silesia has been running for 3 years and is ideal for those who are keen on nocturnal wild boar encounters.",
        "duration":"2 months"
        }, 
        {"id":4,
        "image":"/static/project_4.jpg",
        "title":"Project Bukmore",
        "full_details":"This project based in Northern Bukovena has been running for 12 weeks and is good for experiences tree huggers.",
        "duration":"1 day"
        }
    ]
    """