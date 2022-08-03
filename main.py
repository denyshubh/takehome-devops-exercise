'''
Sample Flask Auth App
'''
from flask import Flask
from config import BaseConfig
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity,jwt_required, unset_jwt_cookies,JWTManager
import os

class Users():
  def __init__(self, user_id, user_full_name, user_email)
    self.userId = user_id
    self.userFullName = user_full_name
    self.userEmail=user_email

@app.route('/healthz')
def index():
    return 'index'

@app.route('/v1/user')
# @jwt_required()
def login():
    return 'login'

jwt = JWTManager()

def create_app():
  app = Flask(__name__)
  app.config['JWT_SECRET_KEY'] = os.getenv('APP_JWT_SECRET', os.urandom(32))
  jwt.init_app(app)
  return app
  
if __name__=='__main__':
  jwtSampleToken = os.getenv('APP_JWT_SECRET', None)
  if jwtSampleToken is None:
    print("APP_JWT_SECRET environment variable not set")
  app = create_app()
  app.run(host="0.0.0.0", port=3000, debug=False)
