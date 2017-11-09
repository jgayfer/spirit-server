# Spirit Server
A simple web server that powers OAuth2 functionality of Spirit.

This is not a standalone application. It is designed to be used in tandem with
[Spirit](https://github.com/jgayfer/spirit), a Discord bot for Destiny 2.

## Requirements
- Python 3.5+
- Pip
- Redis server
- Bungie.net app

## Installing Redis

Redis can be installed with:
```
$ sudo apt-get install redis-server
```
To verify that it has been installed correctly, type:
```
$ redis-server
```

## Creating a Bungie.net Application

Note that if you already have a Bungie.net application in use by Spirit, you don't need to create another one.

1. Navigate to https://www.bungie.net/en/Application
2. Sign in and create a new app
3. Set **OAuth Client Type** to **Confidential**
4. Set **Redirect URL** to https://127.0.0.1:5000/oauth
4. Under **Scope**, select all except the permission to move gear and items

## Running the Server

First, install the required Python libraries
```
$ sudo pip3 install -r requirements.txt
```

Next, create a `credentials.json` file in the root directory of this project. It will contain your
Bungie application's client id and secret.
```
{
  "client_id": "your-client-id",
  "client_secret": "your-client-secret"
}
```

Then the server can be run with:
```
$ python3 server.py
```

By default, the server will run at `http://127.0.0.1:5000`

**Note:** Keep in mind that Bungie will redirect to this web server with HTTPS. However, this app is only setup
for HTTP by default, so you'll need to change the link in your browser from HTTPS to HTTP in order
for the authorization to work.
