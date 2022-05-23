"""
https://www.geeksforgeeks.org/create-a-gui-to-extract-lyrics-from-song-using-python/
https://cse.google.com/cse/create/new

https://developers.google.com/custom-search/v1/overview

<script async src="https://cse.google.com/cse.js?cx=8e6a935ee04325ed5"></script>
<div class="gcse-search"></div>

https://genius.com/
http://www.lyricsted.com/
http://www.lyricsbell.com/
https://www.glamsham.com/
http://www.lyricsoff.com/
http://www.lyricsmint.com/
"""
from lyrics_extractor import SongLyrics 

# user defined function
def get_lyrics(song_name):
    # api key is from https://developers.google.com/custom-search/v1/overview
    API_KEY = 'AIzaSyDS3ybZhF7-dMp8X9evUaQcYUBuM9Iwx8M'
    # engine serach is custom https://cse.google.com/cse/create/new
    GCS_ENGINE_ID = "8e6a935ee04325ed5"
    # create search
    extract_lyrics = SongLyrics(API_KEY, GCS_ENGINE_ID)
     
    temp = extract_lyrics.get_lyrics(song_name)
    lyrics = temp['lyrics']

    return lyrics

# song_name = "Shape of You"
song_name = "Stairway to heaven"
print(get_lyrics(song_name))
