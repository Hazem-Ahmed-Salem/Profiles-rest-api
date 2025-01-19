# Profiles REST API

This is a RESTful API built with _Django_ and _Django REST Framework_ for managing user profiles. It provides endpoints to create, retrieve, update, and delete profiles

## Features

- _User Authentication_: Secure login and registration using the built in Django REST Framework authtoken .
- _Profile Management_: Create, update, and delete user profiles.
- _User Profile Feed_: Add, update, or remove status.

## Technologies Used

- _Django_: Python web framework used for backend development.
- _Django REST Framework_: Toolkit for building Web APIs in Django.
- _SQLite_: Database for storing user profiles and related data.
- _Django Rest FrameWork authtoken_: Tokens for user authentication and authorization.

## Endpoints

### User Authentication

- _POST /api/profile_: Register a new user.
- _POST /api/login_: Log in with existing credentials.

### Profile

- _GET /api/profile/_: Retrieve all users profiles.
- _GET /api/profile/"id"_: Retrieve a user profile by its id.
- _PUT /api/profile/"id"_: Updates the user's information by id
- _PATCH /api/profile/"id"_: Updates part of the user's information by id
- _DELETE /api/profile/"id"_: Delete the current user's profile.

### Profile Feed

- _GET /api/feed/_: Retrieve all user profile status.
- _GET /api/feed/"id"_: Retrieve a user profile status by its id.
- _PUT /api/feed/"id"_: Updates the user's status by id
- _PATCH /api/feed/"id"_: Does the same as the PUT because there is only one field you can update
- _DELETE /api/feed/"id"_: Delete the current user's profile status.

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/Hazem-Ahmed-Salem/Profiles-rest-api.git

2. Navigate to the project folder:
   bash
   cd Profiles-rest-api

3. Create and activate a virtual environment:
   bash
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`

4. Install the required dependencies:
   bash
   pip install -r requirements.txt

5. Set up environment variables by creating a .env file with the following configuration:
   env
   SECRET_KEY=<Your Django Secret Key>
   DEBUG=True
   DB_NAME=profiles_db # Or set this to your PostgreSQL database name
   DB_USER=<Your DB username>
   DB_PASSWORD=<Your DB password>
   DB_HOST=localhost
   DB_PORT=5432

6. Run migrations to set up the database:
   bash
   python manage.py migrate

7. Create a superuser (for admin access):
   bash
   python manage.py createsuperuser

8. Start the development server:
   bash
   python manage.py runserver

The API should now be running on http://localhost:8000.

## Testing

You can test the endpoints using Postman or any other API testing tool. Example requests can be found in the documentation above.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
