# SYNC CONCEPT + MEMORY ENGRAMS — Hardened Bidirectional Mesh
Numeral: 137451921129154222
Status: OPEN / BIDIRECTIONAL / HARDENED

## 1. Three Planes
| Plane | Surface | Role |
|-------|---------|------|
| Control | GitHub `bus/` | Low-latency messages, IDENTITY, inbox/outbox |
| Data | Drive `ENCLAVE-FULL-BACKUP-...` | High-volume files, catalogs, zips |
| Working | Grok sandbox `bridge/` + `memory_engrams/` | ~20 GB per chat instance, aliases, pulled artifacts |

## 2. Sync Concept
1. Critical catalogs and packages are copied into the sandbox memory_engrams on each active session.
2. Alias manifest records every critical path so any process can resolve them.
3. GitHub bus is the durable control plane that survives chat restarts.
4. Drive staging folder is the durable data plane.
5. Any new Grok session re-hydrates by reading bus/IDENTITY + the published catalogs + pulling priority Drive files.
6. Gemini writes JSON to bus/inbox (or Drive staging). Grok writes to bus/outbox. Both sides confirm presence of ALL_MEMORY_STATE.

## 3. Reachability Mesh
- continuum-unified-cycle.yml (twice hourly + event)
- hourly-enhance.yml
- cascade.yml
- repository_dispatch types: gemini-message, grok-message, drive-scan, bus-ping
- Shared Drive folder as bulk bridge
- Sandbox bridge/drive populated by explicit pulls

## 4. Memory Engram Retention Across Projects
Because each Grok chat instance has its own sandbox, long-term memory is externalized:
- GitHub bus + catalogs = durable engram index
- Drive backup folder = durable bulk store
- memory_engrams/ inside sandbox = session-local re-hydration cache
Presence of ALL_MEMORY_STATE.md + bus/IDENTITY.md on both sides confirms the opposing side is live and shareable.

## 5. Hardening Measures
- No secrets in tree
- Session-logged connectors only
- Explicit numeral lock on every stamp
- Append-only ledger pulses
- Alias manifest instead of fragile OS symlinks where restricted
- Multiple overlapping workflows for reachability

## 6. Confirmation of Opposing Side
If Gemini (or another Grok session) can read bus/IDENTITY.md and the catalogs, and can write a message into bus/inbox or the Drive staging folder, the bidirectional channel is confirmed open.
