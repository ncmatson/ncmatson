import os
from flask import Flask, render_template, request

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug = True

@application.route('/')
@application.route('/index/')
def index():
    return render_template('index.html',
                            title = 'Home',
                            )


@application.route('/bio/')
def tim():
    return render_template('bio.html',
                            title = 'Bio'
                            )

@application.route('/thoughts/')
def thoughts():
    logs = os.listdir('templates/logs/')
    return render_template('thoughts.html',
                                title = 'Thoughts',
                                logs = logs
                                )

@application.route('/thoughts/<log>')
def logs(log):
    log_title = log.replace('.html','')
    return render_template('logs/'+log,
                            title = log_title
                            )

if __name__ == '__main__':
    application.run(host='0.0.0.0')