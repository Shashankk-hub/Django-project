# Django Blog Project

This is a full-featured blog application built with Django 5.2.12, allowing users to create profiles, publish posts, and interact with the platform.

## Features
- **User Authentication:** Registration, login, and logout functionalities using Django's built-in authentication system.
- **User Profiles:** Each user can have their own profile with a customizable profile picture.
- **Blog Content Management:** Users can seamlessly create, read, update, and delete their own blog posts.
- **Pagination:** The main blog feed is paginated to enhance user experience and performance.
- **Crispy Forms:** Integrates `django-crispy-forms` with Bootstrap 5 to render clean, responsive, and beautiful forms.

## Technologies Used
- **Backend:** Python, Django 5.2.12
- **Database:** SQLite
- **Frontend/Styling:** HTML, Bootstrap 5

## Setup and Installation

Follow these steps to get the development environment running locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shashankk-hub/Django-project.git
   ```

2. **Navigate to the project's source directory:**
   ```bash
   cd Django-project/CSW2_blogapp/django_project1
   ```

3. **Install dependencies:**
   Make sure you have your virtual environment activated, then install the necessary packages.
   ```bash
   pip install django django-crispy-forms crispy-bootstrap5 Pillow
   ```
   *(Note: `Pillow` is required for image processing with the User Profile models)*

4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure
- `blog/`: Contains the core blogging app (views for posts, models, URLs).
- `users/`: Contains authentication logic and user profile models.
- `django_project1/`: The main configuration package with global routing and settings.
