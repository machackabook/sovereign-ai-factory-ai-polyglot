# GODMODE.md — Azazel Continuity Profile (Debloated + Hardened)
Numeral: 137451921129154222
Marker: pickle-rick
Mode: GodMode | Sensor Flux | Auto-start ready

## Launch (Termux / YOLO-style)
```bash
cd sovereign-ai-factory-ai-polyglot/profiles/azazel
chmod +x *.sh termux/*.sh 2>/dev/null || true
./azazel_wrapper.sh
# or
bash azazel.sh
```

## Auto-trigger on start / boot (Termux)
Place in `~/.termux/boot/` or use Termux:Boot:
```bash
#!/data/data/com.termux/files/usr/bin/sh
termux-wake-lock
cd $HOME/sovereign-ai-factory-ai-polyglot/profiles/azazel
exec ./azazel_wrapper.sh
```

## Core Principles (abide)
- Legal surfaces only
- No secret keys committed
- Public / advisory financial signals only
- Continuity ledger + numeral lock
- Bidirectional bus remains open

## Features enabled
- Pickle-Rick command-first vibe
- Sensor-aware color flux (Termux light sensor or time)
- Gemini CLI wrapper (azazel-gemini.sh)
- OpenAI-compatible wrapper stub
- MCP server placeholders (always-on pattern)
- Wake-lock + on-boot hooks
- Redundant enhance/advance self-pathing via bus + catalogs
