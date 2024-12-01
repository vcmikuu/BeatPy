class BeatSaverError(Exception):
    """Base exception for BeatSaver API errors."""
    def __init__(self, message: str, status_code: int = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        if self.status_code:
            return f"[HTTP {self.status_code}] {self.message}"
        return self.message


class BeatSaverNotFoundError(BeatSaverError):
    """Exception raised when a resource is not found (HTTP 404)."""
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)


class BeatSaverAuthError(BeatSaverError):
    """Exception raised for authentication errors (HTTP 401/403)."""
    def __init__(self, message: str = "Authentication error"):
        super().__init__(message, status_code=401)


class BeatSaverRateLimitError(BeatSaverError):
    """Exception raised for rate limit errors (HTTP 429)."""
    def __init__(self, message: str = "Rate limit exceeded"):
        super().__init__(message, status_code=429)


class BeatSaverServerError(BeatSaverError):
    """Exception raised for server errors (HTTP 5xx)."""
    def __init__(self, message: str = "Server error"):
        super().__init__(message, status_code=500)
