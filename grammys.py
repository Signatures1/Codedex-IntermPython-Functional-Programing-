from functools import reduce
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]
def time_songs(song):
    return song[1] > 5

def convert_seconds(song):
    durration = song[1]
    minutes = int(durration)
    seconds = (durration - minutes) * 100

    return minutes * 60 + seconds

def add_time(total, song):
    duration = song[1]
    return total + duration

duration_songs = filter(time_songs, playlist)
seconds_songs = map(convert_seconds, playlist)
playtime_songs = reduce(add_time, playlist, 0)

print("Songs longer than 5 minutes:", list(duration_songs))
print("Songs in seconds:", list(seconds_songs))
print("Total playtime in seconds:", playtime_songs)