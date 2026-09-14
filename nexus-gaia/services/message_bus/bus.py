"""Bidirectional message bus with replay protection and full envelope fields."""
from __future__ import annotations
import hashlib, json, secrets, time, uuid
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional

SYNC_STATES = ("DISCOVER", "AUTHENTICATE", "SYNC", "VERIFY", "ACK", "COMMIT")

@dataclass
class Message:
    message_id: str
    origin: str
    destination: str
    timestamp: str
    nonce: str
    parent_message: Optional[str]
    capability_scope: List[str]
    signature: str
    sync_state: str
    payload: Dict[str, Any] = field(default_factory=dict)
    acknowledgement: Dict[str, Any] = field(default_factory=lambda: {"acked": False, "acked_at": None, "acked_by": None})

    def to_dict(self) -> dict:
        return asdict(self)

class MessageBus:
    def __init__(self, replay_window_seconds: int = 300):
        self.replay_window = replay_window_seconds
        self._seen_nonces: Dict[str, float] = {}
        self._messages: Dict[str, Message] = {}
        self._order: List[str] = []

    def _sign(self, body: str) -> str:
        return hashlib.sha256(body.encode()).hexdigest()

    def _purge_old_nonces(self, now: float) -> None:
        cutoff = now - self.replay_window
        self._seen_nonces = {n: t for n, t in self._seen_nonces.items() if t >= cutoff}

    def publish(self, origin: str, destination: str, capability_scope: List[str], payload: Dict[str, Any], sync_state: str = "DISCOVER", parent_message: Optional[str] = None) -> Message:
        if sync_state not in SYNC_STATES:
            raise ValueError(f"invalid sync_state: {sync_state}")
        now = time.time()
        self._purge_old_nonces(now)
        nonce = secrets.token_hex(16)
        ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now))
        mid = str(uuid.uuid4())
        body = json.dumps({"message_id": mid, "origin": origin, "destination": destination, "timestamp": ts, "nonce": nonce, "payload": payload}, sort_keys=True)
        msg = Message(message_id=mid, origin=origin, destination=destination, timestamp=ts, nonce=nonce, parent_message=parent_message, capability_scope=capability_scope, signature=self._sign(body), sync_state=sync_state, payload=payload)
        self._seen_nonces[nonce] = now
        self._messages[mid] = msg
        self._order.append(mid)
        return msg

    def acknowledge(self, message_id: str, by: str) -> Message:
        if message_id not in self._messages:
            raise KeyError("unknown message_id")
        msg = self._messages[message_id]
        now = time.time()
        msg.acknowledgement = {"acked": True, "acked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)), "acked_by": by}
        return msg

    def accept_inbound(self, raw: dict) -> Message:
        required = ["message_id", "origin", "destination", "timestamp", "nonce", "capability_scope", "signature", "sync_state"]
        for k in required:
            if k not in raw:
                raise ValueError(f"missing field: {k}")
        now = time.time()
        self._purge_old_nonces(now)
        nonce = raw["nonce"]
        if nonce in self._seen_nonces:
            raise ValueError("replay detected: nonce already seen")
        parent = raw.get("parent_message")
        if parent and parent not in self._messages:
            raise ValueError("parent_message unknown — ordering violation")
        msg = Message(message_id=raw["message_id"], origin=raw["origin"], destination=raw["destination"], timestamp=raw["timestamp"], nonce=nonce, parent_message=parent, capability_scope=list(raw["capability_scope"]), signature=raw["signature"], sync_state=raw["sync_state"], payload=raw.get("payload") or {}, acknowledgement=raw.get("acknowledgement") or {"acked": False, "acked_at": None, "acked_by": None})
        self._seen_nonces[nonce] = now
        self._messages[msg.message_id] = msg
        self._order.append(msg.message_id)
        return msg

    def ordered(self) -> List[Message]:
        return [self._messages[i] for i in self._order if i in self._messages]
