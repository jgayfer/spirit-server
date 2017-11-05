import requests
import json

from flask import Flask, request

app = Flask(__name__)
client_id = None
client_secret = None

@app.route("/oauth/")
def oauth():

    code = request.args.get('code')
    discord_id = request.args.get('state')

    r = requests.post('https://www.bungie.net/platform/app/oauth/token/',
                      data={'grant_type': 'authorization_code', 'code': code,
                            'client_id': client_id, 'client_secret': client_secret})

    json_res = r.json()
    membership_id = json_res['membership_id']
    access_token = json_res['access_token']
    refresh_token = json_res['refresh_token']

    return "<h1 style='color:blue'>Registration Complete!</h1>"


if __name__ == "__main__":
    with open('credentials.json') as f:
        cred_dict = json.load(f)
    client_id = cred_dict['client_id']
    client_secret = cred_dict['client_secret']
    app.run(host='0.0.0.0')
