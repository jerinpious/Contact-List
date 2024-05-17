
# Contact List Project
## Overview
This project is a basic Contact List application built with a Flask backend and a React frontend. The application allows users to create, read, update, and delete contacts. It uses SQLite as the database.

## Requirements
### Backend
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-CORS
### Frontend
- Node.js
- React
### Setup Instructions
#### Backend
- Clone the Repository

~~~
git clone <repository-url>
cd <repository-directory>
~~~
- Create a Virtual Environment
~~~
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
~~~
- Install Dependencies
~~~
pip install flask flask_sqlalchemy flask_cors
~~~
- Run the Flask Application
 - cd to backend
~~~
python main.py
~~~
The backend will be running on http://127.0.0.1:5000.

#### Frontend
- Navigate to the Frontend Directory
~~~
cd frontend
~~~
- Install Dependencies
~~~
npm install
~~~
- Run the React Application
~~~
npm run dev
~~~
The frontend will be running on http://localhost:3000.

### Project Structure
#### Backend
- main.py: Contains the main Flask application code, including route definitions and database setup.
- config.py: Configuration file for the Flask application.
- models.py: Defines the database models.
#### Frontend
- App.jsx: Main component of the React application, rendering the contact list and forms.
- ContactList.jsx: Component for displaying the list of contacts.
- ContactForm.jsx: Component for creating and updating contacts.
### API Endpoints
~~~
GET /contacts: Retrieves all contacts.
POST /create_contact: Creates a new contact.
PATCH /update_contact/<int:user_id>: Updates an existing contact.
DELETE /delete_contact/<int:user_id>: Deletes a contact.
~~~
