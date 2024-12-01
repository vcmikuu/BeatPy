# BeatPy
A Python wrapper for the BeatSaver API

## Installation

Install the `beatpy` package using pip:

```bash
pip install beatpy
```

or install it using GIT:
```bash
pip install git+https://github.com/vcmikuu/BeatPy
```


## Getting Started

First, import the `BeatSaverAPI` class and initialize the API client:

```python
from beatpy import BeatSaverAPI

# Initialize the API client
api = BeatSaverAPI()
```


## Maps and User Functions

### Retrieve Map Information by ID

Get detailed information about a map using its unique ID:

```python
# Get map details by ID
map_id = "12345"
map_details = api.search.get_map_by_id(map_id)

# Print map details
print("Map Details:")
print(map_details)
```


### Retrieve Multiple Maps by IDs

Fetch details for multiple maps at once using their IDs:

```python
# Get details for multiple maps
map_ids = ["12345", "67890", "54321"]
maps_details = api.search.get_maps_by_ids(map_ids)

# Print details for each map
print("Maps Details:")
for map_info in maps_details:
    print(f"- {map_info['name']} (ID: {map_info['id']})")
```


### Retrieve Map by Hash

Find a map using its unique hash value:

```python
# Get map by hash
map_hash = "abcdef1234567890abcdef1234567890"
map_info = api.search.get_map_by_hash(map_hash)

# Print map information
print("Map Info by Hash:")
print(map_info)
```


### Retrieve Maps by Uploader

Get all maps uploaded by a specific user:

```python
# Get maps uploaded by a specific user
uploader_id = "user123"
uploader_maps = api.search.get_maps_by_uploader(uploader_id, page=0)

# Print uploaded maps
print("Uploader Maps:")
for map_info in uploader_maps.get('docs', []):
    print(f"- {map_info['name']} (ID: {map_info['id']})")
```


### Retrieve Maps with Collaborations

Fetch maps created by a user, including collaborations:

```python
# Get collaborative maps for a user
uploader_id = "user123"
collab_maps = api.search.get_maps_with_collaborations(uploader_id)

# Print collaborative maps
print("Collaborative Maps:")
for map_info in collab_maps.get('docs', []):
    print(f"- {map_info['name']} (Collaborators: {map_info['collaborators']})")
```


### Retrieve Latest Maps

Get the most recently created or updated maps:

```python
# Fetch the latest maps
latest_maps = api.search.get_latest_maps()

# Print the latest maps
print("Latest Maps:")
for map_info in latest_maps.get('docs', []):
    print(f"- {map_info['name']} (Uploaded: {map_info['uploaded']})")
```


### Retrieve Deleted Maps

Fetch maps that have been deleted, optionally filtered by date:

```python
# Get deleted maps since a specific date
deleted_maps = api.search.get_deleted_maps(date="2023-01-01")

# Print deleted maps
print("Deleted Maps:")
for map_info in deleted_maps.get('docs', []):
    print(f"- {map_info['name']} (Deleted: {map_info['deleted_at']})")
```


### Retrieve Maps by Play Count

Find maps sorted by their total play count:

```python
# Get maps ordered by play count
popular_maps = api.search.get_maps_by_play_count(page=0)

# Print popular maps
print("Popular Maps:")
for map_info in popular_maps.get('docs', []):
    print(f"- {map_info['name']} (Plays: {map_info['stats']['plays']})")
```


### Retrieve User Information by ID

Fetch details about a specific user using their ID:

```python
# Get user details by ID
user_id = "user123"
user_details = api.search.get_user_by_id(user_id)

# Print user details
print("User Details:")
print(user_details)
```


### Retrieve Multiple Users by IDs

Fetch details for multiple users by their IDs:

```python
# Get user details for multiple IDs
user_ids = ["user123", "user456", "user789"]
users_details = api.search.get_users_by_ids(user_ids)

# Print details for each user
print("Users Details:")
for user in users_details:
    print(f"- {user['name']} (ID: {user['id']})")
```


### Retrieve User Information by Username

Find a user by their username:

```python
# Get user details by username
username = "example_user"
user_info = api.search.get_user_by_name(username)

# Print user information
print("User Info by Username:")
print(user_info)
```


### Verify User Token

Verify the authenticity of a user token:

```python
# Verify a user token
token = "your_auth_token"
verification_result = api.search.verify_user_token(token)

# Print verification result
print("Verification Result:")
print(verification_result)
```

## Search Functions

### Retrieve Latest Maps

Get the most recently created or updated maps:

```python
# Fetch the latest maps
latest_maps = api.search.search_maps(page=1, sortOrder="Latest")

# Print the results
print("Latest Maps:")
for map_item in latest_maps.get('docs', []):
    print(f"- {map_item['name']} (ID: {map_item['id']})")
```

