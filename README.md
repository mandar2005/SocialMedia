# Social Media Web App 🌐📱

A **Django-based social media platform** that allows users to create profiles, post content, follow other users, like posts, and explore content shared by others — similar to Instagram.

---

## 🚀 Features

- ✅ User authentication (Sign up / Login / Logout)
- 🖼️ Upload images and videos
- ❤️ Like/unlike posts
- 🧑‍🤝‍🧑 Follow/unfollow users
- 👤 View profile with posts
- 🔍 Explore page to discover other users and content
- 📷 Lightbox support for media previews
- 📅 Posts sorted by recency

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/index.html) (default)
- HTML, CSS, Bootstrap
- [uikit](https://getuikit.com/) (for lightbox/media UI)

---

## 📂 Project Structure

```
SocialMedia/
├── core/                  # Main app for posts, profiles, and logic
├── templates/             # HTML templates
├── static/                # CSS, JS, and images
├── media/                 # User-uploaded media
├── manage.py              # Django management script
├── db.sqlite3             # Database (default)
└── requirements.txt       # Python dependencies
```

---

## 🧑‍💻 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/mandar2005/SocialMedia.git
cd SocialMedia
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🖼️ Media Handling in Development

Make sure `MEDIA_URL` and `MEDIA_ROOT` are set in `settings.py`. Add this in `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## ✨ Future Enhancements

- 💬 Commenting on posts
- 📨 Messaging system
- 🛎️ Notifications
- 📊 Analytics for post likes/views

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Mandar**  
GitHub: [@mandar2005](https://github.com/mandar2005)

---
