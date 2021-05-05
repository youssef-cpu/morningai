import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from flask import Flask, json,request, jsonify
import random


cred = credentials.Certificate("./morningstar-sdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
# uid = "bdmUTvZQrsMFc6YE0sZcOAjJp633"

# user = auth.get_user(uid)
# print(user.email)
# print('Successfully fetched user data: {0}'.format(user.uid))

# api = Flask(__name__)

api = Flask(__name__)
@api.route('/GenProg', methods=['POST'])
def post_GenProg():
    liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    prog = random.choice(liste)
    print (prog)
    data = request.json
    uid = data.get('uid')
    city_ref = db.collection(u'users').document(uid)
    city_ref.set({
        u'Programe': prog
    }, merge=True)
    return data.get('uid')

if __name__ == '__main__':
    api.run()
