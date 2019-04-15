# Andela Football League ug

Build project with docker-compose
```
docker-compose build
```

Start development server
```
docker-compose up
```

Run migrations
```
docker-compose build
docker-compose up -d
docker exec -it <app-container-name> python manage.py db init
docker exec -it <app-container-name> python manage.py db migrate
docker exec -it <app-container-name> python manage.py db upgrade
```

Access database via the shell
```
docker exec -it <db-container-name> psql -U postgres
```