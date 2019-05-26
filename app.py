from flask import Flask
from flask import request
from flask import jsonify
import json

from application import *
app = Flask(__name__)

@app.route('/getIssues',methods=['POST'])
def get_issues():
   request_params = request.data
   params = json.loads(request_params)
   print(params['url'])
   result = hit_url(params['url'])
   print(result)
   response = app.response_class(response=result, status=200, mimetype='application/json')
   
   return response
   
   
   


if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)
   
