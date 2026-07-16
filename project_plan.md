# 🍽️ Food Recipe Platform — Django Learning Project

## 📌 Project Overview

A full-featured food recipe sharing platform where users can browse, create, share, and purchase premium recipes. Built with Django to master web development through practical implementation.

**Live URL:** [https://myrecipes-sage.vercel.app](https://myrecipes-sage.vercel.app)

---

## 🧰 Technology Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Django 4.2 + Django REST Framework (planned) |
| **Database** | PostgreSQL (Neon / Railway) |
| **Frontend** | Django Templates + Bootstrap 5 |
| **Authentication** | Django Session Auth + django-allauth |
| **File Storage** | Cloudinary (production) |
| **Deployment** | Vercel |
| **Version Control** | Git + GitHub |

---

## 📅 12-Week Implementation Plan

### ✅ Week 1 — Project Setup & Foundation
- [x] Virtual environment & Django installation
- [x] PostgreSQL setup
- [x] Custom User model with email authentication
- [x] Git repository initialized
- [x] Project structure (`config/`, `apps/`, `templates/`)

### ✅ Week 2 — Core Recipe Models & Admin
- [x] Recipe, Category, Ingredient, Step models
- [x] RecipeImage (multiple images, featured flag)
- [x] Django Admin registration with inline formsets
- [x] Category & Tag system

### ✅ Week 3 — Recipe CRUD Operations
- [x] Recipe creation with dynamic ingredients/steps
- [x] FormSets for nested forms
- [x] Edit & Delete with permission checks
- [x] Featured image selection

### ✅ Week 4 — Recipe Browsing & Display
- [x] Homepage with featured recipes
- [x] Recipe grid/list with pagination
- [x] Recipe detail with ingredients & steps
- [x] Category filtering & search

### ✅ Week 5 — User Interactions (Social Features)
- [x] Like system
- [x] Bookmark/Save system
- [x] Comment system
- [x] Rating system (1–5 stars)
- [x] User profiles with activity feed

### ✅ Week 6 — Following & Notifications
- [x] Follow/Unfollow users
- [x] Feed of followed users' recipes
- [x] Activity feed
- [x] Notification system with unread badges

### ✅ Week 7 — Collections & Recommendations
- [x] Recipe collections (public/private)
- [x] Add/remove recipes to collections
- [x] Personalized recommendations
- [x] Trending recipes section

### ✅ Week 8 — Edit/Delete & User Dashboard
- [x] Recipe edit with ingredient/step management
- [x] Recipe delete with confirmation
- [x] User dashboard
- [x] Profile management (bio, picture, website)

### ✅ Week 9 — Testing & Debugging
- [x] Unit tests for models
- [x] View tests
- [x] Form tests
- [x] Integration tests
- [x] Fixed Python 3.14 compatibility issues

### ✅ Week 10 — Deployment (Vercel)
- [x] Environment variables configuration
- [x] PostgreSQL production database (Neon)
- [x] Cloudinary media storage
- [x] WhiteNoise static files
- [x] Vercel deployment
- [x] Custom landing page

### ⏳ Week 11 — Payments (Chapa Integration)
- [ ] Premium recipe model
- [ ] Chapa API integration
- [ ] Purchase flow
- [ ] Access control for premium content

### ⏳ Week 12 — REST API & Final Polish
- [ ] Django REST Framework setup
- [ ] API endpoints for recipes
- [ ] JWT authentication
- [ ] API documentation (Swagger)
- [ ] Final UI polish & mobile responsiveness

---

## 🚀 What We've Accomplished So Far

### ✅ Key Features Implemented

| Feature | Status |
|---------|--------|
| User Authentication (signup/login) | ✅ |
| Recipe CRUD with ingredients/steps | ✅ |
| Multiple image upload (Cloudinary) | ✅ |
| Category system | ✅ |
| Like / Unlike | ✅ |
| Bookmark / Save | ✅ |
| Comments | ✅ |
| Ratings (1–5 stars) | ✅ |
| User profiles | ✅ |
| Follow / Unfollow | ✅ |
| Activity feed | ✅ |
| Notifications | ✅ |
| Recipe collections | ✅ |
| Search & filtering | ✅ |
| Recommendations | ✅ |
| Trending recipes | ✅ |
| Edit & Delete recipes | ✅ |
| Deployment (Vercel) | ✅ |
| PostgreSQL production DB | ✅ |
| Custom landing page | ✅ |
| Testing suite | ✅ |

---

## 🎯 What's Next

### Immediate Next Steps (Week 11)

1. **Payment Integration (Chapa)**
   - Add `is_premium` and `price` fields to Recipe
   - Integrate Chapa payment gateway
   - Build purchase flow
   - Implement access control for premium recipes

2. **REST API (Week 12)**
   - Django REST Framework setup
   - Serializers for all models
   - JWT authentication
   - API documentation

3. **Final Polish**
   - Mobile responsiveness improvements
   - Loading states & animations
   - Accessibility enhancements
   - User documentation

---

## 📁 Project Structure
ood_recipes_project/
├── apps/
│ ├── accounts/ # User auth & profiles
│ ├── recipes/ # Main recipe app
│ ├── core/ # Homepage & shared views
│ └── notifications/ # Activity & notifications
├── config/ # Django settings
├── templates/ # HTML templates
├── static/ # CSS, JS, images
├── media/ # User uploaded files (Cloudinary)
├── fixtures/ # Data fixtures
├── manage.py
├── requirements.txt
├── Procfile # Vercel deployment
└── README.md


---

## 🌐 Live Links

| Environment | URL |
|-------------|-----|
| **Production** | [https://myrecipes-sage.vercel.app](https://myrecipes-sage.vercel.app) |
| **Admin** | [https://myrecipes-sage.vercel.app/admin/](https://myrecipes-sage.vercel.app/admin/) |
| **GitHub** | [https://github.com/sele01/food-recipes](https://github.com/sele01/food-recipes) |

---

## 📊 Success Metrics

| Metric | Current Status |
|--------|----------------|
| User registration | ✅ Working |
| Recipe creation | ✅ Working |
| Social features | ✅ Working |
| Search & filter | ✅ Working |
| Payment integration | ⏳ Planned |
| API | ⏳ Planned |
| Test coverage | ✅ Partial |
| Documentation | ✅ In progress |

---

## 🧠 Learning Outcomes Achieved

- ✅ Django ORM & complex queries
- ✅ Class-based views
- ✅ Authentication & permissions
- ✅ File uploads & Cloudinary
- ✅ PostgreSQL setup & migrations
- ✅ Deployment to Vercel
- ✅ Testing with Django Test Framework

---

## 📝 Notes

- This plan is a guideline, not a strict rulebook.
- Pace adjusted based on learning speed and real-world challenges.
- Python 3.14 compatibility fixed by upgrading Django and using `psycopg2` instead of `psycopg2-binary`.

---

> 📌 **Last Updated:** July 16, 2026  
> **Status:** Active — Core features complete, Payments & API next.
