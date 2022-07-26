'''
Sample Flask Auth App
'''

from flask import Flask, request
from flask_api import status
from flask_jwt_extended import create_access_token,get_jwt_identity,verify_jwt_in_request,JWTManager
import os

class Users():
    def __init__(self, user_id, user_full_name, user_email):
        self.userId = user_id
        self.userFullName = user_full_name
        self.userEmail=user_email

    def to_dict(self):
        return {'UserID': self.userId,'FullName': self.userFullName,'Email': self.userEmail}

app = Flask(__name__, instance_relative_config=False)
app.config['JWT_SECRET_KEY'] = os.getenv('APP_JWT_SECRET', os.urandom(32))
jwt = JWTManager(app)

@app.route('/v1/user', methods=['GET'])
def user():
    try:
        verify_jwt_in_request()
        if get_jwt_identity():
            userId, userFullName, userEmail = get_jwt_identity()
            user = Users(userId, userFullName, userEmail)
            return user.to_dict(), status.HTTP_200_OK
            
    except Exception as e:
        print(e)
    return 'Invalid Token!', status.HTTP_400_BAD_REQUEST

@app.route("/healtz", methods=['GET'])
def healthz():
    return 'ok', status.HTTP_204_NO_CONTENT

@app.route("/token", methods=['POST'])
def generate_auth_token():
    data = request.get_json()
    user = Users(data.get('userId'), data.get('userFullName'), data.get('userEmail'))
    auth_token = create_access_token(identity=[user.userId, user.userFullName, user.userEmail], expires_delta=False)  # jason web token  
    return auth_token
  
if __name__=='__main__':
  jwtSampleToken = os.getenv('APP_JWT_SECRET', None)
  if jwtSampleToken is None:
    print("APP_JWT_SECRET environment variable not set")
  app.run(host="0.0.0.0", port=3000, debug=False)
