#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

VERSION="$(npm view "octicons@latest" version)"

if grep -q --fixed "Octicons version: [v${VERSION}]" README.md; then
  echo "No updates needed"
  exit 0
fi

echo "Updating octicons to version ${VERSION}"

rm -rf node_modules
npm link --quiet "octicons@${VERSION}"
cp node_modules/octicons/build/data.json octicons/data.json
rm -rf node_modules

OCTICONS_README_LINE="Octicons version: [v${VERSION}](https://github.com/primer/octicons/releases/tag/v${VERSION})"
sed --in-place 's|Octicons version: .*|'"${OCTICONS_README_LINE}"'|' README.md

git add octicons/data.json README.md
# git commit -m "Updating Octicons to version ${VERSION}"
