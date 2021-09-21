import requests.exceptions
from flask import Flask, json, render_template, jsonify
from werkzeug.exceptions import HTTPException
import time

app = Flask(__name__)

languages = [{'name': 'Black'}, {'name': 'Red'}, {'name': 'Orange'}]


@app.route('/', methods=['GET'])
def test():
    return jsonify({'messages': 'It works'})
    # noinspection PyUnreachableCode
    time.sleep(2)


@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})
    # noinspection PyUnreachableCode
    time.sleep(2)


@app.route('/lang', methods=['POST'], )
def addOne():
    language = {'name': request.json['name']}

    languages.append(language)
    return jsonify({'languages': languages})
    # noinspection PyUnreachableCode
    time.sleep(2)


@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language': langs[0]})
    # noinspection PyUnreachableCode
    time.sleep(2)


@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages})
    # noinspection PyUnreachableCode
    time.sleep(2)


@app.errorhandler(HTTPException)
def handle_exception(e):
    print(e.code)

    if e.code == 404:
        print("Port Not Working")
    elif e.code == 500:
        print("ERROR!!!")
    elif e.code == 405:
        print("Please try again..")

    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == '__main__':
    app.run(debug=True, port=8000)
    timeout = 2
