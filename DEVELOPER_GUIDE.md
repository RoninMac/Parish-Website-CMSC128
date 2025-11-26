# Virgen Dela Candelaria Parish Website - Developer Guide

## Project Overview
A Django-based website for Virgen Dela Candelaria Parish featuring public pages, email subscriptions, and a custom admin login system.

Other features to be added:
 - Song lyric viewing 
 - announcements that will be sent to the subsribed emails and a announcements page 
 - schedules 
 - priests 
 - donor aknowledgement page 
 - church groups 
 - admin management system for the features mentioned previously
 
**Stack:**
- Backend: Django 5.2
- Frontend: HTML/CSS/JavaScript
- Database: SQLite (default)
- Python: 3.14

---

## Project Structure

```
ChurchWebsite/Website/
├── vcpWebsite/              # Django project configuration
│   ├── settings.py          # Main Django settings (INSTALLED_APPS, DB config)
│   ├── urls.py              # Root URL routing
│   ├── wsgi.py              # WSGI application entry
│   └── asgi.py              # ASGI application entry
│
├── core/                    # Main website app (public pages)
│   ├── views.py             # Page views: home, history, location
│   ├── urls.py              # URL patterns for core app
│   ├── models.py            # (Currently empty - for future features)
│   ├── admin.py             # Admin panel configuration
│   ├── static/
│   │   ├── css/style.css    # Main stylesheet (navbar, footer, cards)
│   │   └── images/          # Hero images and icons
│   └── templates/
│       ├── base.html        # Master template (navbar + footer)
│       ├── index.html       # Home page
│       ├── history.html     # Parish history page
│       └── location.html    # Location/contact page
│
├── people/                  # Email subscription app
│   ├── models.py            # Subscription model (email + timestamp)
│   ├── views.py             # Subscribe form handler
│   ├── urls.py              # URL patterns
│   ├── admin.py             # Admin panel for subscriptions
│   ├── forms.py             # SubscriptionForm (ModelForm)
│   ├── migrations/          # Database migrations
│   └── templates/
│       ├── subscribe.html   # Subscription form page
│       └── thankyouSub.html # Confirmation page
│
├── donations/               # Donation app
│   ├── models.py            # Donation model (if future feature)
│   ├── views.py             # Donate page view
│   ├── urls.py              # URL patterns
│   ├── templates/
│   │   ├── donate.html      # Donation page
│   │   └── thankyou.html    # Donation confirmation
│   └── static/css/style.css
│
├── adminlogin/              # Custom admin login app
│   ├── models.py            # (Empty - uses Django User model)
│   ├── views.py             # Admin login view (TODO: implement logic)
│   ├── urls.py              # URL pattern: /adminlogin/login/
│   ├── apps.py              # App config (name = 'adminlogin')
│   ├── static/
│   │   └── css/
│   │       ├── adminStyle.css    # Login form styling
│   │       └── adminBaseStyle.css # Admin pages layout
│   └── templates/
│       ├── base.html        # Admin base template (navbar + footer)
│       └── login.html       # Admin login form
│
├── songs/                   # Songs/hymns app (not yet implemented)
│
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
├── Pipfile                  # Python dependencies (pipenv)
└── DEVELOPER_GUIDE.md       # This file

```

---

## Installation & Setup

