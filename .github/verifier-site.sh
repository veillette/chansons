#!/usr/bin/env bash
set -euo pipefail

python3 outils/verifier.py
node --test outils/tests/*.test.js
python3 outils/illustrer/generer.py >/dev/null
if [ -n "$(git status --porcelain -- ':(glob)chansons/**/images/*.svg')" ]; then
  echo "Les illustrations diffèrent du générateur. Vérifier le résultat."
  git status --short -- ':(glob)chansons/**/images/*.svg'
  exit 1
fi
