#!/usr/local/bin/python3
import os

txtdir = 'src/'
htmldir = '../templates/logs/'




for file_name in os.listdir(txtdir):
    txt = open(txtdir+file_name,'r')
    html = open(htmldir+file_name.replace('.txt','.html'),'w')

    html.write('''{% extends "log_base.html" %}
{% block log %}\n\n''')

    for line in txt:
        if line is not '\n':
            html.write('<p>'+line.strip()+'</p>\n')
            html.write('<br>\n')

    html.write('\n{% endblock %}')
