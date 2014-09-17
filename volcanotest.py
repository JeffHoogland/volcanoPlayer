import playerVLC

player = playerVLC.volcanoPlayer()

player.auth( "jeffhoogland@linux.com", "turtlethesquirrel")
player.setStation(player.getStations()[0])
print player.getStation()
player.addSongs()
