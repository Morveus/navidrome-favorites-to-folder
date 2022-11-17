# DISCLAIMER
THIS SCRIPT IS PROVIDED AS-IS.

IT'S BEEN BADLY AND QUICKLY WRITTEN.

MAKE SURE YOU KNOW WHAT YOU'RE DOING BEFORE ALLOWING A STRANGER'S SCRIPT TO COPY OR DELETE FILES ON YOUR FILESYSTEM.

# navidrome-favorites-to-folder
Script making copies of your "favorites" in Navidrome to a specified folder. Useful for syncing with portable music players.

# Why
I have a Syncthing instance running on my home cluster, which syncs a music folder to my FiiO M17 portable music player. Before going offline on vacation, I simply have to star (or "like" <3) artists and albums on Navidrome to have them synced with my player.

# Setup
Create a `config.py` file and set your Navidrome username and password (see `config.py.sample`)

Run `pip install -r requirements.txt`

# Run
Run `python3 run.py`

# Real paths
* Run the script once
* Go to "Your account" > "Players"
* Click "favstofold [python-requests]"
* Check the "Report Real Path" option
* Save

# Known issues
Make sure your username in `config.py` is exactly the same as known by Navidrome. 

Using "Morveus" in this script instead of "morveus" (my username in my Navidrome instance) won't allow the script to regsiter as a player.