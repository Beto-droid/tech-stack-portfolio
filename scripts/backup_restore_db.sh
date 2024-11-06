#!/bin/bash

# Variables
CONTAINER_NAME="tech_stack_portfolio_db"
USER="techstackuser"
DATABASE="techstackdb"
BACKUP_DIR="../db_backups"

mkdir -p $BACKUP_DIR

# Create backup
backup_database() {
    BACKUP_FILE="$BACKUP_DIR/backup_$(date +%Y%m%d_%H%M).sql"
    docker exec $CONTAINER_NAME pg_dump -U $USER $DATABASE > $BACKUP_FILE
    echo "Backup saved to $BACKUP_FILE"
}

# Restore from selection backups
restore_database() {
    echo "Warning: This action will delete all data in the $DATABASE database and restore it from a backup."
    read -r -p "Are you sure you want to proceed? (yes/no): " confirm
    if [[ $confirm != "yes" ]]; then
        echo "Restore cancelled."
        exit 0
    fi

    # List available backups
    echo "Available backups:"
    select backup_file in "$BACKUP_DIR"/*.sql; do
        if [[ -n $backup_file ]]; then
            echo "Selected backup: $backup_file"
            break
        else
            echo "Invalid selection. Please try again."
        fi
    done

    # Drop and recreate the db
#    docker exec -i $CONTAINER_NAME psql -U $USER -c "DROP DATABASE $DATABASE;"
#    docker exec -i $CONTAINER_NAME psql -U $USER -c "CREATE DATABASE $DATABASE;"

    # Restore.
    docker exec -i $CONTAINER_NAME psql -U $USER -d $DATABASE < "$backup_file"
    echo "Database restored from $backup_file"
}

# options
echo "Select an option:"
echo "1) Backup"
echo "2) Restore"
echo "3) Exit"
read -r -p "Enter choice [1 or 2]. To exit: choice [3]: " choice

case $choice in
    1)
        backup_database
        ;;
    2)
        restore_database
        ;;
    3)
        echo "Exit.."
        exit 0
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac
