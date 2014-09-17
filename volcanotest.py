#This file doesn't actually play songs when run, you need to run these commands in order from idle

import playerVLC

player = playerVLC.volcanoPlayer()

player.auth( "jeffhoogland@linux.com", "turtlethesquirrel")
player.setStation(player.getStations()[0])
print player.getStation()
player.addSongs()
