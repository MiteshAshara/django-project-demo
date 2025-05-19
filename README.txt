# DJANGO DOCKER SETUP WITH MYSQL - STEP BY STEP GUIDE

## PREREQUISITES
1. Docker installed (verify with: `docker --version`)
2. Docker Compose installed (verify with: `docker-compose --version`)

## STEP 1: INITIALIZE PROJECT FILES
1. Create necessary configuration files:

   # Create MySQL initialization script
   $ echo "CREATE DATABASE IF NOT EXISTS \`demo-site-django\`;
   CREATE USER IF NOT EXISTS 'service_user'@'%' IDENTIFIED BY 'password123';
   GRANT ALL PRIVILEGES ON \`demo-site-django\`.* TO 'service_user'@'%';
   FLUSH PRIVILEGES;" > init.sql

   # Create superuser script
   $ echo "import os
   import django
   
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
   django.setup()
   
   from django.contrib.auth.models import User
   
   username = 'admin'
   email = 'admin@gmail.com'
   password = 'admin'
   
   if not User.objects.filter(username=username).exists():
       print(f'Creating superuser {username}')
       User.objects.create_superuser(username=username, email=email, password=password)
       print('Superuser created successfully')
   else:
       print(f'Superuser {username} already exists')" > create_superuser.py

## STEP 2: BUILD AND START CONTAINERS
1. Build Docker containers:
   $ docker-compose build

2. Start containers in the background:
   $ docker-compose up -d

3. Start containers with logs visible:
   $ docker-compose up

## STEP 3: CHECK CONTAINER STATUS
1. List running containers:
   $ docker-compose ps

2. View logs of the Django application:
   $ docker-compose logs django-app

3. View logs of the MySQL database:
   $ docker-compose logs db

4. Follow Django application logs in real-time:
   $ docker-compose logs -f django-app

## STEP 4: VERIFY DATABASE CONNECTION
1. Access MySQL container shell:
   $ docker-compose exec db bash

2. Connect to MySQL from within container:
   $ mysql -u service_user -ppassword123 -h localhost demo-site-django

3. Check if database exists:
   $ mysql -u service_user -ppassword123 -h localhost -e "SHOW DATABASES;"

4. Test connection from Django container:
   $ docker-compose exec django-app bash
   $ python -c "import MySQLdb; MySQLdb.connect(host='db', user='service_user', passwd='password123', db='demo-site-django')"

5. Network connectivity test:
   $ docker-compose exec django-app bash
   $ nc -zv db 3306

## STEP 5: RUN DJANGO MANAGEMENT COMMANDS
1. Run migrations:
   $ docker-compose exec django-app python manage.py migrate

2. Create superuser manually:
   $ docker-compose exec django-app python manage.py createsuperuser

3. Run superuser creation script:
   $ docker-compose exec django-app python create_superuser.py

4. Collect static files:
   $ docker-compose exec django-app python manage.py collectstatic --noinput

5. Run Django shell:
   $ docker-compose exec django-app python manage.py shell

## STEP 6: ACCESS THE APPLICATION
1. Web interface: http://localhost:8000/
2. Admin interface: http://localhost:8000/admin/
   - Username: admin
   - Password: admin

## STEP 7: EXTERNAL DATABASE ACCESS
1. Connect to MySQL from host machine:
   $ mysql -u service_user -ppassword123 -h 127.0.0.1 -P 3307 -D demo-site-django

2. Import SQL file to database:
   $ mysql -u service_user -ppassword123 -h 127.0.0.1 -P 3307 demo-site-django < backup.sql

3. Export database to SQL file:
   $ docker-compose exec db mysqldump -u service_user -ppassword123 demo-site-django > backup.sql

## STEP 8: MANAGE DOCKER ENVIRONMENT
1. Restart containers:
   $ docker-compose restart

2. Stop containers without removing data:
   $ docker-compose down

3. Stop containers and remove volumes (DELETES ALL DATA):
   $ docker-compose down -v

4. Force rebuild containers (no cache):
   $ docker-compose build --no-cache

5. View Docker disk usage:
   $ docker system df

6. Remove unused volumes:
   $ docker volume prune

## STEP 9: TROUBLESHOOTING
1. Check container logs:
   $ docker-compose logs

2. Check container resources:
   $ docker stats

3. Inspect container networks:
   $ docker network ls
   $ docker network inspect static-site_default

4. Check docker volumes:
   $ docker volume ls
   $ docker volume inspect static-site_db_data

5. Rebuild and restart from scratch:
   $ docker-compose down -v
   $ docker volume prune -f
   $ docker-compose build --no-cache
   $ docker-compose up

## STEP 10: COMMON MYSQL COMMANDS
# Run these after connecting to MySQL

1. Show all databases:
   mysql> SHOW DATABASES;

2. Select a database:
   mysql> USE demo-site-django;

3. Show all tables:
   mysql> SHOW TABLES;

4. Describe table structure:
   mysql> DESCRIBE auth_user;

5. Check for service user:
   mysql> SELECT User, Host FROM mysql.user;

6. Grant privileges (as root):
   mysql> GRANT ALL PRIVILEGES ON `demo-site-django`.* TO 'service_user'@'%';
   mysql> FLUSH PRIVILEGES;
