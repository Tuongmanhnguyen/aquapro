# 🐟 Aquapro Modernization

**Status:** Active Development / Learning Phase
**Architecture:** Monorepo (Django Backend + Vue Frontend)

This project is a modernization of the Aquapro e-commerce platform. It transitions the legacy system into an in-house, full-stack application using **Django Ninja** (for high-performance, type-safe APIs) and **Vue 3** (for a reactive modern frontend).

---

## 🛠 Tech Stack

### Backend (API)
* **Language:** Python 3.13 (Latest stable)
* **Framework:** Django 5.x
* **API Framework:** Django Ninja (Pydantic-based, Fast, Auto-docs)
* **Server:** Gunicorn (Production), `runserver` (Dev)
* **Database:** SQLite (Dev), PostgreSQL (Planned for Prod)
* **Image Processing:** Pillow

### Frontend (UI)
* **Runtime:** Node.js 20 (LTS)
* **Framework:** Vue 3 (Composition API)
* **Build Tool:** Vite
* **HTTP Client:** Axios
* **Styling:** CSS Modules (Scoped)

### Infrastructure (DevOps)
* **Containerization:** Docker & Docker Compose
* **OS Target:** Ubuntu 22.04 / Azure VMs
* **Reverse Proxy (Dev):** Vite Proxy

---

## 📂 Project Structure (Monorepo)

We use a Monorepo structure to keep the backend logic and frontend UI in sync within a single repository.

```text
aquapro/
├── backend/                  # 🐍 DJANGO ROOT
│   ├── config/               # Project Settings (urls.py, settings.py)
│   ├── core/                 # Main Application Logic
│   │   ├── api.py            # API Endpoints (The "Views")
│   │   ├── models.py         # Database Structure (Product, Category)
│   │   ├── schemas.py        # Pydantic Data Validation (Input/Output)
│   │   └── admin.py          # Internal Admin Panel Config
│   ├── media/                # User-uploaded images (Ignored by Git)
│   └── Dockerfile            # Instructions to build the Backend image
│
├── frontend/                 # ⚡ VUE ROOT
│   ├── src/
│   │   ├── api.js            # Central Axios configuration
│   │   └── App.vue           # Main Product Grid Component
│   ├── vite.config.js        # Configures Proxy (Front -> Back connection)
│   └── package.json          # JS Dependency list
│
├── docker-compose.yml        # Orchestration for running the stack with one command
├── requirements.txt          # Python Dependency list
└── README.md                 # Documentation

🚀 Quick Start: Development Mode
This detailed README.md is designed to be your "Project Bible." It documents not just how to run the code, but why the architecture is set up this way, and specifically points out the files you should look at while you are studying.

Here is the comprehensive version. Copy this entire block into your README.md file.

Markdown

# 🐟 Aquapro Modernization

**Status:** Active Development / Learning Phase
**Architecture:** Monorepo (Django Backend + Vue Frontend)

This project is a modernization of the Aquapro e-commerce platform. It transitions the legacy system into an in-house, full-stack application using **Django Ninja** (for high-performance, type-safe APIs) and **Vue 3** (for a reactive modern frontend).

---

## 🛠 Tech Stack

### Backend (API)
* **Language:** Python 3.13 (Latest stable)
* **Framework:** Django 5.x
* **API Framework:** Django Ninja (Pydantic-based, Fast, Auto-docs)
* **Server:** Gunicorn (Production), `runserver` (Dev)
* **Database:** SQLite (Dev), PostgreSQL (Planned for Prod)
* **Image Processing:** Pillow

### Frontend (UI)
* **Runtime:** Node.js 20 (LTS)
* **Framework:** Vue 3 (Composition API)
* **Build Tool:** Vite
* **HTTP Client:** Axios
* **Styling:** CSS Modules (Scoped)

### Infrastructure (DevOps)
* **Containerization:** Docker & Docker Compose
* **OS Target:** Ubuntu 22.04 / Azure VMs
* **Reverse Proxy (Dev):** Vite Proxy

---

## 📂 Project Structure (Monorepo)

We use a Monorepo structure to keep the backend logic and frontend UI in sync within a single repository.

```text
aquapro/
├── backend/                  # 🐍 DJANGO ROOT
│   ├── config/               # Project Settings (urls.py, settings.py)
│   ├── core/                 # Main Application Logic
│   │   ├── api.py            # API Endpoints (The "Views")
│   │   ├── models.py         # Database Structure (Product, Category)
│   │   ├── schemas.py        # Pydantic Data Validation (Input/Output)
│   │   └── admin.py          # Internal Admin Panel Config
│   ├── media/                # User-uploaded images (Ignored by Git)
│   └── Dockerfile            # Instructions to build the Backend image
│
├── frontend/                 # ⚡ VUE ROOT
│   ├── src/
│   │   ├── api.js            # Central Axios configuration
│   │   └── App.vue           # Main Product Grid Component
│   ├── vite.config.js        # Configures Proxy (Front -> Back connection)
│   └── package.json          # JS Dependency list
│
├── docker-compose.yml        # Orchestration for running the stack with one command
├── requirements.txt          # Python Dependency list
└── README.md                 # Documentation
🚀 Quick Start: Development Mode
Recommended for learning and writing code. Runs services directly on your machine.

