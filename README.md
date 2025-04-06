🔩 Django Multi-Layered Web App with API

This is a multi-layered Django web application project built to demonstrate how to integrate a basic API within a Django app. The project includes both frontend rendering (via Django templates) and API endpoints for backend interaction.

**⚠️ Note:** This project is intended to run locally (localhost) and is not deployed.
Anyone who wishes to explore or build upon this can clone the repo and use it on their own machine.

**🚀 Features**

- Multi-layered Django structure (URLs, Views, Models, Templates)
- API to submit and retrieve data (e.g., poll votes)
- Pre-configured SQLite database
- HTML templates rendered on index.html
- CSRF-exempt endpoint for API interaction
- Ready for extension with forms, authentication, or frontend frameworks

**💠 Setup Instructions**

**1. Clone the Repository**
```bash
git clone https://github.com/060205b/Django_Multilayered_webpage_API.git
cd Django_Multilayered_webpage_API/Multi_layered_upgraded
```

**2. Create Virtual Environment (optional but recommended)**
```bash
python -m venv env
```
**On macOS/Linux:**
```bash
source env/bin/activate
```
**On Windows:**
```bash
env\Scripts\activate
```

**3. Install Required Packages**
```bash
pip install django django-cors-headers
```

**4. Run Database Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Start the Server**
```bash
python manage.py runserver
```

📍 **The server will start at:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**📱 API Endpoints**

✅ **POST** `/submit_vote/`
Submit a vote or similar data.

**Headers:**
```http
Content-Type: application/json
```

**Body Example:**
```json
{
  "vote_option": "OptionA"
}
```

✅ **GET** `/api/data/`
Get all submissions stored in the database as a JSON response.

**🗃️ Database Info**

The database used is SQLite (local, file-based).
It stores records from the API — for example:
- Voting results from `/submit_vote/`
- All user submissions collected by the backend

(No forms are used; data is captured directly via frontend JS or tools like Postman)

**📁 Project Structure**
```
Multi_layered_upgraded/
├── myapp/
│   ├── views.py        # Handles rendering & API logic
│   ├── urls.py         # Routes for app-specific pages
│   ├── models.py       # Stores submission data
│   └── templates/myapp/index.html
│
├── myproject/
│   └── urls.py         # Main URL router
│
├── db.sqlite3          # Local database file
├── manage.py
└── README.md           # This file
```

**🔄 Project Flow (Simplified)**

1. 🧑‍💻 User submits a vote or data via frontend or Postman
2. 🔁 API endpoint (`/submit_vote/`) receives and parses the request
3. 🧠 Django backend (`views.py`) processes the data
4. 🗃️ Data is stored using Django ORM into `db.sqlite3` (SQLite DB)
5. 🌐 When `/api/data/` is requested:
   - Backend fetches all saved records from the database
   - Sends them as a JSON response

> Even though data is returned as JSON, it's actually saved in `db.sqlite3`.

**🔧 Tech Stack**

- Python 3.x
- Django 4.x
- SQLite (default DB)
- Django REST-like functionality (without DRF)

**💡 Future Ideas / Contributions**

- Add user login & authentication
- Replace raw API with Django REST Framework
- Add a frontend (React, Vue, or even plain JS) to hit API
- Deploy to Heroku or Railway

**🙌 Author**

Made with 💻 by [@060205b](https://github.com/060205b)

**📄 License**

MIT License — free to use, modify, or extend.

