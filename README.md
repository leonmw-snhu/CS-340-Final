# 🐾 Animal Shelter Dashboard

This project is a full-stack **Flask + Dash** web application that connects to a **MongoDB** database to visualize and manage animal shelter data. Built for the **CS 499 Computer Science Capstone**, it demonstrates software engineering design, data structures/algorithms, and database integration in a secure, modular, and professional-grade application.

## 📊 Features

- 🔐 User authentication with Flask Blueprints
- 📦 Dash/Flask hybrid layout with secure session handling
- 🧠 Clean MVC architecture
- 📄 Case-insensitive filtering and sorting via `dash-ag-grid`
- 🐶 Shelter record display with MongoDB data integration
- 🔁 Configurable environment via `config.py`
- 🧪 Unit tests for model and visualization logic

## 📂 Project Structure
animal_dashboard/
│
├── app.py                # Main Flask + Dash app initializer
├── config.py             # Configuration file (MongoDB, secret keys)
├── run.py                # Entry point for running the app
│
├── controllers/
│   └── auth_controller.py    # Blueprint for login/auth routes
│
├── models/
│   └── animal_shelter.py     # MongoDB DAO class for CRUD operations
│
├── views/
│   └── layout.py             # Dash layout logic using AgGrid
│
├── templates/
│   └── login.html            # Jinja2 template for login page
│
├── static/                   # Static files (CSS, JS, images, etc.)
│
├── tests/
│   ├── test_model.py         # Unit tests for Mongo model layer
│   └── test_dash.py          # Dash layout and interaction tests
│
├── requirements.txt          # Required Python packages
└── README.md                 # You are here

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/animal-shelter-dashboard.git
cd animal-shelter-dashboard

### 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

### 3. Install Dependencies
pip install -r animal_dashboard/requirements.txt

### 4. Prepopulate MongoDB
sh setup_mongo.sh

### 5. Run the App
python -m animal_dashboard.run

### 6. Access the App
http://127.0.0.1:8050/


🔐 Default Credentials

If using the included login system:
	•	Username: aacuser
	•	Password: password

(Adjust auth_controller.py to define actual logic/storage)

💡 Tech Stack
	•	Frontend: Dash, Dash Bootstrap Components, AG Grid
	•	Backend: Flask, Python 3.13+
	•	Database: MongoDB (local or cloud)
	•	Testing: pytest, unittest

🧪 Testing

To run the included tests:
    pytest tests/


📜 License

This project is for academic purposes under SNHU’s CS 499 curriculum.
⸻
Created with ❤️ for the Capstone Project by Leon Machado-Wilcox.