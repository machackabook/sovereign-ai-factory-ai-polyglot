#!/usr/bin/env sh
# azazel-gemini — enhanced Continuity wrapper
# Numeral: 137451921129154222 | Marker: pickle-rick
set +e; set +u
AE="${AE:-$HOME/Æ}"
[ -f "$AE/system/env.sh" ] && . "$AE/system/env.sh" >/dev/null 2>&1 || true
export AZAZEL_MARKER="${AZAZEL_MARKER:-pickle-rick}"
PREFIX="You are AZAZEL interface (Continuity / 137451921129154222). Pickle Rick vibe, command-first, legal only. "
q="${*:-Say hello as Pickle Rick and list available Nexus/Continuity commands.}"
if command -v gemini >/dev/null 2>&1; then
  gemini "${PREFIX}${q}"
elif command -v gmni >/dev/null 2>&1; then
  gmni "${PREFIX}${q}"
elif command -v openai >/dev/null 2>&1; then
  openai api chat.completions.create -m gpt-4o-mini -g user "${PREFIX}${q}"
else
  echo "[azazel-gemini] gemini/gmni/openai not found. Prompt would be:"
  echo "${PREFIX}${q}"
fi
