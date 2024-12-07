# API-Server

The backend server of this application, built with python and fastapi.


# How To Run
As this is only meant to run locally, dependencies like database have to be running locally as well.

The docker-compose.yml file should define all necessary containers and the api-server in it.

**so, the easiest way of booting this app is to run `docker compose up api-server` under `/footbook` directory .**

Access http://0.0.0.0:8000/swagger for API definitions


To have better IDE support, run ` pip3 install -r ./requirements.txt` under `/api-server` directory.
