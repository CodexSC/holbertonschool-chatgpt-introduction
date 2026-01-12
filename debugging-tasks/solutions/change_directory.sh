#!/bin/bash
# Fixed version - checks if directory exists before changing to it
# Bug fixed: Added error handling for non-existent directory

DIRECTORY="/tmp/test_dir"

if [ -d "$DIRECTORY" ]; then
    cd "$DIRECTORY" || exit 1
    ls -la
    echo "Current directory: $(pwd)"
else
    echo "Error: Directory $DIRECTORY does not exist"
    exit 1
fi