Prerequisites
Python 3.13

Node.js 20+

1. Start the Backend
Open a terminal, navigate to the project root:

# 1. Create/Activate Virtual Env (if not already active)
# Note: We use Python 3.13 explicitly
source venv/bin/activate

# 2. Install Dependencies (only if new deps were added)
pip install -r requirements.txt

# 3. Apply Database Migrations (if models changed)
python backend/manage.py migrate

# 4. Run Server
python backend/manage.py runserver

2. Start the Frontend
Open a second terminal:

cd frontend

# 1. Install Dependencies (only if package.json changed)
npm install

# 2. Run Dev Server
npm run dev

🐳 Quick Start: Docker Mode

Recommended for checking if the app works in a "Production-like" environment.

# From the project root
docker compose up -d --build

# Check logs
docker compose logs -f backend

API: http://localhost:8000/api/products

Note: Currently, the Frontend is not Dockerized in Compose yet (Roadmap item), so you still run the frontend via npm run dev.

📚 Learning Guide (For the "Pause")
Since we are pausing to study, here is how the current codebase maps to the concepts you need to learn:

1. Django Models (The "S" in SQL)
Study File: backend/core/models.py

Concept: Look at how models.ForeignKey connects Product to Category. This is the relational database theory applied in Python.

Key Term: "ORM" (Object Relational Mapper).

2. Django Ninja Schemas (The Validation)
Study File: backend/core/schemas.py

Concept: Notice how ProductIn (what the user sends) is different from ProductOut (what we send back). We use Pydantic to ensure data is strictly typed.

Key Term: "Serialization" and "Type Hinting".

3. Vue Reactivity (The "V" in View)
Study File: frontend/src/App.vue

Concept: Look at ref([]). This makes the products variable "reactive"—when the data arrives from the API, the HTML updates automatically without refreshing the page.

Key Term: "Composition API" and "Lifecycle Hooks (onMounted)".

🗺 Roadmap & Next Steps
Phase 1: Backend Polish (Current)
[x] Setup Python 3.13 & Django Ninja

[x] Create Product & Category Models

[x] Implement Image Uploading

[x] Implement Search & Pagination

[ ] Next: Add Authentication (Login/Logout)

Phase 2: Frontend Structure
[x] Setup Vue 3 & Vite Proxy

[x] Basic Product Grid

[ ] Next: Install Vue Router (to click on a product and go to a Details page)

[ ] Next: Build a Navigation Bar component

Phase 3: Infrastructure (DevOps)
[x] Dockerize Backend

[x] Docker Compose Setup

[ ] Next: Move SQLite to PostgreSQL

[ ] Next: Move local media/ folder to Azure Blob Storage

[ ] Next: GitHub Actions (CI/CD)

