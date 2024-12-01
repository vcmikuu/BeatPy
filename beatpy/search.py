import requests
from .exceptions import (
    BeatSaverError,
    BeatSaverNotFoundError,
    BeatSaverAuthError,
    BeatSaverRateLimitError,
    BeatSaverServerError,
)

class SearchAPI:
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

    def search_maps(
        self,
        page=0,
        q=None,
        automapper=None,
        chroma=None,
        cinema=None,
        curated=None,
        environments=None,
        followed=None,
        from_date=None,
        fullSpread=None,
        leaderboard=None,
        maxBpm=None,
        maxDuration=None,
        maxNps=None,
        maxRating=None,
        me=None,
        minBpm=None,
        minDuration=None,
        minNps=None,
        minRating=None,
        noodle=None,
        sortOrder="Latest",
        tags=None,
        to_date=None,
        verified=None,
    ):

        url = f"{self.BASE_URL}/search/text/{page}"
        params = {
            "q": q,
            "automapper": automapper,
            "chroma": chroma,
            "cinema": cinema,
            "curated": curated,
            "environments": environments,
            "followed": followed,
            "from": from_date,
            "fullSpread": fullSpread,
            "leaderboard": leaderboard,
            "maxBpm": maxBpm,
            "maxDuration": maxDuration,
            "maxNps": maxNps,
            "maxRating": maxRating,
            "me": me,
            "minBpm": minBpm,
            "minDuration": minDuration,
            "minNps": minNps,
            "minRating": minRating,
            "noodle": noodle,
            "sortOrder": sortOrder,
            "tags": tags,
            "to": to_date,
            "verified": verified,
        }

        params = {k: v for k, v in params.items() if v is not None}

        response = self.session.get(url, params=params)
        return self._handle_response(response)
