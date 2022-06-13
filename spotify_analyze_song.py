import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pyqtgraph.examples

class Spotipy_Instance(): # Create env var SPOTIPY_CLIENT_ID SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI ( export SPOTIPY...=secret_value)

    scope = ["user-read-currently-playing", "user-read-playback-position", "user-read-playback-state"]
    spotipy = None
    played_id = 0
    raw_analysis = None
    raw_features = None
    player_time = None

    def __init__(self):
        self.spotipy = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))

    def update_current_song_id(self):
        results = self.spotipy.currently_playing(market='FR')
        self.played_id = results.get('item').get('id')
    
    def get_current_song_id(self):
        self.update_current_song_id()
        return self.played_id

    def get_current_song_analysis(self):
        self.update_current_song_id()
        self.raw_analysis = self.spotipy.audio_analysis(self.played_id)
        return self.raw_analysis

    def get_current_song_audio_features(self):
        self.update_current_song_id()
        self.raw_features = self.spotipy.audio_features(self.played_id)
        return self.raw_features

    def get_current_song_playback(self):
        self.update_current_song_id()
        self.song_playback = self.spotipy.current_playback(market='FR')
        return self.song_playback
    
    def get_current_song_time(self):
        self.update_current_song_id()
        self.player_time = self.spotipy.audio_features(self.played_id).get('progress_ms')
        return self.player_time

    def get_info_track(self):
        self.update_current_song_id()
        self.track = self.spotipy.track(self.played_id, market='FR')
        self.song_name = self.track.get('name')
        self.song_image = "image"
        self.song_artist = [self.track.get('artists')[i].get('name') for i in range(len(self.track.get('artists')))]
        self.song_popularity = self.track.get('popularity')
        return self.track
    
    def get_metadata(self):
        pass

    def update(self):
        self.get_current_song_analysis()
        self.get_current_song_time()


sp = Spotipy_Instance()
sp.get_info_track()
pyqtgraph.examples.run()