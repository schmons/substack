#!/usr/bin/env bash
# Usage: ./new-article.sh my-article-slug
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 <slug>" >&2
  exit 1
fi

root="$(cd "$(dirname "$0")" && pwd)"
dest="$root/articles/$(date +%Y-%m)-$1"

if [ -e "$dest" ]; then
  echo "Already exists: $dest" >&2
  exit 1
fi

cp -r "$root/_template" "$dest"
sed -i.bak "s/^created: YYYY-MM-DD/created: $(date +%Y-%m-%d)/" "$dest/draft.md" && rm "$dest/draft.md.bak"
echo "Created $dest"
