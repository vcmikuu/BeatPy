import requests
from typing import List, Dict, Union
from .search import SearchAPI
from .exceptions import (
    BeatSaverError,
    BeatSaverNotFoundError,
    BeatSaverAuthError,
    BeatSaverRateLimitError,
    BeatSaverServerError,
)


BASE_URL = "https://api.beatsaver.com"

class BeatSaverAPI:
    def __init__(self):
        self.session = requests.Session()
        self.search = SearchAPI(self.session)

    def _handle_response(self, response):
        """Handles HTTP response and raises appropriate exceptions."""
        if response.status_code == 404:
            raise BeatSaverNotFoundError()
        elif response.status_code == 401 or response.status_code == 403:
            raise BeatSaverAuthError()
        elif response.status_code == 429:
            raise BeatSaverRateLimitError()
        elif 500 <= response.status_code < 600:
            raise BeatSaverServerError()
        elif not response.ok:
            raise BeatSaverError(f"Unexpected error: {response.text}", status_code=response.status_code)
        return response.json()

    def get_map_by_id(self, map_id: str) -> Dict:
        """Get map information by map ID."""
        response = self.session.get(f"{BASE_URL}/maps/id/{map_id}")
        return self._handle_response(response)

    def get_maps_by_ids(self, map_ids: List[str]) -> List[Dict]:
        """Get maps for multiple map IDs."""
        ids = ",".join(map_ids)
        response = self.session.get(f"{BASE_URL}/maps/ids/{ids}")
        return self._handle_response(response)

    def get_map_by_hash(self, hash_value: str) -> Dict:
        """Get map information by hash."""
        response = self.session.get(f"{BASE_URL}/maps/hash/{hash_value}")
        return self._handle_response(response)

    def get_maps_by_uploader(self, uploader_id: str, page: int = 0) -> Dict:
        """Get maps uploaded by a specific user."""
        response = self.session.get(f"{BASE_URL}/maps/uploader/{uploader_id}/{page}")
        return self._handle_response(response)
    
    def get_maps_with_collaborations(self, uploader_id: str) -> Dict:
        """Get maps by a user including collaborations."""
        response = self.session.get(f"{BASE_URL}/maps/collaborations/{uploader_id}")
        return self._handle_response(response)

    def get_latest_maps(self) -> Dict:
        """Get latest maps."""
        response = self.session.get(f"{BASE_URL}/maps/latest")
        return self._handle_response(response)

    def get_deleted_maps(self, date: str = "") -> Dict:
        """Get deleted maps since or before a certain date."""
        params = {"before": date} if date else {}
        response = self.session.get(f"{BASE_URL}/maps/deleted", params=params)
        return self._handle_response(response)

    def get_maps_by_play_count(self, page: int = 0) -> Dict:
        """Get maps ordered by play count."""
        response = self.session.get(f"{BASE_URL}/maps/plays/{page}")
        return self._handle_response(response)

    def get_user_by_id(self, user_id: str) -> Dict:
        """Get user information by user ID."""
        response = self.session.get(f"{BASE_URL}/users/id/{user_id}")
        return self._handle_response(response)

    def get_users_by_ids(self, user_ids: List[str]) -> List[Dict]:
        """Get user information for multiple user IDs."""
        ids = ",".join(user_ids)
        response = self.session.get(f"{BASE_URL}/users/ids/{ids}")
        return self._handle_response(response)

    def get_user_by_name(self, username: str) -> Dict:
        """Get user information by name."""
        response = self.session.get(f"{BASE_URL}/users/name/{username}")
        return self._handle_response(response)

    def verify_user_token(self, token: str) -> Dict:
        """Verify user token."""
        response = self.session.post(f"{BASE_URL}/users/verify", json={"token": token})
        return self._handle_response(response)
    

