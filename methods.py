import random
import string
import config

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_source_track_path(track_path):
    full_path = config.source_folder + '/' + track_path
    return full_path

def get_dest_track_path(track_path):

    return