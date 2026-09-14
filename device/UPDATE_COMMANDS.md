# Device Update Command Structure — Pull New Enhancements
Numeral: 137451921129154222
Context: Existing non-empty profiles / factory already on device. Reconstruct for update (not fresh clone).

## 1. Primary Update Path (already cloned)
```bash
cd ~/sovereign-ai-factory-ai-polyglot   # or your actual path
git fetch origin
git pull origin main
chmod +x profiles/azazel/*.sh profiles/azazel/termux/*.sh 2>/dev/null || true
```

## 2. Safe Update + Re-launch Azazel
```bash
cd ~/sovereign-ai-factory-ai-polyglot
git stash push -m "device-local-$(date +%Y%m%d%H%M)" 2>/dev/null || true
git pull origin main
git stash pop 2>/dev/null || true
chmod +x profiles/azazel/*.sh 2>/dev/null || true
./profiles/azazel/azazel_wrapper.sh
```

## 3. Update Only Azazel Profile (sparse / targeted)
```bash
cd ~/sovereign-ai-factory-ai-polyglot
git fetch origin
git checkout origin/main -- profiles/azazel/
chmod +x profiles/azazel/*.sh 2>/dev/null || true
./profiles/azazel/azazel_wrapper.sh
```

## 4. Update Factory Packages + Bus + Catalogs
```bash
cd ~/sovereign-ai-factory-ai-polyglot
git fetch origin
git checkout origin/main -- packages/ bus/ docs/ enclaves/ sovereign_ai_factory_core.Ai
```

## 5. Full Reconstruct (if local drift is severe)
```bash
cd ~
mv sovereign-ai-factory-ai-polyglot sovereign-ai-factory-ai-polyglot.bak.$(date +%Y%m%d%H%M) 2>/dev/null || true
gh repo clone machackabook/sovereign-ai-factory-ai-polyglot
cd sovereign-ai-factory-ai-polyglot
chmod +x profiles/azazel/*.sh 2>/dev/null || true
./profiles/azazel/azazel_wrapper.sh
```

## 6. Trigger Remote Pipeline Then Pull
```bash
gh workflow run factory-device-pipeline.yml -f target=termux
# Wait ~30-60s, then:
cd ~/sovereign-ai-factory-ai-polyglot && git pull origin main
```

## 7. Bus-Aware Update (preserve local inbox/outbox)
```bash
cd ~/sovereign-ai-factory-ai-polyglot
cp -a bus/inbox bus/inbox.local 2>/dev/null || true
cp -a bus/outbox bus/outbox.local 2>/dev/null || true
git pull origin main
cp -n bus/inbox.local/* bus/inbox/ 2>/dev/null || true
```

## Notes
- Existing non-empty profiles are preserved by using `git pull` / `git checkout origin/main -- <path>` instead of wipe+clone.
- Local modifications can be stashed or backed up before pull.
- After any update, re-apply chmod and re-launch wrapper or boot hook.
- factory-device-pipeline continues to publish enhancements; device only needs to pull.
