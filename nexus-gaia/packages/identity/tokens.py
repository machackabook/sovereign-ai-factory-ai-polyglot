"""Short-lived scoped tokens for nodes and AI agents. Never store master credentials."""
from __future__ import annotations
import hashlib, secrets, time
from dataclasses import dataclass
from typing import List

@dataclass
class ScopedToken:
    token_id: str
    subject: str
    scope: List[str]
    issued_at: float
    expires_at: float
    nonce: str

    def is_valid(self, now: float | None = None) -> bool:
        now = now or time.time()
        return now < self.expires_at

    def has_scope(self, required: str) -> bool:
        return required in self.scope or "*" in self.scope

def issue_token(subject: str, scope: List[str], ttl_seconds: int = 3600) -> ScopedToken:
    if ttl_seconds < 60 or ttl_seconds > 86400:
        raise ValueError("ttl_seconds must be between 60 and 86400")
    now = time.time()
    nonce = secrets.token_hex(16)
    raw = f"{subject}:{','.join(scope)}:{now}:{nonce}"
    token_id = hashlib.sha256(raw.encode()).hexdigest()[:32]
    return ScopedToken(token_id=token_id, subject=subject, scope=scope, issued_at=now, expires_at=now + ttl_seconds, nonce=nonce)
