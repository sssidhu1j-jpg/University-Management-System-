# 🎓 University Management System (UMS)

An enterprise-ready University Management System built with **Python**, **Django**, and **Bootstrap**. This platform streamlines academic and administrative operations—including student admissions, course allocations, online quizzes, grade processing, and tuition fee payments.

---

## 🌟 Key Features

| Module | Description |
| :--- | :--- |
| **🔐 Accounts & Roles** | Multi-role authentication (Admin, Lecturer/Professor, Student, Registrar) with custom profile management. |
| **📚 Course Management** | Course creation, syllabus organization, course materials, and semester-based student enrollments. |
| **📝 Online Quiz System** | Create quizzes, randomized questions, timed examinations, and instant automated grading. |
| **📊 Results & Grading** | Automatic GPA/CGPA calculation, grade sheets, student transcripts, and downloadable PDF reports. |
| **💳 Tuition Payments** | Integrated online payment processing (Stripe & GoPay) for semester fees and payment receipts. |
| **🔍 Search & Filter** | Global search across students, faculty, departments, and course catalogs. |
| **⚡ REST API** | Built-in Django REST Framework (DRF) endpoints for mobile or external service integrations. |

---

## 📁 Simple Project Architecture

The repository is structured logically to separate backend logic and assets:

```plaintext
University-Management-System/
│
├── backend/                      # Django application core
│   ├── manage.py                 # Django command-line utility
│   ├── config/                   # Global project settings and URL routing
│   │
│   ├── accounts/                 # User authentication, roles, and profiles
│   ├── course/                   # Courses, subjects, and enrollments
│   ├── quiz/                     # Assessments, quizzes, and questions
│   ├── result/                   # Grades, transcripts, and scoring
│   ├── payments/                 # Stripe/GoPay invoice & payment processing
│   ├── search/                   # Global search engine
│   ├── core/                     # Core dashboard, AI chat helper, and utilities
│   │
│   ├── templates/                # Bootstrap HTML templates
│   ├── static/                   # CSS stylesheets, JavaScript, and UI icons
│   ├── media/                    # User-uploaded files (avatars, documents)
│   ├── requirements/             # Environment dependencies (base, local, production)
│   ├── requirements.txt          # Requirements entry point
│   └── .env.example              # Environment variables template
│
├── api/                          # Serverless entrypoint
│   └── index.py
│
├── .gitignore                    # Prevents cache, venv, and secrets from committing
└── README.md                     # Documentation
```

---

## 🚀 Getting Started

### Prerequisites

- **Python**: 3.10 or higher
- **Git**

---

### Step-by-Step Local Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/sssidhu1j-jpg/University-Management-System-.git
cd University-Management-System-
```

#### 2. Create and Activate a Virtual Environment
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r backend/requirements.txt
```

#### 4. Configure Environment Variables
Copy `.env.example` into `backend/.env`:
```bash
# Windows
Copy-Item backend\.env.example backend\.env

# Linux / macOS
cp backend/.env.example backend/.env
```

#### 5. Apply Database Migrations
```bash
python backend/manage.py migrate
```

#### 6. Create an Admin Account
```bash
python backend/manage.py createsuperuser
```
Follow the prompts to enter your username, email, and password.

#### 7. Start the Development Server
```bash
python backend/manage.py runserver
```

Now open your browser and visit:
- 🌐 **Web Application**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- ⚙️ **Admin Portal**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🛠️ Built With

- **Framework**: [Django](https://www.djangoproject.com/)
- **API**: [Django REST Framework](https://www.django-rest-framework.org/)
- **Frontend**: HTML5, CSS3, JavaScript, [Bootstrap 5](https://getbootstrap.com/)
- **Database**: SQLite (default) / PostgreSQL (production)
- **PDF Generation**: ReportLab & xhtml2pdf
- **Payment Gateways**: Stripe, GoPay

---

## 👤 Author

- GitHub: [@sssidhu1j-jpg](https://github.com/sssidhu1j-jpg)
