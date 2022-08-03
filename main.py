'''
Sample Flask Auth App
'''
from flask import Flask
from flask_api import status
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required,JWTManager
import os

class Users():
    def __init__(self, user_id, user_full_name, user_email):
        self.userId = user_id
        self.userFullName = user_full_name
        self.userEmail=user_email

    def to_dict(self):
        return {'UserID': self.userId,'FullName': self.userFullName,'Email': self.userEmail}

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('APP_JWT_SECRET', os.urandom(32))
jwt = JWTManager(app)

@app.route('/healthz')
def healthz():
    return 'ok', status.HTTP_204_NO_CONTENT

@app.route('/v1/user')
@jwt_required()
def user():
    print(get_jwt_identity())
    if get_jwt_identity():
        userId, userFullName, userEmail = get_jwt_identity()
        user = Users(userId, userFullName, userEmail)
        return user.to_dict(), status.HTTP_200_OK
    else:
        return 'Invalid Token!', status.HTTP_400_BAD_REQUEST


# def generate_temp_auth_token():
#     user = Users('1', 'Shubham Kumar Singh', 'denyshubham@gmail.com')
#     auth_token = create_access_token(identity=[user.userId, user.userFullName, user.userEmail], expires_delta=False)  # jason web token  
#     return auth_token
  
if __name__=='__main__':
  jwtSampleToken = os.getenv('APP_JWT_SECRET', None)
  if jwtSampleToken is None:
    print("APP_JWT_SECRET environment variable not set")
  app.run(host="0.0.0.0", port=3000, debug=True)
