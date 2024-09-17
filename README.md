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
    
4. Run the Application
    - Start the FastAPI server using uvicorn:
        ```
        uvicorn main:todoApp --reload
        ```
    - This will start the development server at http://127.0.0.1:8000.

5. Access the home page
   - Open your browser and navigate to http://127.0.0.1:8000/todoHome to view the To-Do list interface.
  
## Endpoints

- "get/todoHome" : Renders the to-do list.
- "post/add-todoHTML" : Adds a new to-do item (via form submission).
- "get/delete-todo/{todo_id}" : Deletes a to-do item based on its ID.
- "get/toggle-completion/{todo_id}" : Toggles the completion status of a to-do item based on its ID.

In last 2 I have used get method as html only has 2 methods (get and post) but if you look in main.py file. If you want you can find **DELETE** and **UPDATE methods** for both endpoints commneted at bottom of the code.

## Data Models
- Todo
  ```
  {
  "todo_text": "string",
  "completed": "boolean"
  }
  ```

This README.md file includes details about how to set up and run your FastAPI project, the available API endpoints, and the data models used.

