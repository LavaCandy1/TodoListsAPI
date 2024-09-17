# FastAPI To-Do Application

This is a simple To-Do list application built using FastAPI and PostgreSQL as the backend database. The application allows users to add, delete, and mark tasks as completed directly from the web interface built using Jinja2 templates.

## Features

    - Add new to-do items
    - Mark tasks as completed or pending
    - Delete tasks
    - PostgreSQL integration for persistent data storage
    - Dynamic HTML rendering using Jinja2 templates

## Tech Stack

    - FastAPI: For creating the web server and API.
    - PostgreSQL: Database for storing to-do items.
    - SQLAlchemy: ORM used to interact with PostgreSQL.
    - Jinja2: Templating engine for rendering dynamic HTML.
    - HTML & CSS: Frontend styling and structure.

## Project Structure

```
├── database.py          # Database connection and session management
├── main.py              # FastAPI app, defining routes and logic
├── models.py            # SQLAlchemy models for database schema
├── requirements.txt     # List of dependencies
├── static/              # Static files (CSS, etc.)
│   └── home.css         # Styles for the to-do page
├── templates/           # HTML templates rendered by FastAPI
│   └── todoHome.html    # Main page for the to-do list
└── README.md            # Project documentation
```


## Setup and Installation

--- Prerequisites
    - Python 3.7+
    - PostgreSQL installed and running
    - Virtual environment for Python (recommended)
