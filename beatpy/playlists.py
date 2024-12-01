import requests
from .exceptions import (
    BeatSaverError,
    BeatSaverNotFoundError,
    BeatSaverAuthError,
    BeatSaverRateLimitError,
    BeatSaverServerError,
)


class PlaylistsAPI:
    BASE_URL = "https://api.beatsaver.com"

    def __init__(self, session=None):
        self.session = session or requests.Session()

    def _handle_response(self, response):
        if response.status_code == 404:
            raise BeatSaverNotFoundError("Resource not found")
        elif response.status_code == 401:
            raise BeatSaverAuthError("Authentication failed")
        elif response.status_code == 429:
            raise BeatSaverRateLimitError("Rate limit exceeded")
        elif response.status_code >= 500:
            raise BeatSaverServerError("Server error")
        elif not response.ok:
            raise BeatSaverError(f"Unexpected error: {response.status_code}")
        return response.json()

    def get_latest_playlists(self):
        url = f"{self.BASE_URL}/playlists/latest"
        response = self.session.get(url)
        return self._handle_response(response)

    def search_playlists(self, page, query=None):
        url = f"{self.BASE_URL}/playlists/search/{page}"
        params = {"q": query} if query else {}
        response = self.session.get(url, params=params)
        return self._handle_response(response)

    def search_playlists_v1(self, page, query=None):
        url = f"{self.BASE_URL}/playlists/search/v1/{page}"
        params = {"q": query} if query else {}
        response = self.session.get(url, params=params)
        return self._handle_response(response)

    def get_playlists_by_user(self, user_id, page):
        url = f"{self.BASE_URL}/playlists/user/{user_id}/{page}"
        response = self.session.get(url)
        return self._handle_response(response)

    def get_playlist_detail(self, playlist_id, page):
        url = f"{self.BASE_URL}/playlists/id/{playlist_id}/{page}"
        response = self.session.get(url)
        return self._handle_response(response)
