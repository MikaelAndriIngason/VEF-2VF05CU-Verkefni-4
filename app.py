# coding=UTF-8

import urllib.request, json
from bottle import route, run, template

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

if __name__ == "__main__":
    run(debug=True)
