
# BMM 

BMM project with Django4


## Installation

Make virtual environment (linux/mac):
```bash
python3 -m venv venv
```
Make virtual environment (windows):
```bash
python -m venv venv
```
Open venv (linux/mac):
```bash
source venv/bin/activate
```
Open venv (windows):
```bash
venv\Scripts\activate
```
Install requirements:
```bash
pip install -r requirements.txt
```
Make migrations:
```bash
python manage.py makemigrations
```
Migrate:
```bash
python manage.py migrate
```
Create superuser:
```bash
python manage.py createsuperuser
```

## Server
Run server and enjoy:
```bash
python manage.py runserver
```