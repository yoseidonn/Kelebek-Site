# Kelebek Site
## Description
**Kelebek Site** is a **dynamic marketing website** for **the Kelebek App**, designed to promote the app, provide essential information about its features, and offer an easy-to-use interface for users and developers. In addition to the marketing content, Kelebek also serves as a platform to interact with the app's API, offering functionality for managing and accessing user data, project information, and more.

**The admin panel of the Kelebek Site allows administrators to dynamically create and manage the following elements:**

**Headings:** Customize section titles on the site
**Slides:** Manage image or content sliders for showcasing features or announcements
**Headers:** Define different sections of the site
**Announcements:** Post important messages or updates about the app
These elements are dynamically rendered on the frontend, ensuring that the site remains flexible and up-to-date without requiring code changes, giving administrators control over how content is presented.

The **Kelebek Site** acts as *both a marketing platform and a gateway to the Kelebek App's license verification backend*, allowing users to explore the app's features while developers can interact with the API for app-related operations.

***

## Requirements
Before getting started, ensure you have the following installed:

1. Python 3.x
2. PostgreSQL (for database management but it's optional)

***

## Installation
To set up the project on your local machine, follow these steps:

### Clone the repository:
```
# bash
git clone <repository_url>
cd kelebek-site
```
***

### Create and activate a virtual environment:
``` 
# bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
***

### Install the required dependencies:
```
# bash
pip install -r requirements.txt
```
***

### Apply database migrations:
```
# bash
python manage.py migrate
```
***

### Create a superuser to access the admin panel:
```
# bash
python manage.py createsuperuser
```
***

### Set up your environment variables (OPTIONAL):
Create a .env file in the root directory and configure your database credentials and any other required environment variables *if you want to switch to PostgreSQL or use email services.*

**Locate the .env alongside the venv/ and kelebeksistemi_container/**

Example .env file:

```
POSTGRES={
    "ENGINE": "django.db.backends.postgresql", 
    "HOST": "...", "PORT": "...", "NAME": "", 
    "USER": "postgres", 
    "PASSWORD": "..."}
MAIL={
    "ADDRESS": "<yourmail@email.com>", 
    "PASSWORD": "<passwordForYourEmail>", 
    "USE_SSL": "True", 
    "PORT": "465", 
    "HOST": "smtp.gmail.com", 
    "BACKEND": "django.core.mail.backends.smtp.EmailBackend"}```
``` 
***

### Run the development server:
```
# bash
python manage.py runserver
```
Access the site by visiting http://127.0.0.1:8000 in your web browser.

## Dependencies
The following packages are installed for the project:

```
asgiref==3.8.1
Django==5.1.4
django-phonenumber-field==8.0.0
django-restframework==0.0.1
djangorestframework==3.15.2
idna==3.10
phonenumbers==8.13.52
pillow==11.0.0
psycopg2-binary==2.9.10
pymemcache==4.0.0
python-dotenv==1.0.1
pytz==2024.2
six==1.17.0
sqlparse==0.5.3
typing_extensions==4.12.2
```