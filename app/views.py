import os
from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html',
                            title = 'Home',
                            )


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
    log_title = log.replace('.html','')
    return render_template('logs/'+log,
                            title = log_title
                            )
