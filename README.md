# RBAC System

This RBAC (Role-Based Access Control) system is designed for secure and efficient management of user data and roles. Built using **MySQL**, **FastAPI**, **JavaScript**, and **HTML/CSS**, it offers seamless functionality and robust security features.

---

## 🚀 Key Features:

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

## 🛠️ Prerequisites:
- **Python 3.11.6**
- **MySQL**

---

## 📜 Steps to Use:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PoojaDNaik/RBAC.git
   cd RBAC

Install Dependencies: Use the following command to install required packages:

bash
Copy code
pip install -r requirements.txt
Initialize the Database: Run the initialization script to set up the database:

bash
Copy code
python init_db.py
Start the Server: Launch the FastAPI server:

bash
Copy code
uvicorn main:app --reload
