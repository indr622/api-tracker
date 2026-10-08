#!/bin/sh
# Usage: scripts/commit.sh <chore|feature|bugfix|fix> "pesan"
# Auto add, commit (semantic) dan push.
set -e
type="$1"; shift
case "$type" in chore|feature|bugfix|fix) ;; *) echo "type harus chore|feature|bugfix|fix" >&2; exit 1;; esac
git add -A
git commit -m "$type: $*"
git push
