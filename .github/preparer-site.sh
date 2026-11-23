#!/usr/bin/env bash
set -euo pipefail

rsync -a --delete --delete-excluded \
  --include='/.nojekyll' --include='/*.html' \
  --include='/manifest.webmanifest' --include='/sw.js' \
  --include='/chansons/***' --include='/css/***' --include='/icones/***' \
  --include='/js/***' --include='/lib/***' --include='/polices/***' --exclude='*' ./ _site/

revision=${GITHUB_SHA:-$(git rev-parse HEAD)}
sed -i "s/^const VERSION = .*/const VERSION = \"${revision:0:12}\";/" _site/sw.js
grep -q "^const VERSION = \"${revision:0:12}\";" _site/sw.js