### 1. Install Dependencies
```bash
pipenv install
pipenv shell
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (for Django admin)
```bash
python manage.py createsuperuser
# Enter username, email, password
```

### 4. Start Development Server
```bash
python manage.py runserver
# Open http://127.0.0.1:8000/
```

---

## Key URLs & Routes

| URL | View | Purpose |
|-----|------|---------|
| `/` | core.views.index | Home page |
| `/history/` | core.views.history | Parish history page |
| `/location/` | core.views.location | Location/contact page |
| `/donate/` | donations.views.donate | Donation page |
| `/subscribe/` | people.views.subscribe | Email subscription form |
| `/adminlogin/login/` | adminlogin.views.admin_login | Custom admin login |
| `/admin/` | django.contrib.admin | Django admin panel |

---

## Apps & Responsibilities

### `core` - Public Website
- **Purpose:** Main public-facing pages
- **Views:** Home, History, Location pages (static content)
- **Styling:** Global navbar, footer, card layouts (style.css)
- **Future:** Add dynamic content from models

### `people` - Subscriptions
- **Purpose:** Email subscription management
- **Model:** Subscription (email, created_at)
- **Views:** Subscribe form (GET/POST), confirmation page
- **Admin:** View/export subscribers in Django admin
- **Future:** Email confirmation, double opt-in, unsubscribe

### `donations` - Donations
- **Purpose:** Donation page (currently static)
- **Views:** Donation form (TODO: implement backend)
- **Future:** Integrate payment gateway (Stripe, PayPal)

### `adminlogin` - Custom Admin
- **Purpose:** Custom admin login (separate from Django admin)
- **Status:** Template created, view logic TODO
- **URLs:** /adminlogin/login/
- **Note:** Has its own base.html template (separate navbar/footer styling)

### `songs` - Hymns/Songs
- **Purpose:** Song/hymn management (not yet implemented)
- **Status:** Placeholder app

---

## Important Files & Locations

### Stylesheets
- **Main site:** `core/static/css/style.css` - Navbar, footer, cards
- **Admin login:** `adminlogin/static/css/adminStyle.css` - Login form styling
- **Admin base:** `adminlogin/static/css/adminBaseStyle.css` - Admin pages layout

### Templates
- **Master template:** `core/templates/base.html` (extended by most pages)
- **Admin template:** `adminlogin/templates/base.html` (used by admin pages)
- **Page templates:** Each app has its own templates/ directory

### Static Files
- **Images:** `core/static/images/` (hero.jpg, etc.)
- **Icons:** `core/static/icons/` (facebook.jpg, instagram.jpg, x.jpg)

---

## Common Tasks

### Add a New Page
1. Create view in `core/views.py`:
   ```python
   def new_page(request):
       return render(request, 'new_page.html')
   ```
2. Add URL in `core/urls.py`:
   ```python
   path('new-page/', views.new_page, name='new_page'),
   ```
3. Create template `core/templates/new_page.html` (extends base.html)
4. Add nav link in `core/templates/base.html`

### Access Django Admin
1. Go to `/admin/`
2. Log in with superuser credentials
3. Manage subscriptions, users, permissions

### Collect Static Files (Production)
```bash
python manage.py collectstatic --noinput
```

### Make Database Migrations
```bash
python manage.py makemigrations [app_name]
python manage.py migrate
```

---

## Known Issues & TODOs

### High Priority
- [ ] Consolidate `index()` and `home()` views in core
- [ ] Implement `adminlogin.views.admin_login` authentication logic
- [ ] Add `{% block stylesheets %}` to base.html for per-page CSS overrides

### Medium Priority
- [ ] Add error handling for duplicate emails in subscribe form
- [ ] Implement email confirmation for subscriptions
- [ ] Add location map (Google Maps / Leaflet)
- [ ] Implement donation payment gateway
- [ ] Add responsive design for mobile devices

### Low Priority
- [ ] Implement songs/hymns app
- [ ] Add contact form validation
- [ ] Add social media integration
- [ ] Set up email backend for sending newsletters

---

## Debugging Tips

### Static Files Not Loading
- Ensure app is in `INSTALLED_APPS` in settings.py
- Use `{% static 'path/file' %}` template tag, not hardcoded paths
- Run `python manage.py collectstatic` in production

### Templates Not Found
- Check template file exists in `app/templates/app/`
- Verify `APP_DIRS = True` in settings.py
- App must be in `INSTALLED_APPS` for Django to find templates

### Database Errors
- Run migrations: `python manage.py migrate`
- Check for pending migrations: `python manage.py showmigrations`
- Reset DB (dev only): `rm db.sqlite3 && python manage.py migrate`

### URL Not Resolving
- Check URL patterns in app `urls.py`
- Verify app urls are included in project `urls.py` with `path(..., include(...))`
- Use `python manage.py show_urls` (if django-extensions installed)

---

## Contact & Maintenance
**Last Updated:** November 2025
**Current Maintainer:** [Your Name/Team]

For questions or issues, refer to Django docs: https://docs.djangoproject.com/

---
