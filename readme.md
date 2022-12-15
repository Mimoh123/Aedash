# Personal Blog **Aedash**



## Setting up PostgreSQL
-[Install](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) PostgreSQL
-After downloading the installer, prepare to install, Install window will ask for setting up the password. Set a strong password

-You can manually set up the database using the gui tool. Create and setup a database server. Remember the owner and the database name
In our case we can name the database as *django* and owner as *postgres*

## PostgreSQL setting up in django
-install pyscopg2 `pip install psycopg2`
-in *settings.py* file, replace the database object with this,
```
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'django',
'USER': 'postgres',

'PASSWORD': env('PSGS'),
}
```
## I am using Eleephant sql as DaaS
```
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'username',
'USER': 'username',
'HOST' : ''
'PASSWORD': env('PSGS'),
}
```


## Setting up **.env** file

Refer [Here](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f) to setup .env file for django

##More infor from [Here](https://sweetcode.io/django-postgresql-migration-from-sqlite/)