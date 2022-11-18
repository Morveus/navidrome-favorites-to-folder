import random
import string
import config
import os
import shutil

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def strip_navidrome_mount(track_path):
    # Replacing Navidrome host's internal mount path by this host's mount point
    clean_path = track_path.replace(config.mount_folder, '', 1)

    return clean_path

def get_source_track_path(track_path):
    clean_track_path = strip_navidrome_mount(track_path)
    slash = "/"

    if(config.source_folder.endswith('/') or clean_track_path.startswith('/')):
        slash = ""

    full_path = config.source_folder + slash + clean_track_path
    return full_path

def get_dest_track_path(track_path):
    clean_track_path = strip_navidrome_mount(track_path)
    slash = "/"

    if(config.destination_folder.endswith('/') or clean_track_path.startswith('/')):
        slash = ""

    full_path = config.destination_folder + slash + clean_track_path

    return full_path

def get_dest_single_track_folder():
    slash = "/"

    if(config.destination_folder.endswith('/') or config.single_tracks_folder.startswith('/')):
        slash = ""

    full_path = config.destination_folder + slash + config.single_tracks_folder

    return full_path

def get_dest_single_path(filename):
    dest_folder = get_dest_single_track_folder()
    dest_path = dest_folder+"/"+filename
    return dest_path

def get_dest_folder_path(track_path):
    path = '/'.join(get_dest_track_path(track_path).split('/')[0:-1])
    return path

def destination_exists(track_path):
    if(os.path.exists(get_dest_track_path(track_path))):
        return True
    return False

def destination_identical(track_path, destination=False):
    if destination == False:
        destination = track_path
    if(destination_exists(destination)):
        source_size = os.path.getsize(get_source_track_path(track_path))
        dest_size = os.path.getsize(get_dest_track_path(destination))
        if(source_size == dest_size):
            return True

    return False

def copy_track(track_path, single, filename):
    source_path = get_source_track_path(track_path)
    dest_path = get_dest_track_path(track_path)
    dest_folder = get_dest_folder_path(track_path)

    if single:
        dest_folder = get_dest_single_track_folder()
        dest_path = dest_folder+"/"+filename

    os.makedirs(dest_folder, exist_ok=True)
    shutil.copyfile(source_path, dest_path)
    return