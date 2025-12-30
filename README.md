
# Credit Card Application Management System (CCAMS)

## 📌 Project Overview
The **Credit Card Application Management System (CCAMS)** is a web-based application developed using **Django, HTML, CSS, and JavaScript**.  
This system allows users to apply for a credit card online, track application status, and enables administrators to manage and approve applications efficiently.

---

## 🚀 Features

### 👤 User Module
- Apply for Credit Card using an online form
- Upload required documents (PAN Card & Address Proof)
- Enter personal, contact, and income details
- Check credit card application status using application number
- Responsive and user-friendly UI

### 🔐 Admin Module
- Secure Admin Login
- View submitted credit card applications
- Verify applicant details
- Approve or reject applications
- Manage application records

---

## 🖥️ Pages Implemented
- Home Page
- Credit Card Application Form
- Check Application Status Page
- Admin Login Page

> **Note:**  
> *About* and *Contact Us* pages were intentionally not implemented as they contain only static informational content related to credit cards and do not affect core project functionality.

---

## 🧱 Project Folder Structure
Credit-Card-Application-Management-System/
│
├── .idea/                          # IDE configuration files
│   ├── inspectionProfiles/
│   ├── CreditCardproject.iml
│   ├── misc.xml
│   └── modules.xml
│
├── CreditCardproject/              # Main Django project
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                 # Project settings
│   ├── urls.py                     # Root URL configuration
│   └── wsgi.py
│
├── myapp/                          # Application module
│   ├── __pycache__/
│   ├── migrations/                 # Database migrations
│   ├── static/                     # CSS, JS, Images
│   ├── templates/                  # HTML templates
│   ├── templatetags/               # Custom template filters
│   ├── __init__.py
│   ├── admin.py                    # Admin configuration
│   ├── apps.py
│   ├── forms.py                    # Django forms
│   ├── models.py                   # Database models
│   ├── tests.py
│   └── views.py                    # Business logic
│
├── media/                          # Uploaded files (PAN, Address Proof)
│
├── db.sqlite3                      # SQLite database
│
├── manage.py                       # Django management script
│
├── README.md                       # Project documentation
│
└── .gitignore                      # Git ignored files
---

## 🛠️ Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Version Control:** Git & GitHub
- **Development Tools:** VS Code

---

## ▶️ How to Run the Project Locally

```bash
# Clone repository
git clone https://github.com/shami0392/Credit-Card-Application-Management-System.git

# Navigate to project folder
cd Credit-Card-Application-Management-System

# Install dependencies
pip install django

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
