# Intructions
## Step 1:
clone this app
<br>
`git clone https://github.com/MidoriyaHero/Blog-AI-Gen.git`
## Step 2:
install dependences 
<br>
`pip install requirements.txt`
<br>
NOTE: make sure you change directory to this repo.
## Step 3:
Change database setting in setting.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'YOUR-PJ-NAME', 
        'USER':'YOUR-USERNAME', #WHEN CREATE DATABASE
        'PASSWORD':'YOUR PASSWORD', #WHEN CREATE DATABASE
        'HOST':'HERE IS HOST', #localhost IF you run locally
        'PORT':'5432', # default Postgres's port 
    }
}
```
Then create `.evn` to load your API key with name `GEMINI_API_KEY`
NOTE: to generate GEMINI API key go to [here](https://aistudio.google.com/app/apikey)   
<br>
## Step 4:
run server by command `python manage.py runserver` 
<br>

## NOTE:
For futher information you may need to follow this [video](https://www.youtube.com/watch?v=ftKiHCDVwfA)
