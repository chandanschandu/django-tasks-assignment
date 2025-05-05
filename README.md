# 📝 Django Task Management System

A RESTful API to manage TODO tasks with full CRUD operations, search, sort, and Dockerized setup.

---

## 🚀 Features

- Add, list, edit, and delete tasks
- Search tasks by title or date
- Sort tasks by date
- Docker support for easy setup
- Class-based views with Django REST Framework
- Clean code structure with serializers, viewsets, and URLs

---

## 📦 Setup Instructions (Local)

```bash
# Clone the repo
git clone https://github.com/chandanschandu/django-tasks-assignment.git
cd django_tasks

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
```

Visit the API at: [http://localhost:8000/tasks/](http://localhost:8000/tasks/)

---

## 🐳 Docker Setup

```bash
# Build and run with Docker Compose
docker-compose build
docker-compose up
```

---

## 📬 API Endpoints

| Method | Endpoint                 | Description                          |
|--------|--------------------------|--------------------------------------|
| POST   | `/tasks/`                | Add a task with title and description |
| GET    | `/tasks/`                | List all tasks                        |
| GET    | `/tasks/?sort_by_date=true` | Sort tasks by date                |
| GET    | `/tasks/?search_date=YYYY-MM-DD` | Search tasks by date         |
| GET    | `/tasks/?search=TitleKeyword`     | Search tasks by title         |
| PATCH  | `/tasks/<id>/`           | Edit a task by ID                     |
| DELETE | `/tasks/<id>/`           | Delete a task by ID                   |

---

## 🧠 Project Structure

### 📁 Views

- `TaskListCreateView`: Handles `GET /tasks/` and `POST /tasks/`
- `TaskDetailView`: Handles `PATCH /tasks/<id>/` and `DELETE /tasks/<id>/`

Defined in: `tasks/views.py`

### 📄 Serializers

- `TaskSerializer`: Converts `Task` model instances to/from JSON

Defined in: `tasks/serializers.py`


## ✅ Examples

### Add a Task

**POST** `/tasks/`

```json
{
  "title": "Finish Django Assignment",
  "description": "Complete the coding task and push to GitHub",
  "date": "2025-05-05"
}
```

### Search Tasks by Title

**GET** `/tasks/?search=django`

### Sort Tasks by Date

**GET** `/tasks/?sort_by_date=true`

### Edit a Task

**PATCH** `/tasks/1/`

```json
{
  "title": "Updated Task Title"
}
```

### Delete a Task

**DELETE** `/tasks/1/`

---
