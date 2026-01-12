#!/bin/bash
# Automation example: Project backup script
# Demonstrates how ChatGPT can help create backup automation

# Configuration
PROJECT_DIR="${1:-.}"
BACKUP_DIR="${2:-./backups}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="project_backup_${TIMESTAMP}.tar.gz"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create backup
echo "Creating backup of $PROJECT_DIR..."
tar -czf "${BACKUP_DIR}/${BACKUP_NAME}" \
    --exclude='node_modules' \
    --exclude='.git' \
    --exclude='*.log' \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    "$PROJECT_DIR"

if [ $? -eq 0 ]; then
    echo "Backup created successfully: ${BACKUP_DIR}/${BACKUP_NAME}"
    echo "Backup size: $(du -h "${BACKUP_DIR}/${BACKUP_NAME}" | cut -f1)"
    
    # Keep only last 5 backups
    cd "$BACKUP_DIR" || exit 1
    ls -t project_backup_*.tar.gz | tail -n +6 | xargs -r rm
    echo "Old backups cleaned up (keeping last 5)"
else
    echo "Error: Backup failed"
    exit 1
fi
