### Local Setup
```
Install python 3.8+ 
# Install virtualenv & activate it
pip install -U pip virtualenv && virtualenv env && source env/bin/activate 

1.pip install -r requirements.txt

# set below env variable
2. export DJANGO_SETTINGS_MODULE=router.settings

#run migrations
3.1 python manage.py makemigrations
3.2 python manage.py migrate

#create superuser 
4. python manage.py createsuperuser
It will ask to enter user details, please add it and remember the username/password

# start the server
5. python manage.py runserver 0.0.0.0:5000

# exchange username password to get the token
CURL example
curl --location --request POST 'http://localhost:5000/api/v1/login' \
--header 'Content-Type: application/json' \
--data-raw '{"username": "ur username", "password": "ur password"}'
It will you gve you a token in response.

Pass this token in header order to GET/POST/PATCH/DELETE  router details
for example Authorization : token <ur token>

6. Number of APIs its support.
1. GET /api/v1/router-details -> it will return all routers
2. POST /api/v1/router-details -> create router details
3. PATCH /api/v1/router-details/{loop_back} -> get specific router detailn by loop back
4. DELETE /api/v1/router-details/{loop_back} -> Soft delete Router

# note: you have to pass token in header in order to access this endpoints.
```

### Run Test Case
```
1. export DJANGO_SETTINGS_MODULE= router.qa_settings
2. python manage.py migrate
3. pytest -s -vv tests
```

### SSH To Server
```
1. python manage.py sshrouter 
# Note : To Run this command add username and password of machine, this command will run ls command and store its out put in file
2. python manage.py transferFile  # Transfer file on ftp server and ftp server details
```

