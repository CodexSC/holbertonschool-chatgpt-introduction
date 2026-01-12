#!/bin/bash
# This script attempts to change to a directory and list its contents
# Contains a bug - use ChatGPT to identify the issue

DIRECTORY="/tmp/test_dir"

cd $DIRECTORY
ls -la
echo "Current directory: $(pwd)"
