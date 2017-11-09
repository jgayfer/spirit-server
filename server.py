import requests
import json
import pickle

from flask import Flask, request
import redis


app = Flask(__name__)
red = redis.StrictRedis(host='localhost', port=6379, db=0)

with open('credentials.json') as f:
    cred_dict = json.load(f)
    client_id = cred_dict['client_id']
    client_secret = cred_dict['client_secret']

@app.route("/")
@app.route("/oauth/")
def oauth():

    if 'code' not in request.args or 'state' not in request.args:
        return "<h1 style='color:blue'>Missing Code or State</h1>"

    code = request.args.get('code')
    discord_id = request.args.get('state')
    r = requests.post('https://www.bungie.net/platform/app/oauth/token/',
                      data={'grant_type': 'authorization_code', 'code': code,
                            'client_id': client_id, 'client_secret': client_secret})
    json_res = r.json()

    # Check response from Bungie
    if not all(k in json_res for k in ("access_token", "refresh_token", "membership_id")):
        return "<h1 style='color:blue'>Bad response from Bungo</h1>"

    # Extract user info
    membership_id = json_res['membership_id']
    access_token = json_res['access_token']
    refresh_token = json_res['refresh_token']
    user_info = {}
    for i in ('membership_id', 'access_token', 'refresh_token'):
        user_info[i] = locals()[i]

    # Pickle info and send to Redis
    pickled_info = pickle.dumps(user_info)
    #red.set(discord_id, pickled_info)
    red.publish(discord_id, pickled_info)

    return "<h1 style='color:blue'>Registration Complete!</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
