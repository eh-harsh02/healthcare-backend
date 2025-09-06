# Healthcare Backend System

## Overview
This project is a **Healthcare Backend System** built with **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**. It allows secure management of **Doctors**, **Patients**, and their **mappings**. The system also provides **JWT-based authentication** for secure access to API endpoints.

---

## Features
- **User Authentication**
  - Register new users.
  - Login and receive JWT tokens (access & refresh tokens).
- **Doctor Management**
  - Create, read, update, delete (CRUD) operations for doctors.
- **Patient Management**
  - CRUD operations for patients.
  - Each patient is assigned to a doctor.
- **Patient-Doctor Mapping**
  - Track relationships between patients and doctors.
  - Prevent duplicate mappings using unique constraints.
- **Secure APIs**
  - JWT authentication for all sensitive endpoints.
  - Permissions enforced via DRF `IsAuthenticated`.

---

## Technologies Used
- **Backend:** Django 5.2.6
- **REST API:** Django REST Framework
- **Authentication:** djangorestframework-simplejwt (JWT)
- **Database:** PostgreSQL
- **Environment Management:** Python-decouple
- **Testing:** Postman

---

## Folder Structure

```
healthcare-backend/
│
├── backend/ # Django project configuration
│ ├── settings.py # Project settings
│ ├── urls.py # Project URLs
│ └── wsgi.py
│
├── healthcare/ # Django app
│ ├── models.py # Database models
│ ├── views.py # ViewSets for CRUD
│ ├── views_auth.py # JWT authentication views
│ ├── serializers.py # Serializers for models
│ └── urls.py # App URLs
│
├── venv/ # Virtual environment
├── manage.py
├── requirements.txt
└── .env # Environment variables

```

---

# API Endpoints

## Authentication

| Endpoint           | Method | Description            |
|-------------------|--------|------------------------|
| `/auth/register/`  | POST   | Register a new user    |
| `/auth/login/`     | POST   | Login and get JWT tokens |

## Doctor

| Endpoint                | Method      | Description          |
|-------------------------|------------|--------------------|
| `/api/doctors/`         | GET        | List all doctors     |
| `/api/doctors/`         | POST       | Create a new doctor  |
| `/api/doctors/<id>/`    | PUT/PATCH  | Update doctor info   |
| `/api/doctors/<id>/`    | DELETE     | Delete a doctor      |

## Patient

| Endpoint                 | Method      | Description           |
|--------------------------|------------|---------------------|
| `/api/patients/`         | GET        | List all patients    |
| `/api/patients/`         | POST       | Create a new patient |
| `/api/patients/<id>/`    | PUT/PATCH  | Update patient info  |
| `/api/patients/<id>/`    | DELETE     | Delete a patient     |

## Patient-Doctor Mapping

| Endpoint                  | Method      | Description                  |
|---------------------------|------------|------------------------------|
| `/api/mappings/`          | GET        | List all patient-doctor mappings |
| `/api/mappings/`          | POST       | Create a new mapping         |
| `/api/mappings/<id>/`     | PUT/PATCH  | Update mapping               |
| `/api/mappings/<id>/`     | DELETE     | Delete mapping               |

> **Note:** All endpoints except register and login require JWT token in the header:  
> `Authorization: Bearer <access_token>`

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/eh-harsh02/healthcare-backend.git

   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Windows
   source venv/bin/activate       # macOS/Linux

   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

   ```
4. Run the development server:
   ```bash
   python manage.py runserver

   ```

## 📬 Contact

For any queries or suggestions, feel free to reach out:
📧 [harshraj0381@gmail.com](mailto:harshraj0381@gmail.com)
