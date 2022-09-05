# alkemy-challenge
Alkemy Challenge: Data Analytics + Python - Backend Developer

> This project is a  Data Analytics Challenge with Python from https://www.alkemy.org/

# Requirements:

- Docker and Docker Compose

# Run it locally

## 1. Clone or download de repository:

```
git@github.com:josdanind/alkemy-challenge.git
```

## 2. Configure the environment variables into the .env

By default these are the values:

```
# Data Sources
MUSEUMS = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv"
LIBRARIES = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"
CINEMAS = ""


# Postgres
DB_USER = "josdanind"
DB_HOST = "localhost"
DB_PORT = 5432
DB_PASS = "password"
DB_NAME = "alkemy-challenge"
```

> Cinema data does not exist!

## 3. Run docker-compose.yml

at the level of the docker-compose.yml file, execute:

```
docker-compose up --build
```

## 4. Enter to Database

```
docker exec -it alkemy-db psql --username=josdanind --dbname=alkemy-challenge
```

## 5. Show data

```sql
SELECT * FROM places;
SELECT * FROM info;
```