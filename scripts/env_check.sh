#!/usr/bin/env bash
set -euo pipefail
echo "[sSoS] env check — numeral 137451921129154222"
echo "pwd=$(pwd)"
echo "python=$(command -v python3 || echo missing)"
echo "git=$(git rev-parse --short HEAD 2>/dev/null || echo nogit)"
test -f sovereign_ai_factory_core.Ai && echo "core=present" || echo "core=MISSING"
mkdir -p docs/ledgers scripts .github/workflows
echo "[sSoS] env check ok"
