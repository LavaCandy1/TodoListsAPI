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

 **Prerequisites**
- Python 3.7+
- PostgreSQL installed and running
- Virtual environment for Python (recommended)

1. Clone the repository
    ```
    git clone <your-repository-url>
    cd <repository-directory>
    ```
2. Install dependencies
    - Install the necessary packages via `pip`:
        ```
        pip install -r requirements.txt
        ```
3. Configure PostgreSQL
    - Ensure PostgreSQL is installed and running.
    - Create a PostgreSQL database named TodoData:
      ```
      CREATE DATABASE TodoData;
      ```
    - Update the connection URL in database.py:
      ```
      URL_Database = "postgresql://<username>:<password>@localhost:5432/TodoData"
      ```
    - This will start the development server at http://127.0.0.1:8000.
4. Run the Application
    - Start the FastAPI server using uvicorn:
        ```
        uvicorn main:todoApp --reload
        ```
