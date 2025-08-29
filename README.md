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

## 3. Running the Project
Run the CLI using:

```
python run.py

```

You will see a menu like this:

=== Clinic Appointment Scheduler ===
1. Create Patient
2. List Patients
3. Create Doctor
4. List Doctors
5. Schedule Appointment
6. List Appointments
0. Exit
Select an option:


## LICENSE

MIT License

Copyright (c) [2025] [Gladys Achando]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.








