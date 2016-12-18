from app import app
from flask import render_template
import os

@app.route('/')
@app.route('/index/')
def index():
    user = {'nickname': 'Cameron','age':21}  # fake user
    return render_template('index.html',
                            title = 'home',
                            user = user)


@app.route('/bio/')
def tim():
    return render_template('bio.html',
                            title = 'Bio'
                            )

@app.route('/thoughts/')
def thoughts():
    logs = os.listdir('app/templates/logs/')
    return render_template('thoughts.html',
                                title = 'Thoughts',
                                logs = logs
                                )

@app.route('/thoughts/<log>')
def logs(log):
    return render_template('logs/'+log)
