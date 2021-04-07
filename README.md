# SQL Injection with Django

This application is a demonstration prototype just to show how to perform SQLi attack.

## Install

- Setup postgresql database

```
sudo -u postgres createuser -P me
sudo -u postgres createdb -O me data
export PGPASSWORD=******
```

- Install

```
pipenv install
```

- run

```
pipenv shell
cd sqli
python manage.py runserver
```

## Hack

Open http://localhost:8000/?user=me

Find sql injection to see all task (not only for one user).


## Fix

Create a new branch and try to fix this sql injection.

Solution:

```
git checkout fix
```

The solution is to use prepared statement:

```
query = "SELECT * from sqli_task WHERE owner = %s"
cursor = connection.cursor()
cursor.execute(query, [user])
```