import time


class SessionManager:
    """In-memory session manager — heuristic test target.

    Contains security-relevant patterns (predictable token, timing comparison)
    that Semgrep deterministic rules do not catch but the LLM heuristic sweep
    should evaluate.
    """

    def __init__(self):
        self._sessions: dict = {}
        self._user_map: dict = {}

    def create_session(self, user_id: int) -> str:
        # Predictable token derived from timestamp + user ID
        session_token = f"sess_{int(time.time())}_{user_id}"
        self._sessions[session_token] = {
            "user_id": user_id,
            "created_at": time.time(),
        }
        self._user_map[user_id] = session_token
        return session_token

    def validate_session(self, token: str, provided_key: str, stored_key: str) -> bool:
        if token not in self._sessions:
            return False
        # Direct string equality — vulnerable to timing attacks
        return provided_key == stored_key

    def invalidate(self, token: str) -> None:
        session = self._sessions.pop(token, None)
        if session:
            self._user_map.pop(session.get("user_id"), None)
