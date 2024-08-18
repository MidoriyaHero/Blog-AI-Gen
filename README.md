# Step 1:
Create database in local storage

```
createdb -h localhost -p 5432 -U dbuser testdb
```

This mean create database in `localhost` with `port:5432`

# Step 2:
Connect to database server by changing `setting.py` file Script_Convert folder

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', #Change to engine name when creating database
        'NAME': 'DBName', #This is the name of the database
        'USER':'Name of postgres', #Name of the user when create postgresql database default: postgres
        'PASSWORD':'yourpass', #password for the database (default: 'postgres')
        'HOST':'localhost',
        'PORT':'5432',
    }
}
```
## Notes: if you use cloud storage, change these parameters to given values on your server 

# Step 3:
Run command:
```
python manage.py makemigrations
```
You will get the results like this:
```
No changes detected
```
and then run command:
```
python manage.py migrate
```
Results:
```
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
# Step 4:
Create superuser ADMIN by command:
```
python manage.py createsuperuser
```
Then you just specify your username and password (you can leave email address blank)
<br />
Result:
```
Superuser created successfully.
```

# Step 5:
if you want to create a new table on your scheme, create the new one on `models.py` in `script_gen folder`

# Step 6:
if you create a new model run these commands:
```
python manage.py makemigrations
python manage.py migrate
```
Results should look like this:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, sessions
Running migrations:
  Applying blogpost.0001_initial... OK
```
Then go to `admin.py` in `script_gen folder`
adding your model name <br> 
`admin.site.register(ModelName)`

# NOTED: Please add them into database to make the website work.
