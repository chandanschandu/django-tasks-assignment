# Django Task Management System

## Features

- Full CRUD API for tasks
- Search by title, date
- Sort by date
- Dockerized setup

## Setup

```bash
git clone https://gitlab.com/chandans01/django-tasks-assignment.git
cd django_tasks
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## docker
docker-compose build
docker-compose up
