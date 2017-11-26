import flask
import openalpr_api
from openalpr_api.rest import ApiException
from pprint import pprint
import urllib
from os.path import join as _j
import base64
from flask import Flask, request, session, g, redirect, url_for, Response
import json

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=False,
))

def callAPI(image_url):
    target_path = _j('tmp',image_url.split('/')[-1])
    urllib.urlretrieve(image_url,target_path)
    with open(target_path, "rb") as image_file:
        image_bytes = base64.b64encode(image_file.read())
    api_instance = openalpr_api.DefaultApi()
    secret_key = 'sk_e014dacb3b70f1a4a902b301' 
    country = "us" 
    recognize_vehicle = 0 
    state = '' 
    return_image = 0 
    topn = 10 
    prewarp = ''
    
    try:
        api_response = api_instance.recognize_bytes(image_bytes,
                                                    secret_key,
                                                    country,
                                                    recognize_vehicle=0,
                                                    state='',
                                                    return_image=0,
                                                    topn=10,
                                                    prewarp='')
        return api_response
    except ApiException as e:
        print "Exception when calling DefaultApi->recognize_bytes: %s\n" % e

def sign(res):
    res['author'] = 'sepehr'
    return res

@app.route("/get", methods=['GET','POST'])
def get():
    if request.json:
        data = request.json # will be
        image_url=data['image_url']
        res = sign(callAPI(image_url).to_dict())
        dumped = json.dumps(res)
        response = Response(response=dumped, status=200, mimetype='application/json')
        return response
    else:
        return "no json received"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)

