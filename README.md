
# Tech Stack Portfolio

This is a portfolio showcasing my full-stack development work, featuring a variety of technologies and applications.
The project is structured using Django and leverages Docker for containerization.
Below, you’ll find information on how to set up, run, and interact with the project.

## Applications Included
This portfolio demonstrates various applications, including (details to be filled in as apps are added):
- **App 1:** Description placeholder.
- **App 2:** Description placeholder.
- **App 3:** Description placeholder.

## Getting Started

There are two ways to run the project:

### 1. Local Django Setup with Dockerized PostgreSQL
This method uses your local Python environment for Django while connecting to a PostgreSQL database running as a Docker service.

**Steps:**
1. Start the database service using Docker:
   ```bash
   docker compose up -d db
   ```

2. Run Django locally:
   ```bash
   python manage.py runserver
   ```

### 2. Full Dockerized Setup
Run both the Django application and the PostgreSQL database using Docker Compose.

**Steps:**
1. Build the Docker images and start the services:
   ```bash
   docker compose up --build
   ```

2. For debugging, check logs and run in verbose mode:
   ```bash
   docker compose --verbose up --build
   ```

3. If you encounter cache issues, rebuild without cache:
   ```bash
   docker compose build --no-cache
   ```

## Interacting with the Docker Containers

### Accessing the Database
To connect to the PostgreSQL database running in Docker, use:
   ```bash
   docker exec -it tech_stack_portfolio_db psql -U techstackuser -d techstackdb
   ```


### Entering the Web Container
To enter the web container’s shell for debugging:
   ```bash
   docker exec -it tech_stack_portfolio_web /bin/bash
   ```

## Exporting Python Requirements
To generate a `requirements.txt` file for your environment:
   ```bash
   pip freeze > requirements.txt
   ```

## Did you change something in my code?
Well, you need to remake the docker image from django.
   ```bash
   docker build -t my_django_portfolio_web .
   ```

## Docker failed?
See their logs
   ```bash
   docker logs
   ```

## Any Problems django migrations ?
Try
   ```bash
   python manage.py migrate --fake <migration> zero

   ```


# PostgreSQL Dump and restore

## Backup

  # [AUTO]
  ### In scripts folder there is a bash to backup an already running db. Add -x

  ```
  chmod +x backup_restore_db.sh
  ```

  ### Then run 
  ```
  ./backup_restore_db.sh 
  ```
   # [MANUAL]
   ### Having the service of db running, run 

   ```
   bash pg_dump -h localhost -p 5444 -U your_username -d your_database_name > backup.sql
   bash pg_dump -h localhost -p 5444 -U techstackuser -d techstackdb > backup.sql
   ```

   ### Inside the container

   ```
   docker exec -it your_postgres_container_name bash
   pg_dump -U your_username your_database_name > /path/to/backup.sql
   docker cp your_postgres_container_name:/path/to/backup.sql ./backup.sql
   ```
   
   ### example:

   ```
   docker exec -it tech_stack_portfolio_db bash
   pg_dump -U techstackuser techstackdb > /path/to/backup.sql
   docker cp tech_stack_portfolio_db:/path/to/backup.sql ./backup.sql   
   ```

## Restore
   ### Make sure the db its running
   ```
   docker-compose up -d
   ```
   ### Check if DB its created, if not create it.
   ```
   docker exec -it your_postgres_container_name psql -U your_username -c "CREATE DATABASE your_database_name;"
   ```
   ### Copy backup to container
   ```
   docker cp /path/to/backup.sql your_postgres_container_name:/backup.sql
   ```
   ### Run the backup.
   ```
   docker exec -it your_postgres_container_name psql -U your_username -d your_database_name -f /backup.sql
   ```

# NPM

## The readme its located in the to_do_app



