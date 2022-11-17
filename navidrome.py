import hashlib
from config import *
import favstofold
import requests


navidrome_salt = favstofold.get_random_string(5)
navidrome_password_salt = navidrome_password + navidrome_salt
navidrome_token = hashlib.md5(navidrome_password_salt.encode()).hexdigest()

navidrome_auth = "u=" + navidrome_username + "&t=" + navidrome_token + "&s=" + navidrome_salt + "&v=1.12.0&c=favstofold" 

def prepare_base_uri():
    navidrome_base_uri = navidrome_scheme + '://' + navidrome_host + ':' + navidrome_port + '/rest/'
    if(navidrome_scheme == 'https'):
        if(navidrome_port == '443'):
            navidrome_base_uri = navidrome_scheme + '://' + navidrome_host + '/rest/'
    return navidrome_base_uri

def prepare_call(endpoint):
    full_url = prepare_base_uri() + endpoint + '?' + navidrome_auth
    return full_url

def call(endpoint, arguments=""):
    full_url = prepare_call(endpoint)
    r = requests.get(full_url+arguments)
    # print(full_url+arguments)
    return r.text

def ping():
    return call('ping.view')

def getStarred():
    return call('getStarred')

def getMusicDirectory(id):
    arguments = "&id="+id
    return call('getMusicDirectory', arguments)