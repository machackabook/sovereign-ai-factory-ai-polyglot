#!/usr/bin/env bash
# Fail-closed environment check. Source-only neighbor.
set -euo pipefail
NUMERAL="137451921129154222"
echo "[env-check] numeral=${NUMERAL}"
if [[ ! -f README.md ]]; then
  echo "[env-check] FAIL: missing README.md" >&2
  exit 1
fi
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[env-check] WARN: not a git work tree (catalog only)"
else
  sha=$(git rev-parse HEAD 2>/dev/null || true)
  if [[ -z "${sha}" || "${sha}" == "0000000000000000000000000000000000000000" ]]; then
    echo "[env-check] FAIL: empty SHA / point-zero null" >&2
    exit 1
  fi
  echo "[env-check] HEAD=${sha}"
fi
# Never print secrets even if present.
for k in CASCADE_TOKEN GH_TOKEN GITHUB_TOKEN GOOGLE_APPLICATION_CREDENTIALS; do
  if [[ -n "${!k:-}" ]]; then
    echo "[env-check] ${k}=set (value redacted)"
  else
    echo "[env-check] ${k}=unset"
  fi
done
echo "[env-check] OK"
