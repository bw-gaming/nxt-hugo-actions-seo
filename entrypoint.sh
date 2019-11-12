#!/bin/sh

# Exit on failure
set -e

if [ -z "$PUBLISH_DIR" ]; then
  PUBLISH_DIR="$GITHUB_WORKSPACE/public"
fi


python seo.py $PUBLISH_DIR