# CSW2_blogapp

A dynamic Django-based blog application with full database integration and Bootstrap 5 styling.

## 🚀 Features
- Custom User `Post` model management via Django Admin
- Bootstrap 5 responsive layout and navigation
- Fully integrated SQLite database
- Dynamic template inheritance

## 🛠️ Requirements
- Python 3.10+
- Django 5.2.12

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aryan1196/CSW2_blogapp.git
   cd CSW2_blogapp
   ```

2. **Create a Virtual Environment**
   It's highly recommended to run this project inside a virtual environment to isolate the dependencies.
   ```bash
   # On Windows
   python -m venv djangoEnv
   djangoEnv\Scripts\activate

   # On macOS/Linux
   python3 -m venv djangoEnv
   source djangoEnv/bin/activate
   ```

3. **Install Dependencies**
   *Note: Since there is no `requirements.txt` yet, you only need to ensure Django is installed.*
   ```bash
   pip install django
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Optional)**
   To access the Django Admin dashboard and manage your Posts:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   Open your browser and navigate to `http://127.0.0.1:8000/`.
