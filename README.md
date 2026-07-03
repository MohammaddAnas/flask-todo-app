# Flask Todo App

A simple Todo List web application built using Python Flask. The application allows users to create, update, view, and delete tasks while demonstrating the core concepts of Flask web development.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- View all tasks
- Search tasks by title or description
- Mark tasks as completed or incomplete
- Store task creation date and time
- Responsive user interface
- Dynamic pages using Jinja2 templates

## Technologies Used

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Datetime

### Frontend
- HTML
- CSS
- JavaScript

### Flask Concepts
- Routing
- GET and POST methods
- Jinja2 template inheritance
- SQLAlchemy ORM
- CRUD operations

## Project Structure

```text
Todo-App/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── update.html
│   └── about.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── test.js
```

## Live Demo

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MohammadAnas/flask-todo-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-todo-app
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your browser and visit:

   ```
   http://127.0.0.1:5000/
   ```

## Future Improvements

- User authentication
- Task categories
- Task priorities
- Due dates
- Dark mode

## Author

Muhammad Anas