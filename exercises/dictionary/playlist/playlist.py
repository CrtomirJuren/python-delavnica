"""
vaje za list in dictionary
# playlist = list
# song = dictionary
"""
# -- imports ---
from lyrics_extractor import SongLyrics

# --- functions ---
def get_lyrics(title):
    # api key is from https://developers.google.com/custom-search/v1/overview
    API_KEY = 'AIzaSyDS3ybZhF7-dMp8X9evUaQcYUBuM9Iwx8M'
    # engine serach is custom https://cse.google.com/cse/create/new
    GCS_ENGINE_ID = "8e6a935ee04325ed5"
    # create search
    extract_lyrics = SongLyrics(API_KEY, GCS_ENGINE_ID)

    temp = extract_lyrics.get_lyrics(title)
    lyrics = temp['lyrics']

    return lyrics

"""
Napiši funkcijo poišči, ki kot argument sprejme playlisto in izvajalca.
Če izvajalca je v playlisti, ga izbriši in o tem opozori uporabnika. ('song added')
Če izvajalca ni samo opozori. ('song already in playlist')
"""
def add_song(playlist:list, title:str,band:str)->list:
    """ add song to playlist """
    song = {'title': title, 'band': band}
    playlist.append(song)

"""
Napiši funkcijo poišči, ki kot argument sprejme playlisto in izvajalca.
Če izvajalca je v playlisti, ga izbriši in o tem opozori uporabnika. ('song removed')
Če izvajalca ni samo opozori. ('song not in playlist')
"""
def remove_song(playlist:list, title:str,band:str)->None:
    """ remove song from playlist """
    # search song
    for song in playlist:
        if song == {'title': title, 'band': band}:
            playlist.remove(song)

def remove_song_by_title(playlist:list, title:str)->None:
    """ remove song from playlist """
    # search song
    for song in playlist:
        for key in song.keys():
            if song[key] == title:
                playlist.remove(song)

"""
Napiši funkcijo poišči, ki kot argument sprejme playlisto in izvajalca.
Če izvajalca ni na playlisti vrni False, če ne pa vrni index pesmi
"""
def find_by_author(playlist, author):
    """ search playlist by author """
    pass

"""
funkcija ki kot argument sprejme song,
in pesem prikaže v terminalu v obliki
'ime pesmi' by 'band'
"""
def format_song(song:dict)->str:
    """ song to formatted string
        'naslov pesmi' by 'ime banda'
    """
    return song['title'] + ' by ' + song['band']

"""
funkcija ki kot argument sprejme playlist,
in vsako pesem posebej prikaže v terminalu.
uporabi funkcijo format_song
"""
def print_playlist(playlist:list)->None:
    for song in playlist:
        print(format_song(song))

# --- začetek programa ---
top_ten_rock = []

add_song(top_ten_rock, 'All My Life', 'Foo Fighters')
add_song(top_ten_rock, 'Stairway to Heaven', 'Led Zeppelin')
add_song(top_ten_rock, 'Black', 'Pearl Jam')
add_song(top_ten_rock, 'Smells like teen spirit', 'Nirvana')
print_playlist(top_ten_rock)

print('----')

remove_song(top_ten_rock, 'Black', 'Pearl Jam')
print('----')
remove_song_by_title(top_ten_rock, 'Stairway to Heaven')

# z uporabo fukcije get_lirics pridobi besedilo
lyrics = get_lyrics('Smells like teen spirit')
print(lyrics)



