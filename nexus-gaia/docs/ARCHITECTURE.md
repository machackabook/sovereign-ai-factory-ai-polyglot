# Nexus/Gaia Architecture — Cloud-First Control Plane

**Numeral lock (Continuity):** 137451921129154222  
**Boundary:** Strict public / private. Google Drive = cloud storage, not a security boundary.  
**Enclave / sparsebundle:** Encrypted; never exposed directly to external AI agents.

## Planes

| Plane | Role |
|-------|------|
| Control | Gateway + Message Bus + short-lived scoped tokens |
| Data | Virtual NAS / Drive references (no secrets in git) |
| Memory | Memory Fabric (engrams as references + hashes) |
| Mesh | Node heartbeats, capability advertisement |
| Client | Canvas (visualization only; no root keys) |

## Sync state machine
`DISCOVER → AUTHENTICATE → SYNC → VERIFY → ACK → COMMIT`

## Payment rule
Payment execution is **never** a side-effect of heartbeat or ordinary bus events. It requires a separate authenticated, auditable authorization path and capability `payment.authorize`.

## Recovery
Account recovery uses independent authorized identities. Master credentials are never duplicated between accounts.

## Canvas API contract
Gateway: authenticate → scoped token → send/heartbeat. Bootstrap may be a data URL of **public** config only.