---

### Search Maps by Keyword

Search for maps using a specific keyword:

```python
# Search for maps with the keyword "retro" on the first page
search_results = api.search.search_maps(page=1, q="retro", sortOrder="Latest")

# Print the search results
print("Search Results:")
for map_item in search_results.get('docs', []):
    print(f"- {map_item['name']} by {map_item['uploader']}")
```


### Filter Maps by BPM Range

Find maps that fall within a specific BPM range:

```python
# Search for maps with BPM between 120 and 150
bpm_filtered_maps = api.search.search_maps(page=1, minBpm=120, maxBpm=150, sortOrder="Rating")

# Print the results
print("Maps with BPM 120-150:")
for map_item in bpm_filtered_maps.get('docs', []):
    print(f"- {map_item['name']} (BPM: {map_item['bpm']})")
```


### Retrieve Verified Maps

Retrieve maps that have been verified:

```python
# Search for verified maps
verified_maps = api.search.search_maps(page=1, verified=True, sortOrder="Plays")

# Print the verified maps
print("Verified Maps:")
for map_item in verified_maps.get('docs', []):
    print(f"- {map_item['name']} by {map_item['uploader']} (Verified: {map_item['verified']})")
```


### Search Maps by Date Range

Find maps uploaded within a specific date range:

```python
# Search for maps uploaded in 2023
date_filtered_maps = api.search.search_maps(page=1, from_date="2023-01-01", to_date="2023-12-31", sortOrder="Latest")

# Print the results
print("Maps from 2023:")
for map_item in date_filtered_maps.get('docs', []):
    print(f"- {map_item['name']} (Uploaded: {map_item['uploaded']})")
```


### Combine Multiple Filters

Search for maps with multiple filters applied:

```python
# Search for chroma-enabled maps with a rating of 4.5 or higher
filtered_maps = api.search.search_maps(page=1, chroma=True, minRating=4.5, sortOrder="Rating")

# Print the results
print("Chroma Maps with High Ratings:")
for map_item in filtered_maps.get('docs', []):
    print(f"- {map_item['name']} by {map_item['uploader']} (Rating: {map_item['stats']['rating']})")
```

## Playlists Functions

### Retrieve Latest Playlists

Get the most recently created or updated playlists:

```python
# Fetch the latest playlists
latest_playlists = api.playlists.get_latest_playlists()

# Print the results
print("Latest Playlists:")
for playlist in latest_playlists.get('docs', []):
    print(f"- {playlist['name']} (ID: {playlist['id']})")
```


### Search Playlists

Search for playlists using flexible parameters:

```python
# Search playlists with the keyword "fun" on the first page
search_results = api.playlists.search_playlists(page=0, query="fun")

# Print the search results
print("Search Results:")
for playlist in search_results.get('docs', []):
    print(f"- {playlist['name']} by {playlist['author']}")
```

You can also use the `search_playlists_v1` method for an alternate version of the search endpoint:

```python
# Search playlists using the v1 endpoint
search_results_v1 = api.playlists.search_playlists_v1(page=0, query="challenge")

# Print the results
print("Search Results (v1):")
for playlist in search_results_v1.get('docs', []):
    print(f"- {playlist['name']} (Tags: {', '.join(playlist.get('tags', []))})")
```


### Get Playlists by User

Fetch playlists created by a specific user:

```python
# Fetch playlists created by a user with ID "12345"
user_playlists = api.playlists.get_playlists_by_user(user_id="12345", page=0)

# Print the user's playlists
print("User Playlists:")
for playlist in user_playlists.get('docs', []):
    print(f"- {playlist['name']} (Created: {playlist['createdAt']})")
```


### Get Playlist Details

Access detailed information about a specific playlist:

```python
# Get details for a playlist with ID "abc123"
playlist_details = api.playlists.get_playlist_detail(playlist_id="abc123", page=0)

# Print the playlist details
print("Playlist Details:")
print(f"Name: {playlist_details['name']}")
print(f"Author: {playlist_details['author']}")
print(f"Description: {playlist_details['description']}")
print(f"Maps: {len(playlist_details['maps'])} songs")
```


## Error Handling

The package includes custom exceptions for handling common API errors:

```python
try:
    # Fetch playlists or perform some other API operation
    playlists = api.playlists.get_latest_playlists()
except BeatSaverNotFoundError:
    print("The requested resource was not found.")
except BeatSaverAuthError:
    print("Authentication failed.")
except BeatSaverRateLimitError:
    print("Rate limit exceeded. Please try again later.")
except BeatSaverServerError:
    print("The server encountered an error.")
except BeatSaverError as e:
    print(f"An unexpected error occurred: {e}")
```


## Contribution

If you’d like to contribute to the `beatpy` package, feel free to submit a pull request or open an issue!

