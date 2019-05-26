from flask import Flask
from flask import request, render_template
from flask import jsonify
import json

from IssueCounter import *
app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')  # main page to input link


@app.route('/getIssues', methods=['POST'])
def get_issues():
    url = request.form.to_dict()
    global total
    total = 0
    # input link is passed through the url and passed to hit_url function to fetch the count
    res = hit_url(url['link'])
    return render_template("result.html", result=json.loads(res))


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
