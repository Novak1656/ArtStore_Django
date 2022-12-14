# ArtStore - is a service for buying and selling digital illustrations.

# Description
Thanks to this web application, designers, illustrators and artists
will be able to put their works up for sale.

Ordinary users have the opportunity to purchase all kinds of illustrations:
logos, wallpapers, covers, avatars, etc. The purchased works will be stored
in the user's own gallery from where he can download the illustration to his
device at any time.

# Usage
- Open the project in any user-friendly development environment.
- In the file settings.py in the artstore directory in the DATABASES dictionary,
 specify 'USER' and 'PASSWORD' from your pgadmin.
 Or use the following code to connect to the sqlite3 DBMS.

 ***
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }
 ***

- Open the terminal and use the 'cd' command to navigate to the project directory
 (there should be a file in this directory manage.py ).
- Perform migrations for the database using the following commands:
  python manage.py makemigrations
  python manage.py migrate
- Start the server with the command:
  python manage.py runserver
- Follow the link http://127.0.0.1:8000/
