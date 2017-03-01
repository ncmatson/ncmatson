from app import app, grabber
from flask import render_template, request, url_for
import os, requests
import re

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

@app.route('/map/')
def map():
    return render_template('map.html',
    title = 'Map'
    )

def rm(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

@app.route('/grabber/', methods=['POST'])
def doGrabber():
    rm('app/static/img', 'dg*')
    data = request.form
    lat = data['lat']
    lon = data['lon']
    zoom = data['zoom']

    g = grabber.Grabber('app/static/img')
    time = g.grab(lat, lon, zoom)

    url = url_for('static', filename='img/dg'+time+'.jpg')
    return url
