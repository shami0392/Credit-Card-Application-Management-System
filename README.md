# Credit Card Application Management System (CCAMS)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=flat&logo=gunicorn&logoColor=white)](https://gunicorn.org/)

## Table of Contents

- [Introduction](#introduction)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the Application](#running-the-application)
- [Features & Routes](#features--routes)
    - [Public Routes](#public-routes)
    - [Admin Authentication](#admin-authentication)
    - [Application Processing](#application-processing)
    - [Sub-Admin Management](#sub-admin-management)
    - [Reports & Analytics](#reports--analytics)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Database Schema](#database-schema)
- [View Functions](#view-functions)
- [Configuration](#configuration)
- [Security Features](#security-features)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a production-ready Credit Card Application Management System built with Django. The application provides a comprehensive platform for users to apply for credit cards online while enabling administrators and sub-bankers to efficiently manage, verify, and approve applications. It features a complete admin workflow with document uploads, application tracking, status management, and detailed reporting capabilities.

## Architecture

The system is composed of several core components:

- **Public Application Interface**: User-facing credit card application submission
- **Admin Dashboard**: Centralized dashboard showing application statistics and status counts
- **Authentication System**: Secure login for admin and sub-banker users
- **Application Processing**: Complete workflow for reviewing, approving, and rejecting applications
- **Sub-Admin Management**: Role-based access with sub-banker accounts
- **Document Management**: Secure file storage for uploaded documents
- **Tracking System**: Historical tracking of application status changes
- **Reporting Module**: Date-based and search-based reporting capabilities
- **Static File Management**: WhiteNoise integration for production static file serving

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)
- [Git](https://git-scm.com/downloads)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (recommended)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/shami0392/Credit-Card-Application-Management-System.git
    cd Credit-Card-Application-Management-System
    ```

2. Create and activate a virtual environment:

    ```sh
    # Windows
    python -m venv venv
    venv\Scripts\activate
    
    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory (optional for local development):

    ```env
    # Django Configuration
    SECRET_KEY=your_secret_key_here
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    
    # Database Configuration
    DATABASE_URL=sqlite:///db.sqlite3
    
    # Static Files
    STATIC_URL=/static/
    MEDIA_URL=/media/
    
    # Email Configuration (optional)
    EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your_email@gmail.com
    EMAIL_HOST_PASSWORD=your_app_password
    ```

### Running the Application

1. Apply database migrations:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Create a superuser for admin access:

    ```sh
    python manage.py createsuperuser
    ```

3. Collect static files (for production):

    ```sh
    python manage.py collectstatic --noinput
    ```

4. Run the development server:

    ```sh
    python manage.py runserver
    ```

5. The application will be available at:
    - Main Application: `http://127.0.0.1:8000/`
    - Admin Dashboard: `http://127.0.0.1:8000/dashboard/`
    - Django Admin: `http://127.0.0.1:8000/admin/`

## Features & Routes

### Public Routes

#### Home Page
```http
GET /
```

Displays the landing page with credit card offerings and information.

**Template:** `index_home.html`

#### About Page
```http
GET /about/
```

Displays information about the credit card services and company.

**Template:** `index_about.html`

#### Contact Page
```http
GET /contact-us/
```

Displays contact information and support details.

**Template:** `index_contact.html`

#### Credit Card Application Submission
```http
POST /apply/
Content-Type: multipart/form-data

{
  "fullname": "John Doe",
  "email": "john@example.com",
  "mobile": "9876543210",
  "pan_number": "ABCDE1234F",
  "address": "123 Main Street, City",
  "annual_income": "500000",
  "documents": [<files>]
}
```

**Response:**
- Generates unique 10-digit registration number
- Redirects to home with success message
- Message includes application tracking number

#### Track Application Status
```http
POST /track/
Content-Type: application/x-www-form-urlencoded

fromdate=<application_number_or_search_term>
```

**Features:**
- Search by full name, mobile, email, or registration number
- Displays application details and current status
- Shows all matching applications

**Template:** `index_search.html`

### Admin Authentication

#### Admin Login
```http
GET /authentication_login/
POST /authentication_login/

{
  "username": "admin",
  "password": "password123"
}
```

**Features:**
- Validates user credentials
- Checks for staff status
- Creates session and redirects to dashboard
- Error handling for invalid users

**Template:** `authentication-login.html`

#### Logout
```http
GET /logout/
```

**Features:**
- Clears user session
- Displays success message
- Redirects to login page

#### Change Password
```http
POST /change-password/
Authentication: Required

{
  "pwd1": "new_password",
  "pwd2": "confirm_password",
  "pwd3": "old_password"
}
```

**Features:**
- Validates new password matches confirmation
- Updates user password securely
- Redirects to home after success

**Template:** `change_password.html`

### Application Processing

#### Admin Dashboard
```http
GET /dashboard/
Authentication: Required
```

**Displays:**
- Total number of sub-bankers
- New applications count (Not Updated Yet)
- Approved applications count
- Rejected applications count

**Template:** `admin_dashboard.html`

#### View Applications List
```http
GET /applications/?action=<filter>
Authentication: Required
```

**Filter Options:**
- `action=New` - Shows applications with status "Not Updated Yet"
- `action=Approved` - Shows approved applications
- `action=Rejected` - Shows rejected applications
- `action=All` - Shows all applications

**Template:** `applicationlist.html`

#### Application Detail & Action
```http
GET /detail/<application_id>/
POST /detail/<application_id>/
Authentication: Required

{
  "remark": "Verification complete",
  "limit": "50000",
  "status": "Approved"
}
```

**Features:**
- View complete application details
- Add remarks and credit limit
- Update application status
- Creates tracking history entry
- Displays full tracking timeline

**Template:** `detail.html`

#### Delete Application
```http
POST /delete-application/<application_id>/
Authentication: Required
```

**Features:**
- Permanently removes application
- Shows success message
- Redirects to applications list

### Sub-Admin Management

#### Add Sub-Banker
```http
GET /add-subadmin/
POST /add-subadmin/
Authentication: Required

{
  "username": "subadmin1",
  "firstname": "John",
  "email": "john@bank.com",
  "password": "secure_password",
  "mobile": "9876543210"
}
```

**Features:**
- Creates new user account
- Associates user with Subbanker profile
- Sets up permissions and access

**Template:** `add_subadmin.html`

#### Edit Sub-Banker
```http
GET /edit-subadmin/<subadmin_id>/
POST /edit-subadmin/<subadmin_id>/
Authentication: Required
```

**Features:**
- Updates existing sub-banker details
- Modifies user information
- Updates contact details

#### View All Sub-Bankers
```http
GET /view-subadmin/
Authentication: Required
```

**Features:**
- Lists all sub-banker accounts
- Shows contact information
- Provides edit/delete options

**Template:** `view_subadmin.html`

#### Delete Sub-Banker
```http
POST /delete-subadmin/<subadmin_id>/
Authentication: Required
```

**Features:**
- Removes sub-banker account
- Cascades to associated user
- Shows confirmation message

### Reports & Analytics

#### Date Range Report
```http
POST /report-date/
Authentication: Required

{
  "fromdate": "2025-01-01",
  "todate": "2025-01-31"
}
```

**Features:**
- Filters applications by creation date range
- Displays all applications within period
- Supports custom date selection

**Template:** `report_date.html`

#### Search Report
```http
POST /search-report/
Authentication: Required

{
  "fromdate": "<search_term>"
}
```

**Features:**
- Search by full name or registration number
- Displays matching applications
- Admin-only access

**Template:** `search_report.html`

#### Update About Page
```http
POST /about-admin/
Authentication: Required

{
  "pagetitle": "About Our Services",
  "description": "Detailed description..."
}
```

**Features:**
- Updates About page content
- Modifies page title and description
- Admin content management

#### Update Contact Page
```http
POST /contact-admin/
Authentication: Required

{
  "pagetitle": "Contact Us",
  "description": "Contact information...",
  "email": "support@bank.com",
  "mobile": "1800-XXX-XXXX"
}
```

**Features:**
- Updates Contact page content
- Modifies contact details
- Admin content management

#### Admin Profile Management
```http
POST /profile/
Authentication: Required

{
  "firstname": "John",
  "email": "john@bank.com",
  "username": "johndoe",
  "mobile": "9876543210"
}
```

**Features:**
- Update admin user information
- Modify contact details
- Change profile settings

**Template:** `profile.html`

## Project Structure

```
Credit-Card-Application-Management-System/
├── CreditCardproject/              # Main Django project
│   ├── __init__.py
│   ├── asgi.py                     # ASGI configuration
│   ├── settings.py                 # Project settings (production-ready)
│   ├── urls.py                     # URL routing configuration
│   └── wsgi.py                     # WSGI configuration for deployment
├── myapp/                          # Core application module
│   ├── migrations/                 # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── static/                     # Static assets
│   │   ├── css/
│   │   │   ├── style.css           # Main stylesheet
│   │   │   └── responsive.css      # Responsive design
│   │   ├── js/
│   │   │   ├── main.js             # Main JavaScript
│   │   │   └── validation.js       # Form validation
│   │   └── fonts/
│   │       └── ElegantIcons/       # Icon font files
│   ├── templates/                  # HTML templates
│   │   ├── base.html               # Base template
│   │   ├── index_home.html         # Home page
│   │   ├── index_about.html        # About page
│   │   ├── index_contact.html      # Contact page
│   │   ├── index_search.html       # Application tracking
│   │   ├── authentication-login.html  # Admin login
│   │   ├── admin_dashboard.html    # Dashboard
│   │   ├── applicationlist.html    # Applications list
│   │   ├── detail.html             # Application details
│   │   ├── add_subadmin.html       # Add sub-banker
│   │   ├── view_subadmin.html      # View sub-bankers
│   │   ├── change_password.html    # Change password
│   │   ├── profile.html            # User profile
│   │   ├── report_date.html        # Date range report
│   │   ├── search_report.html      # Search report
│   │   ├── about.html              # Admin: Edit About
│   │   └── contact.html            # Admin: Edit Contact
│   ├── __init__.py
│   ├── admin.py                    # Django admin configuration
│   ├── apps.py                     # App configuration
│   ├── forms.py                    # Django forms (ApplicationForm, SubbankerForm)
│   ├── models.py                   # Database models
│   ├── views.py                    # View functions
│   ├── urls.py                     # App-level URL routing
│   └── tests.py                    # Unit tests
├── media/                          # User-uploaded files
│   └── documents/                  # Application documents
├── staticfiles/                    # Collected static files (production)
├── db.sqlite3                      # SQLite database
├── manage.py                       # Django management script
├── Procfile                        # Render deployment configuration
├── requirements.txt                # Python dependencies
├── runtime.txt                     # Python runtime version
├── .gitignore                      # Git ignore rules
├── LICENSE                         # MIT License
└── README.md                       # Project documentation
```

## Technologies Used

- **Django**: High-level Python web framework for rapid development
- **Python**: Primary programming language (3.8+)
- **SQLite**: Lightweight database for development and small deployments
- **WhiteNoise**: Static file serving for production
- **Gunicorn**: Production WSGI HTTP server
- **HTML5/CSS3**: Frontend markup and styling
- **JavaScript**: Client-side interactivity and validation
- **ElegantIcons**: Custom icon font
- **Bootstrap** (optional): Responsive UI framework

## Database Schema

### Application Model

```python
class Application(models.Model):
    """Credit card application with complete applicant details"""
    
    # Unique identifier
    regnumber = models.CharField(max_length=20, unique=True)
    
    # Personal Information
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    dateofbirth = models.DateField()
    
    # Identity & Address
    pan_number = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    
    # Employment & Income
    occupation = models.CharField(max_length=100)
    annual_income = models.DecimalField(max_digits=12, decimal_places=2)
    
    # Documents (uploaded files)
    pan_card = models.FileField(upload_to='documents/')
    address_proof = models.FileField(upload_to='documents/')
    income_proof = models.FileField(upload_to='documents/', blank=True)
    
    # Application Status
    status = models.CharField(
        max_length=20, 
        default='Not Updated Yet',
        choices=[
            ('Not Updated Yet', 'Pending Review'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected')
        ]
    )
    limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Timestamps
    creationdate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'applications'
        ordering = ['-creationdate']
        verbose_name = 'Credit Card Application'
        verbose_name_plural = 'Credit Card Applications'
    
    def __str__(self):
        return f"{self.regnumber} - {self.fullname}"
```

### Subbanker Model

```python
class Subbanker(models.Model):
    """Sub-admin users who can manage applications"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    
    # Additional fields
    designation = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'subbankers'
        verbose_name = 'Sub Banker'
        verbose_name_plural = 'Sub Bankers'
    
    def __str__(self):
        return f"{self.user.username} - {self.user.first_name}"
```

### TrackingHistory Model

```python
class Trackinghistory(models.Model):
    """Historical tracking of application status changes"""
    
    application = models.ForeignKey(
        Application, 
        on_delete=models.CASCADE,
        related_name='tracking_history'
    )
    remark = models.TextField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
    )
    
    class Meta:
        db_table = 'tracking_history'
        ordering = ['-created_at']
        verbose_name = 'Tracking History'
        verbose_name_plural = 'Tracking Histories'
    
    def __str__(self):
        return f"{self.application.regnumber} - {self.status}"
```

### About Model

```python
class About(models.Model):
    """About page content management"""
    
    pagetitle = models.CharField(max_length=200)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'about'
        verbose_name = 'About Page'
        verbose_name_plural = 'About Pages'
```

### Contact Model

```python
class Contact(models.Model):
    """Contact page content management"""
    
    pagetitle = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact Page'
        verbose_name_plural = 'Contact Pages'
```

### Running Migrations

```sh
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Rollback migration
python manage.py migrate myapp <migration_name>
```

## View Functions

### Public View Functions

```python
def index(request)
    """Display home page"""

def index_about(request)
    """Display about page with content from database"""

def index_contact(request)
    """Display contact page with information"""

def add_application(request, pid=None)
    """
    Handle credit card application submission
    - Generates unique 10-digit registration number
    - Saves application with documents
    - Supports editing existing applications
    """

def index_search(request)
    """
    Track application status
    - Search by name, mobile, email, or registration number
    - Public access for applicants
    """
```

### Authentication View Functions

```python
def authentication_login(request)
    """
    Admin/Sub-banker login
    - Validates credentials
    - Checks staff status
    - Creates session
    """

@login_required
def logout_user(request)
    """Logout and clear session"""

@login_required
def change_password(request)
    """
    Change user password
    - Validates new password confirmation
    - Updates password securely
    """
```

### Admin Dashboard View Functions

```python
@login_required
def dashboard(request)
    """
    Admin dashboard with statistics
    - Total sub-bankers
    - New applications count
    - Approved applications count
    - Rejected applications count
    """

@login_required
def applicationlist(request)
    """
    List applications with filters
    - Filter by status (New, Approved, Rejected, All)
    - Paginated results
    """

@login_required
def detail(request, pid)
    """
    Application detail and action page
    - View complete application
    - Add remarks and credit limit
    - Update status
    - Create tracking history
    """

@login_required
def delete_application(request, pid)
    """Delete application permanently"""
```

### Sub-Admin Management View Functions

```python
@login_required
def add_subadmin(request, pid=None)
    """
    Add or edit sub-banker
    - Create new user account
    - Associate with Subbanker profile
    - Update existing sub-banker
    """

@login_required
def view_subadmin(request)
    """List all sub-bankers"""

@login_required
def delete_subadmin(request, pid)
    """Delete sub-banker account"""
```

### Reporting View Functions

```python
@login_required
def report_date(request)
    """
    Generate date range report
    - Filter by creation date range
    - Display applications within period
    """

@login_required
def search_report(request)
    """
    Search-based report
    - Search by name or registration number
    - Admin-only access
    """
```

### Content Management View Functions

```python
@login_required
def about(request)
    """Update About page content"""

@login_required
def contact(request)
    """Update Contact page content"""

@login_required
def profile(request)
    """Update admin profile information"""
```

### Utility Functions

```python
def random_with_N_digits(n)
    """
    Generate random N-digit number
    - Used for application registration numbers
    - Returns 10-digit unique identifier
    """
```

## Configuration

### settings.py Configuration

```python
# Security Settings
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static Files Configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'myapp/static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media Files Configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# File Upload Settings
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB

# Login Settings
LOGIN_URL = '/authentication_login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/authentication_login/'
```

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `SECRET_KEY` | Django secret key for cryptographic signing | - | Yes |
| `DEBUG` | Enable debug mode (use False in production) | `False` | Yes |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `localhost` | Yes |
| `DATABASE_URL` | Database connection string | SQLite | No |
| `EMAIL_BACKEND` | Email backend for notifications | Console | No |
| `EMAIL_HOST` | SMTP server hostname | - | No |
| `EMAIL_PORT` | SMTP server port | `587` | No |
| `EMAIL_HOST_USER` | SMTP username | - | No |
| `EMAIL_HOST_PASSWORD` | SMTP password | - | No |

## Security Features

- **CSRF Protection**: Django's built-in CSRF token validation on all forms
- **XSS Prevention**: Template auto-escaping and input sanitization
- **SQL Injection Protection**: Django ORM parameterized queries
- **Authentication Required**: `@login_required` decorator on sensitive views
- **Staff Status Check**: Additional validation for admin-only operations
- **Secure File Uploads**: File type validation and secure storage
- **Password Hashing**: PBKDF2 algorithm with SHA256 hash
- **Session Security**: Secure, HTTP-only cookies in production
- **HTTPS Enforcement**: Secure cookie flags when deployed
- **Error Handling**: Try-catch blocks for authentication failures
- **Content Security Policy**: Headers to prevent XSS attacks

## Development

### Development Server

Run the development server with auto-reload:

```sh
python manage.py runserver
```

For custom host/port:

```sh
python manage.py runserver 0.0.0.0:8000
```

### Database Management

```sh
# Create database backup
python manage.py dumpdata > backup.json

# Load data from backup
python manage.py loaddata backup.json

# Reset database
python manage.py flush

# Open database shell
python manage.py dbshell
```

### Django Shell

```sh
# Open Django shell
python manage.py shell

# Example usage
>>> from myapp.models import Application
>>> applications = Application.objects.all()
>>> applications.count()
>>> 
>>> # Create test application
>>> app = Application.objects.create(
...     fullname="Test User",
...     email="test@example.com",
...     mobile="9876543210",
...     pan_number="ABCDE1234F",
...     regnumber="1234567890"
... )
```

### Code Quality

```sh
# Check for issues
python manage.py check

# Run code formatter (Black)
black .

# Run linter (Flake8)
flake8 .

# Run type checker (mypy)
mypy .

# Security check
bandit -r myapp/
```

## Testing

### Running Tests

```sh
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test myapp

# Run specific test case
python manage.py test myapp.tests.ViewTestCase

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html

# Run with verbose output
python manage.py test --verbosity=2
```

### Test Structure

```
myapp/
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_views.py
│   ├── test_forms.py
│   └── test_authentication.py
```

### Example Test Cases

```python
from django.test import TestCase, Client
from django.contrib.auth.models import User
from myapp.models import Application, Subbanker

class ApplicationTestCase(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testadmin',
            password='testpass123',
            is_staff=True
        )
        
    def test_application_creation(self):
        """Test application creation"""
        app = Application.objects.create(
            fullname="John Doe",
            email="john@example.com",
            mobile="9876543210",
            pan_number="ABCDE1234F",
            regnumber="1234567890",
            annual_income=500000
        )
        self.assertEqual(app.status, 'Not Updated Yet')
        self.assertEqual(app.fullname, 'John Doe')
    
    def test_admin_login(self):
        """Test admin authentication"""
        response = self.client.post('/authentication_login/', {
            'username': 'testadmin',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to dashboard
    
    def test_dashboard_requires_login(self):
        """Test dashboard authentication requirement"""
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
```

## Deployment

### Render Deployment

This project is optimized for deployment on [Render](https://render.com/).

#### Deployment Configuration

**Procfile:**
```
web: gunicorn CreditCardproject.wsgi:application
```

**Build Command:**
```sh
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

**Start Command:**
```sh
gunicorn CreditCardproject.wsgi:application
```

#### Render Environment Variables

Set these in your Render dashboard:

```env
PYTHON_VERSION=3.11.0
SECRET_KEY=<generate-secure-random-key>
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
DATABASE_URL=<render-postgres-url>
```

#### Deployment Steps

1. Push code to GitHub:
```sh
git add .
git commit -m "Deploy to Render"
git push origin main
```

2. Create new Web Service on Render
3. Connect your GitHub repository
4. Configure environment variables
5. Deploy
