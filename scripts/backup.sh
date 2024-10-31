#!/bin/bash

# Variables
CONTAINER_NAME="tech_stack_portfolio_db"
USER="techstackuser"
DATABASE="techstackdb"
BACKUP_DIR="../db_backups"

mkdir -p $BACKUP_DIR

BACKUP_FILE="$BACKUP_DIR/backup_$(date +%Y%m%d).sql"

# Run pg_dump command inside the container
docker exec $CONTAINER_NAME pg_dump -U $USER $DATABASE > $BACKUP_FILE

echo "Backup saved to $BACKUP_FILE"