# RBAC System

This RBAC (Role-Based Access Control) system is designed for secure and efficient management of user data and roles. Built using **MySQL**, **FastAPI**, **JavaScript**, and **HTML/CSS**, it offers seamless functionality and robust security features.

---

## Key Features:

### User Registration & Login:
- Users can register with their email address and create an account.
- Email uniqueness is enforced—registration with an existing email is not allowed.
- After registering, users can log in to access their personalized data.

### Role Management:

#### Admin Role:
- The admin is pre-configured in the database.
- Admins have access to advanced functionality, including:
  - Viewing all user data.
  - Adding new users.
  - Updating user details.
  - Deleting users.

#### User Role:
- Users can only view and manage their own data, ensuring privacy and restricted access.

### Additional Features:
- Password recovery option for both Admin and User roles.

---

## Prerequisites:
- **Python 3.11.6**
- **MySQL**

---

### Steps to Install

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/checklist-application.git
    cd checklist-application
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    Ensure you are in the virtual environment, then install the required packages from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the database initialization script**:
    If you're using a different server or environment, you will need to initialize the database before starting the application. Run the following command to set up the necessary tables:
    ```bash
    python initDB.py
    ```

5. **Run the application**:
    Use **uvicorn** to start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```


You need to add your server details in .env files for database connection.
