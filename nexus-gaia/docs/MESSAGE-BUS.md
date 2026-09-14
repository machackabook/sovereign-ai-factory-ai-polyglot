# Message Bus

Envelope fields: message_id, origin, destination, timestamp, nonce, parent_message, capability_scope, signature, acknowledgement, sync_state, payload.

## Security
- Replay protection via nonce window
- Ordering via parent_message chain
- Signature over canonical body (production: real HMAC/KMS keys outside repo)
- Acknowledgement explicit

## Channels
Bidirectional. External participants connect only through the Gateway.
