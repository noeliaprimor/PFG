#!/usr/bin/env bash
set -euo pipefail

# Auto backup script for the repo
# Usage:
#  - Configure remote and branch via env vars: GIT_REMOTE (default: origin), GIT_BRANCH (default: main)
#  - Run this from cron or systemd timer

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

REMOTE=${GIT_REMOTE:-origin}
BRANCH=${GIT_BRANCH:-main}

# Ensure we're inside a git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[auto_backup] ERROR: not a git repository: $REPO_DIR" >&2
  exit 1
fi

# Make sure remote exists (optional)
if ! git remote | grep -q "^${REMOTE}$"; then
  echo "[auto_backup] WARNING: remote '${REMOTE}' not configured. Add it with: git remote add ${REMOTE} <URL>" >&2
fi

# Avoid committing unintentional big files: leave that decision to .gitignore and LFS

# If there are changes, commit and push
if git status --porcelain | grep -q .; then
  echo "[auto_backup] Changes detected. Committing and pushing..."
  git add -A
  TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  git commit -m "backup: automated ${TIMESTAMP}"

  # Push with a few retries
  for i in 1 2 3; do
    if git push "$REMOTE" "HEAD:${BRANCH}"; then
      echo "[auto_backup] Push succeeded"
      exit 0
    else
      echo "[auto_backup] Push attempt ${i} failed, retrying..." >&2
      sleep 5
    fi
  done
  echo "[auto_backup] ERROR: push failed after retries" >&2
  exit 2
else
  echo "[auto_backup] No changes. Nothing to do."
fi
