# Author : Keven Imbeault
# Creation date : 06/03/2019
# Description : Code to create a Flask app for authentification purposes for the Streamlabs API

#Imports for Flask server
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from json import dumps
import requests, json

#Laucnhing Flask app
app = Flask(__name__)

@app.route('/auth')
def auth():
    #Open the file containing the Client ID and Client Secret from Streamlabs
    f = open('Streamlabs_Credentials.txt', 'r')    
    Token_Data = {'grant_type': 'authorization_code','client_id': 'Client_Id', 'client_secret': 'Client_Secret', 'redirect_uri': 'http://localhost:4000/auth', 'code': request.args.get('code')}
    Token_Data['client_id'] = f.readline().rstrip("\n\r")
    Token_Data['client_secret'] = f.readline().rstrip("\n\r")

    #Makes a POST request to get a token
    r = requests.post('https://streamlabs.com/api/v1.0/token?', data = Token_Data)

    #Makes sure it received a response from the API (No error)
    if r.status_code == 200 :
        Response = []
        Json_Response = r.json()

        Response.append(Json_Response['access_token'])
        Response.append(Json_Response['refresh_token'])

        return "You good fam"
        
    else :
        return r.text

if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)

