
# Personal Blog **Aedash** ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white) 

Aedash is a personal blog prepared using the Django framework based on Python. It is a fully functional blog application with following features

 - Ability to write blog posts
 - Ability to add manager and editors
 - Fully Functional authentication system including OAuth2 (Google, Facebook login)
 - Fully Functional Comment System)


## Setting up the application

### Setting up PostgreSQL
-[Install](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) PostgreSQL
-After downloading the installer, prepare to install, Install window will ask for setting up the password. Set a strong password

-You can manually set up the database using the gui tool. Create and setup a database server. Remember the owner and the database name
In our case we can name the database as *django* and owner as *postgres*

###  PostgreSQL setting up in django
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
###  I am using Eleephant sql as DaaS (Desktop as a service)
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
