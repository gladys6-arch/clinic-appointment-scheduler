# 🏥 Clinic Appointment Scheduler 

## 📌 About the Project
The **Clinic Appointment Scheduler** is a python command-line application that helps manage patients, doctors, and appointments in a clinic.

It uses:
- **SQLAlchemy ORM** for database interactions
- **Alembic** for database migrations
- **Click** / menu- driven CLI for user interaction

With this app, you can:
✔️ Add and view patients

✔️ Add and  view doctors

✔️ Schedule and view appointments


## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/yourusername/clinic-appointment-scheduler.git

```

```
cd clinic-appointment-scheduler

```

### 2. Create and Activate a Virtual Environment

On Linux/macOS

```
python3 -m venv clinic-env

```

```
clinic-env\Scripts\activate

```

### 3. Install Dependencies
If using pip:

```
pip install -r requirements.txt

```

or manually install:

```
pip install sqlalchemy alembic click tabulate

```

### 4. Initialize the Database
Run Alembic migrations to set up the database tables:

```
alembic upgrade head

```








