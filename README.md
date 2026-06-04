# Contractsys

**Web-based rental contract management system** built with Python and Flask. Allows registering clients, creating contracts with file uploads, and viewing all contracts through a web interface.

---

## Features

- Contract registration with client details (name, CPF, email)
- Address registration (location and ZIP code), rent value and move-in date
- File upload linked to contracts (PDF, DOCX, DOC)
- Direct file download from the system
- Full contract listing
- Data persistence with SQLite
- Web interface with Flask and Jinja2 templates
- User authentication (login/logout)

---

## Tech Stack

| Technology   | Usage                          |
|--------------|--------------------------------|
| Python 3     | Back-end and application logic |
| Flask        | Web framework                  |
| SQLite       | Local database                 |
| Jinja2       | Dynamic HTML templates         |
| HTML / CSS   | User interface                 |
| Git / GitHub | Version control                |

---

## Project Structure

```
Contractsys/
├── app.py           # Main routes and application logic
├── database.py      # Table creation and SQLite operations
├── templates/       # HTML templates (Jinja2)
├── static/          # Static files (CSS, images)
├── uploads/         # User-uploaded files (auto-generated)
└── README.md
```

---

## Getting Started

**Requirements:** Python 3.8+ installed

```bash
# 1. Clone the repository
git clone https://github.com/felipebsa/Contractsys.git
cd Contractsys

# 2. Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

# 3. Install dependencies
pip install flask

# 4. Run the application
python app.py
```

Access at: **http://127.0.0.1:5000**

---

## Available Routes

| Route              | Method     | Description                        |
|--------------------|------------|------------------------------------|
| `/`                | GET        | Home page                          |
| `/cadastrar`       | GET / POST | Contract registration form         |
| `/listar`          | GET        | List all contracts                 |
| `/status`          | GET        | Contract status view               |
| `/download/<id>`   | GET        | Download file linked to a contract |

---

## Data Model

```sql
CREATE TABLE contracts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT    NOT NULL,
    cpf_client  TEXT    NOT NULL,
    location    TEXT    NOT NULL,
    cep         TEXT,
    rent_value  REAL    NOT NULL,
    entry_date  DATE    NOT NULL,
    email       TEXT,
    file_path   TEXT
);
```

---

## Upcoming Improvements

- [ ] Payment status per contract
- [ ] Filters and search in contract listing
- [ ] Input data validation and protection
