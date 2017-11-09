# Spirit Server
A simple web server that powers OAuth2 functionality of Spirit.

## Requirements
- Python 3.5+
- Pip
- Redis server

## Installing Redis

Redis can be installed with
```
$ sudo apt-get install redis-server
```
To verify that it has been installed correctly, type:
```
$ redis-server
```
If Redis starts up, then you're good to go!

## Running the Server

First, install the required Python libraries
```
$ sudo pip3 install -r requirements.txt
```

Then the server can be run with
```
$ python3 server.py
```
