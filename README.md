# Junction

A Django web platform that helps low-income workers find jobs and connects them with employers.

## Overview

Junction lets employers publish job posts and lets workers browse them, with user accounts and profile pictures. It is a full-stack Django project backed by SQLite.

## Features

| Area | What it does |
|---|---|
| Accounts | Registration, login and logout with Django authentication |
| Profiles | One profile per user with a profile picture, resized to at most 300x300 pixels |
| Job posts | Title, description, author, posting date and an availability status (default: available) |
| Admin | Django admin site for managing users and posts |

## Tech Stack

Python, Django, SQLite, django-crispy-forms, Pillow, gunicorn, HTML/CSS templates.

## Project Structure

```text
Junction/
├── junction1/        # Django project settings and URL routing
├── users/            # Registration, login and profile app
├── webpage/          # Job post app and page templates
├── media/            # Uploaded profile pictures
├── manage.py
└── requirements.txt
```

## Getting Started

Step 1. Clone the repository and move into it:

```bash
git clone https://github.com/malehaICK/Junction.git
cd Junction
```

Step 2. Install the dependencies:

```bash
pip install -r requirements.txt
```

Step 3. Create the database tables and an admin account:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Step 4. Start the development server and open http://127.0.0.1:8000/ in your browser:

```bash
python manage.py runserver
```

## Configuration

Secrets are read from environment variables and are never stored in the repository. Set these before running the server (all are optional for local development):

```bash
export DJANGO_DEBUG=True                 # development only; defaults to False
export DJANGO_SECRET_KEY="your-own-long-random-key"
export DJANGO_ALLOWED_HOSTS="localhost,127.0.0.1"
export EMAIL_HOST_USER="your-address@example.com"
export EMAIL_HOST_PASSWORD="your-app-password"
```

The SQLite database (`db.sqlite3`) and uploaded files in `media/` are created locally and are intentionally not committed. Run `python manage.py migrate` to create a fresh database.

## Author

Maleha Israt Chowdhury. [Portfolio](https://malehaisratchowdhury.netlify.app/)

## License

Released under the MIT License. See the `LICENSE` file.
