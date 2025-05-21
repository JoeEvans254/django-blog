# 📝 Django Blog Platform

A simple, modern blog platform built with **Django** and styled using **Tailwind CSS**. The application allows users to register, log in, create and manage blog posts

---

## 🚀 Features

### ✅ Core Functionality
- User registration and authentication (Writers, Readers)
- Create, edit, and delete blog posts (Writers)
- Blog detail and listing pages with search and sorting

### 💡 UI/UX
- Responsive design using Tailwind CSS CDN
- Clean, minimalist interface
- Image preview and compression on upload

### 🔐 Security
- Password hashing, CSRF protection, session timeouts


---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, TailwindCSS
- **Database**: SQLite (default)
- **Deployment Ready**: Gunicorn + Nginx (recommended)

---

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/JoeEvans254/django-blog.git
cd django-blog
python -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

