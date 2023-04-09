### About
Backend in Fast api for 3 tables:

- Trip
- Review
- Blog


Start Server
````
uvicorn trabook_backend.api:app --reload
````

Go to database configuration in the following file
````
trabook_backend/orm/database.py
````

Populate data with default values, running the sql sentences in this file `populate_tables.sql`


### Follow the next step to set up in your local Environment
````
pip3 install pipenv
sudo -H pip3 install -U pipenv
pipenv install 
pipenv shell

uvicorn trabook_backend.api:app --reload
````