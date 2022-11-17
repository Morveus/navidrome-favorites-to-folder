# navidrome-favorites-to-folder
Script making copies of your "favorites" in Navidrome to a specified folder. Useful for syncing with portable music players.

# DISCLAIMER
THIS SCRIPT IS PROVIDED AS-IS.

IT'S BEEN BADLY AND QUICKLY WRITTEN.

MAKE SURE YOU KNOW WHAT YOU'RE DOING BEFORE ALLOWING A STRANGER'S SCRIPT TO COPY OR DELETE FILES ON YOUR FILESYSTEM.

THIS SCRIPT HAS ONLY BEEN TESTED ON LINUX AND PROBABLY WON'T WORK ON A WINDOWS SYSTEM WITHOUT A FEW TWEAKS.

# Why
I have a Syncthing instance running on my home cluster, which syncs a music folder to my FiiO M17 portable music player. Before going offline on vacation, I simply have to star (or "like" <3) artists and albums on Navidrome to have them synced with my player.

# Setup
Create a `config.py` file and set your Navidrome username and password (see `config.py.sample`)

Run `pip install -r requirements.txt`

# Real paths
* Run ping: `python3 ping.py`
* This will ping your Navidrome instance
* Go to "Your account" > "Players"
* Click "favstofold [python-requests]"
* Check the "Report Real Path" option
* Save

# Run
Run `python3 run.py`

# Known issues (on Navidrome's side)
Make sure your username in `config.py` is exactly the same as known by Navidrome. 

Using "Morveus" in this script instead of "morveus" (my username in my Navidrome instance) won't allow the script to regsiter as a player.

# Known issues (on my side)
The script will definitely NOT work correctly if you haven't found `favstofold` in your Navidrome players and checked "Report Real Path"