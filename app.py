#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import bottle
from bottle import route, run, template
import urllib.request, json

with urllib.request.urlopen("http://apis.is/currency/") as url:
    apidata = json.loads(url.read().decode())

@route("/")
def index():
    return '''<h1>Verkefni 4 - JSON og API</h1><hr><a href="/json">> Verkefni 4.1 - JSON</a><br><a href="/api">> Verkefni 4.2 - API</a>'''

@route("/json")
def verk4_1():
    data = open('gengi.json', 'r', encoding='utf-8')
    gengi = json.load(data)
    data.close()
    return template('index', gogn=gengi)

@route("/api")
def verk4_2():
    return template('table', data=apidata)

bottle.run(host='0.0.0.0', port=argv[1])
