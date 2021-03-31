#Setup

### Build docker image
`docker build -t wct-api-container .`

### Run docker image:
`docker run -d --name wct_api_container -p 8000:8000 wct-api-container`

### Bash into the container:
`docker exec -it wct_api_container bash`


### Create database tables:
`python manage.py create-db-tables`

### Seed table data:
`python manage.py seed-tables`


### Start container (on subsequent runs):
`docker start wct_api_container`

Entering localhost:8000/docs in the browser should show: 


![alt text](https://i.ibb.co/FwKqvwx/Screenshot-from-2021-03-31-01-16-30.png)
