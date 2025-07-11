
# 📘 MyFaceclone

A lightweight Facebook clone built with Django — featuring user authentication, profile updates, timeline posts, and friend management. Designed to simulate the core functionality of a social networking platform with clean UI and responsive behavior.

---

## 🎯 Live Demo

🔗 [Try Here](#)  
<!-- Replace # with your deployed live link if available -->

---

## 🔍 Features

* 🔐 Secure login and registration system
* 👤 User profile with avatar, status, and location
* 📝 Create and view posts on the timeline
* 👥 Friend management — add, accept/decline, unfriend
* 🖼 Upload and display user profile pictures
* 📱 Responsive user interface with Bootstrap

---

## 📸 Preview

### 🔹 Authentication Page  
![Authentication Page](screenshots/authentication_page.png)

### 🔹 Home Page  
![Home Page](screenshots/home_page.png)

### 🔹 Profile Page  
![Profile Page](screenshots/profile_page.png)

---

## 🛠 Technologies Used

**Frontend:**
- HTML5
- CSS3 (Bootstrap)
- JavaScript
- Font Awesome

**Backend:**
- Django 3.2+
- SQLite3
- Python 3.8+

---

## 🚀 Quick Start

bash
# Clone the repository
git clone https://github.com/rojalinworks/MyFaceclone

# Navigate to the project directory
cd MyFaceclone

# Create a virtual environment
python -m venv env

# Activate the virtual environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# Install Django
pip install django

# Run migrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
`

Visit `http://127.0.0.1:8000/` in your browser to access the app.

---

## 📁 Project Structure


MyFaceclone/
├── MyFaceclone/             # Main project settings
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Social/                  # App for social features
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/               # HTML templates
│   ├── home.html
│   ├── index.html
│   └── profile.html
├── static/                  # CSS, JS, images, fonts
│   ├── css/
│   ├── js/
│   ├── img/
│   └── fonts/
├── media/                   # Uploaded user avatars
│   └── avatar.jpg
├── screenshots/             # Screenshots for preview
│   ├── authentication_page.png
│   ├── home_page.png
│   └── profile_page.png
├── db.sqlite3               # Database
├── manage.py
└── README.md


---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!
Fork the project and submit a pull request, or open an issue for feedback or bugs.

---

## 📄 License

This project is built for educational purposes and is based on a tutorial.
See [Bootstrap License](https://github.com/twbs/bootstrap/blob/main/LICENSE) for UI library terms.

---

> Built with ❤ using Django by [Rojalin Mohapatra](https://github.com/rojalinworks)



