


# Backend Assignment

## Project Description
This project implements a backend system for user and discussion management using Flask. It supports the following features:
- User Signup/Login
- Create, Update, Delete User
- Create, Update, Delete Discussion
- Search Users by Name
- Search Discussions by Tags or Text
- Follow/Unfollow Users
- Like/Comment on Posts

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Flask-JWT-Extended
- SQLite (can be switched to another DB)

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/18h61a05b0/backend-assignment.git
    cd backend-assignment
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Run the application:
    ```bash
    flask run
    ```

## API Documentation
### User Endpoints
- **Signup**: `POST /users/signup`
- **Login**: `POST /users/login`
- **Get All Users**: `GET /users/`
- **Search Users**: `GET /users/search?name=<name>`

### Discussion Endpoints
- **Create Discussion**: `POST /discussions/`
- **Get All Discussions**: `GET /discussions/`
- **Search Discussions by Tags**: `GET /discussions/search/tags?tags=<tags>`
- **Search Discussions by Text**: `GET /discussions/search/text?text=<text>`

## Postman Collection
Postman link : 

## Tests
To run the tests, execute:
```bash
python -m unittest discover tests
