# Ghibli Project
Ghibli Project.

Backend:
* Django
* Python
* Redis
* PostgreSQL
* Celery

Frontend:
* jQuery

The project can automated fetch Ghibli data using celery


## Project Setup
### Docker
You need to install `docker-compose`. Run command
```shell script
pip install docker-compose
```

After that you can run commands

```shell script
docker-compose build
docker-compose up -d
```

After that you can run `docker-compose ps`. You will see

```shell script
      Name                     Command                 State             Ports
--------------------------------------------------------------------------------------
ghibli_backend_1    sh -c sh runserver.sh            Up           8000/tcp
ghibli_celery_1     celery -A backend worker - ...   Up
ghibli_data_1       true                             Restarting
ghibli_frontend_1   docker-entrypoint.sh sh -c ...   Up           8080/tcp
ghibli_nginx_1      /usr/sbin/nginx                  Up           0.0.0.0:8000->80/tcp
ghibli_postgres_1   docker-entrypoint.sh postgres    Up           5432/tcp
ghibli_redis_1      docker-entrypoint.sh redis ...   Up           6379/tcp
```

You can open `0.0.0.0:8000`

### Without Docker
After that you need to run commands.

#### Backend
```shell script
cd backend
pipenv install --dev
python manage.py migrate
python manage.py createsu
python manage.py runserver
```
#### Frontend
```shell script
cd frontend
npm install
npm install -g nodemon
npm install express --save
nodemon server.js
```

## After Setup
* YOU NEED RUN SERVER
* Open [http://0.0.0.0:8000][http://0.0.0.0:8000]
#### 


## API Documentation
* [http://0.0.0.0:8000/doc/redoc/][http://0.0.0.0:8000/doc/redoc/]
* [http://0.0.0.0:8000/doc/swagger/][http://0.0.0.0:8000/doc/swagger/]

## Testing

### Without docker
```shell script
cd backend/
python manage.py test
```
### From Docker
```shell script
docker-compose exec backend python manage.py test
```

## USERS
### Admin
```shell script
Username:     admin
Password:     admin123456
```

## Contribution

Any help is appreciated. Or feel free to create a Pull Request.

[http://0.0.0.0:8000/doc/redoc/]: http://0.0.0.0:8000/doc/redoc/

[http://0.0.0.0:8000/doc/swagger/]: http://0.0.0.0:8000/doc/swagger/

[http://0.0.0.0:8000]: http://0.0.0.0:8000