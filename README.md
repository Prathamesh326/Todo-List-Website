# Todo List Website

This is a web-based Todo List application built with Flask, SQLAlchemy, and Bootstrap. It provides users with an easy-to-use interface to manage tasks, set due dates, and mark tasks as completed. Users can register, log in, add tasks, edit tasks, and delete tasks, all while keeping their data secure with authentication features.

## Features

- **User Registration and Login:** Secure registration and login using Flask-Bcrypt for password hashing.
- **Task Management:** Add, edit, and delete tasks with a due date.
- **Responsive Design:** Frontend styled with Bootstrap for responsiveness.
- **Task Alerts:** Users receive feedback when tasks are added successfully or updated.

## Technologies Used

- **Backend:** Python, Flask, Flask-Bcrypt, Flask-Login, SQLAlchemy
- **Frontend:** HTML, Bootstrap, CSS
- **Database:** SQLite

## Project Structure

- **app.py:** Main Flask application file, defines routes, models, and authentication.
- **templates/**: Contains HTML templates for each page.
  - `base.html`: Base template with navigation and alerts.
  - `login.html`: Login page.
  - `register.html`: Registration page.
  - `dashboard.html`: Task dashboard page.
  - `task_form.html`: Form page for adding or editing tasks.
- **forms.py**: Contains Flask-WTF forms for login, registration, and task management.
- **static/css/styles.css**: Custom CSS styles for the frontend.

## Getting Started

To run this project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Prathamesh326/Todo-List-Website.git
   cd Todo-List-Website
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   Open Python shell and run:
   ```python
   from app import db
   db.create_all()
   ```

5. **Run the application:**
   ```bash
   flask run
   ```

6. **Access the application:**
   Open your browser and go to `http://127.0.0.1:5000`.

## Usage

1. **Register an Account:** Go to the registration page and create an account.
2. **Login:** Log in with your registered email and password.
3. **Add Tasks:** Click on "Add Task" to create a new task with a title, description, and due date.
4. **Manage Tasks:** You can view, edit, and delete tasks from the dashboard.
5. **Logout:** Click the logout button to securely log out of your session.

## Future Enhancements

- Adding categories for tasks.
- Adding a priority selection option.
- Implementing task completion reminders.

## Contributing

Feel free to contribute to this project by creating issues or submitting pull requests.
